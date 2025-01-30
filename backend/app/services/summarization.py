import io
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import spacy
from transformers import pipeline

# Load NLP models
nlp = spacy.load("en_core_web_sm")  # For basic text processing
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")  # Pretrained summarization model

async def process_document(file):
    combined_text, images = extract_text_and_images(file)
    summary = generate_summary(combined_text)
    return {"summary": summary, "images": len(images)}

def extract_text_and_images(file):
    """
    Extracts text and images from a PDF file, performing OCR on images if necessary.
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    combined_text = ""
    images = []

    for page in doc:
        # Extract text from the page
        combined_text += page.get_text() + "\n"

        # Extract images and perform OCR
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(image_bytes)  # Store image bytes
            
            # Perform OCR on the image
            text_from_image = pytesseract.image_to_string(Image.open(io.BytesIO(image_bytes)))
            combined_text += "\n" + text_from_image

    return combined_text, images

def generate_summary(text):
    """
    Generates a summary from extracted text using NLP techniques.
    """
    # Preprocess text: Remove unnecessary whitespace and limit input size
    doc = " ".join(text.split())[:4000]  # Truncate text to 4000 characters for efficiency
    
    if len(doc) < 200:
        return doc  # If text is too short, return as is

    # Use Transformer-based summarization
    summary = summarizer(doc, max_length=500, min_length=100, do_sample=False)
    return summary[0]["summary_text"]
