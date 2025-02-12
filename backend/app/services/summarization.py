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
            extracted_text = pytesseract.image_to_string(image)
            image_text_content += extracted_text + "\n"  # Append extracted text
            image_count += 1
            
    # Merge document text and image text before summarization
    combined_text = text_content + "\n" + image_text_content

    # Simple text summarization (can be replaced with NLP-based summarization)
    summary = await summarize_text(combined_text)

    return {
        "summary": summary,
        "images": image_count
    }

async def summarize_text(text: str) -> str:
    """
    Uses the Gemini API to analyze the document text and generate a summary.
    """
    prompt = f"Summarize the following document:\n\n{text[:5000]}"  # Limit to 5000 characters
    response = await call_gemini_api(prompt)
    return response
