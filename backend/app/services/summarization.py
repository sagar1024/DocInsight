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
