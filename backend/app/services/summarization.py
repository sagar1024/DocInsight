import io
import fitz  #PyMuPDF
from PIL import Image
import pytesseract

async def process_document(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    combined_text = ""
    images = []

    for page in doc:
        # Extract text from the page
        combined_text += page.get_text()

        # Extract images and perform OCR
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(image_bytes)
            text_from_image = pytesseract.image_to_string(Image.open(io.BytesIO(image_bytes)))
            combined_text += "\n" + text_from_image

    # Analyze the combined text (with image OCR results)
    summary = generate_summary(combined_text)
    return {"summary": summary, "images": len(images)}

async def process_document(file):
    combined_text, images = extract_text_and_images(file)
    summary = generate_summary(combined_text)
    return {"summary": summary, "images": len(images)}

def generate_summary(text):
    # Placeholder for summary generation logic
    # Replace with advanced summarization methods if needed
    return text[:1000]  # Truncate to 1000 characters for demonstration
