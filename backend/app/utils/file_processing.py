import os
import io
import tempfile
from typing import Tuple
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

def save_uploaded_file(file, upload_dir: str) -> str:
    """
    Save an uploaded file to a specified directory.
    
    Args:
        file: The file object to save.
        upload_dir (str): The directory where the file should be saved.
    
    Returns:
        str: The file path of the saved file.
    """
    try:
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        return file_path
    except Exception as e:
        raise ValueError(f"Failed to save uploaded file: {str(e)}")

def extract_text_from_file(file_path: str) -> str:
    """
    Extract text from supported document types (e.g., PDF, Word, PPT, Excel).
    
    Args:
        file_path (str): The path to the file.
    
    Returns:
        str: The extracted text content.
    """
    try:
        # Example for PDF extraction, extend this for other formats.
        if file_path.endswith(".pdf"):
            from PyPDF2 import PdfReader
            reader = PdfReader(file_path)
            text = "".join([page.extract_text() for page in reader.pages])
            return text
        else:
            raise ValueError("Unsupported file type for text extraction")
    except Exception as e:
        raise ValueError(f"Failed to extract text from file: {str(e)}")

def delete_temp_file(file_path: str) -> None:
    """
    Delete a temporary file to free up space.
    
    Args:
        file_path (str): The path to the file to delete.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        raise ValueError(f"Failed to delete temporary file: {str(e)}")

def extract_text_and_images(file_stream):
    doc = fitz.open(stream=file_stream, filetype="pdf")
    combined_text = ""
    images = []

    for page in doc:
        combined_text += page.get_text()
        for img in page.get_images(full=True):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            images.append(image_bytes)
            text_from_image = pytesseract.image_to_string(Image.open(io.BytesIO(image_bytes)))
            combined_text += "\n" + text_from_image

    return combined_text, images
