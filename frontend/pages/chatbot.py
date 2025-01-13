import streamlit as st
from utils.api_client import query_chatbot

def render():
    """Render the Chatbot Page."""
    st.title("Interactive Chatbot")
    st.markdown(
        """
        Ask questions about your documents or general queries! Powered by the Gemini API, 
        the chatbot provides precise and context-aware answers.
        """
    )

    # Chat interface
    st.subheader("Chat Interface")
    chat_history = st.session_state.get("chat_history", [])
    user_query = st.text_input("Your Question", placeholder="Type your question here...")

    if st.button("Ask"):
        if user_query.strip():
            # Call backend API
            response = query_chatbot(user_query)

            if response:
                # Append to chat history
                chat_history.append({"user": user_query, "bot": response})
                st.session_state["chat_history"] = chat_history

                # Display chat history
                for chat in chat_history:
                    st.write(f"**You**: {chat['user']}")
                    st.write(f"**Bot**: {chat['bot']}")
                    st.markdown("---")
            else:
                st.error("Failed to get a response from the chatbot. Please try again.")
        else:
            st.warning("Please enter a question.")

    # Clear chat history
    if st.button("Clear Chat"):
        st.session_state["chat_history"] = []
        st.success("Chat history cleared.")

