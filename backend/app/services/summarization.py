import numpy as np
import re
import cv2
import fitz  #PyMuPDF for PDF processing
import io
import pytesseract
from PIL import Image
from fastapi import UploadFile
from app.utils.external_api import call_gemini_api

async def process_document(file: io.BytesIO):
    """
    Process the uploaded document to extract text and images.
    Performs OCR on images if necessary and generates a text summary.
    """
    text_content = ""
    image_text_content = ""  # Store extracted text from images
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
            processed_image = preprocess_image(image)
            extracted_text = pytesseract.image_to_string(processed_image)
            
            extracted_text = clean_extracted_text(extracted_text)
            
            image_text_content += extracted_text + "\n"  # Append extracted text
            image_count += 1
            
    # Merge document text and image text before summarization
    combined_text = (text_content + "\n" + image_text_content).strip()
    if not combined_text:
        return {"summary": "No content to summarize", "images": image_count}

    # Simple text summarization (can be replaced with NLP-based summarization)
    summary = await summarize_text(combined_text)

    return {
        "summary": summary,
        "images": image_count
    }

# async def summarize_text(text: str) -> str:
#     """
#     Uses the Gemini API to analyze the document text and generate a summary.
#     """
#     prompt = f"Summarize the following document:\n\n{text[:5000]}"  # Limit to 5000 characters
#     response = await call_gemini_api(prompt)
#     return response

async def summarize_text(text: str) -> str:
    # Split into chunks if text is too long
    chunk_size = 5000
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]

    # Summarize each chunk and combine results
    summaries = [await call_gemini_api(f"Summarize the following document:\n\n{chunk}") for chunk in chunks]

    # Combine summaries into a final summary
    return "\n".join(summaries)


#HELPER functions -

def preprocess_image(image):
    # Convert to grayscale
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

    # Rescale the image to improve OCR accuracy
    scale_factor = 2  # Adjust as needed
    height, width = gray.shape[:2]
    resized = cv2.resize(gray, (width * scale_factor, height * scale_factor), interpolation=cv2.INTER_LINEAR)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(resized, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Optional: Denoise the image
    denoised = cv2.fastNlMeansDenoising(thresh, None, 30, 7, 21)

    return Image.fromarray(denoised)

def clean_extracted_text(text):
    # Remove non-ASCII characters
    cleaned_text = re.sub(r'[^\x00-\x7F]+', ' ', text)
    
    # Remove extra whitespace
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    
    return cleaned_text
