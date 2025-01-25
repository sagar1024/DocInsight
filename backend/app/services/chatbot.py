from app.utils.external_api import gemini_chatbot_api

# async def handle_chat_query(query: str, document_context: str = "") -> str:
#     """
#     Process a query using the Gemini API and return the response.
    
#     Args:
#         query (str): The user's query.
#         document_context (str): Additional document context to refine the chatbot response.
    
#     Returns:
#         str: The chatbot's response.
#     """
#     try:
#         response = gemini_chatbot_api(query, context=document_context)
#         return response
#     except Exception as e:
#         raise ValueError(f"Failed to process chatbot query: {str(e)}")

async def query_chatbot(query, document_text):
    # Combine the user's query with document context
    prompt = f"Document Context: {document_text[:2000]}\n\nUser Query: {query}"
    response = await call_gemini_api(prompt)
    return response
