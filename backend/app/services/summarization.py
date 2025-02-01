# import fitz  # PyMuPDF
# from PIL import Image
# import pytesseract
# import spacy
# import io
# from transformers import pipeline
# from app.utils.file_processing import extract_text_and_images

# # Load NLP models
# # nlp = spacy.load("en_core_web_sm")  # For basic text processing
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Pretrained summarization model

# async def process_document(file):
#     combined_text, images = extract_text_and_images(file)
#     summary = generate_summary(combined_text)
#     return {"summary": summary, "images": len(images)}

# def generate_summary(text):
#     """
#     Generates a summary from extracted text using NLP techniques.
#     """
#     # Preprocess text: Remove unnecessary whitespace and limit input size
#     doc = " ".join(text.split())[:4000]  # Truncate text to 4000 characters for efficiency
    
#     if len(doc) < 200:
#         return doc  # If text is too short, return as is

#     # Use Transformer-based summarization
#     summary = summarizer(doc, max_length=500, min_length=100, do_sample=False)
#     return summary[0]["summary_text"]

#ALTERNATE -

from transformers import pipeline
import io
import fitz  # PyMuPDF for PDF processing
import pytesseract
from PIL import Image
from fastapi import UploadFile

async def process_document(file: io.BytesIO):
    """
    Process the uploaded document to extract text and images.
    Performs OCR on images if necessary and generates a text summary.
    """
    text_content = ""
    image_count = 0
    pdf_document = fitz.open(stream=file.read(), filetype="pdf")  # Read PDF

    for page in pdf_document:
        # Extract text from each page
        text_content += page.get_text("text") + "\n"

        # Extract images from each page
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))

            # Perform OCR on the image
            text_content += pytesseract.image_to_string(image)
            image_count += 1

    # Simple text summarization (can be replaced with NLP-based summarization)
    summary = summarize_text(text_content)

    return {
        "summary": summary,
        "images": image_count
    }

# def summarize_text(text: str) -> str:
#     """
#     Simple summarization: Return first 3 sentences.
#     You can replace this with an advanced model (e.g., Hugging Face, Gemini API).
#     """
#     sentences = text.split(". ")
#     return ". ".join(sentences[:3]) + "..." if len(sentences) > 3 else text

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text: str) -> str:
    """
    Uses a pre-trained BART summarization model to generate a better summary.
    """
    if len(text) < 100:
        return text  # If the text is short, return it as is

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]
