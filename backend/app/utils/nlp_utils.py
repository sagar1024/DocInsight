from transformers import pipeline

def generate_summary(text: str, length: str = "medium") -> str:
    """
    Generate a summary of the given text using a pre-trained NLP model.
    
    Args:
        text (str): The input text to summarize.
        length (str): Desired summary length ("short", "medium", "long").
    
    Returns:
        str: The generated summary.
    """
    try:
        summarizer = pipeline("summarization")
        max_length_map = {
            "short": 50,
            "medium": 100,
            "long": 150,
        }
        max_length = max_length_map.get(length, 100)
        summary = summarizer(text, max_length=max_length, min_length=25, do_sample=False)
        return summary[0]["summary_text"]
    except Exception as e:
        raise ValueError(f"Failed to generate summary: {str(e)}")
