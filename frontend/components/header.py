import streamlit as st

def render_header():
    """Render a top navbar for DocInsight."""
    st.markdown(
        """
        <style>
            .navbar {
                background-color: #1e1e1e;  /* Dark background */
                padding: 15px;
                text-align: center;
                font-size: 24px;
                color: white;
                font-weight: bold;
                border-bottom: 3px solid #00adb5;  /* Red accent border */
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
        </style>
        <div class="navbar">
            📄 DocInsight — AI Powered Document Summarizer
        </div>
        """,
        unsafe_allow_html=True
    )
