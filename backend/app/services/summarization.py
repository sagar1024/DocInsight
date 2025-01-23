# import textract
# from typing import Optional
# from transformers import pipeline

# # Load a transformer-based summarization model
# summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

# def extract_text_from_file(file_path: str) -> str:
#     """
#     Extract text content from uploaded files.
#     Supports PDF, Word, Excel, and PowerPoint files.
#     """
#     try:
#         text = textract.process(file_path).decode("utf-8")
#         return text
#     except Exception as e:
#         raise ValueError(f"Error extracting text from file: {e}")

# def summarize_text(
#     text: str, 
#     max_length: int = 200, 
#     min_length: int = 50, 
#     language: str = "en"
# ) -> str:
#     """
#     Summarize a given text using a transformer-based model.
#     """
#     if not text or len(text.split()) < 10:
#         raise ValueError("Text too short for summarization.")
    
#     try:
#         # Generate summary
#         summary = summarization_pipeline(
#             text, 
#             max_length=max_length, 
#             min_length=min_length, 
#             do_sample=False
#         )[0]["summary_text"]
        
#         # Optionally, language translation could be added here
#         # if a specific language is required.
        
#         return summary
#     except Exception as e:
#         raise ValueError(f"Error summarizing text: {e}")

from app.utils.nlp_utils import generate_summary

async def summarize_document(content: str, length: str = "medium") -> str:
    """
    Generate a summary for the provided document content.
    
    Args:
        content (str): The document's content.
        length (str): The desired summary length (e.g., "short", "medium", "long").
    
    Returns:
        str: The summarized content.
    """
    try:
        summary = generate_summary(content, length)
        return summary
    except Exception as e:
        raise ValueError(f"Failed to summarize document: {str(e)}")
