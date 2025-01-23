import os
import tempfile
from typing import Tuple

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
