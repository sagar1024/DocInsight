import streamlit as st

def render_footer():
    """Renders the footer."""
    st.markdown(
        """
        <hr style="margin-top: 30px; margin-bottom: 10px;">
        <div style="text-align: center; font-size: 14px; color: gray;">
            © 2025 DocInsight. All rights reserved. | 
            <a href="https://www.docinsight.com" target="_blank" style="text-decoration: none; color: gray;">Visit Website</a> |
            <a href="mailto:support@docinsight.com" style="text-decoration: none; color: gray;">Contact Support</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
