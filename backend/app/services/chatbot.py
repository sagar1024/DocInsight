from app.integrations.gemini_api import generate_chatbot_reply

def get_chatbot_response(query: str, document_text: str = "") -> str:
    """
    Processes the user query with optional document context and returns a chatbot response.

    Args:
        query (str): The user's input query.
        document_text (str, optional): Context extracted from a document to improve response quality.

    Returns:
        str: The chatbot's response.
    """
    try:
        # Combine the query with document context if provided
        prompt = f"Document Context: {document_text[:2000]}\n\nUser Query: {query}" if document_text else query
        
        # Call the Gemini API to get a response
        response = generate_chatbot_reply(prompt)
        return response
    except Exception as e:
        return f"Error generating chatbot response: {str(e)}"
