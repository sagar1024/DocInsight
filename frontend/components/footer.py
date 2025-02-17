import streamlit as st

def render_footer():
    """Renders the footer and sticks it to the bottom."""
    st.markdown(
        """
        <style>
            .footer {
                position: fixed;
                bottom: 0;
                left: 0;
                width: 100%;
                background-color: #1f1f1f;  /* Dark grayish background */
                color: #ffffff;  /* White text */
                text-align: center;
                font-size: 14px;
                padding: 10px 0;
                z-index: 1000;
                border-top: 1px solid #333333;  /* Dark border */
            }
            .footer a {
                text-decoration: none;
                color: #4CAF50;  /* Green for links */
            }
            .footer a:hover {
                color: #80E27E;  /* Lighter green for hover effect */
            }
        </style>
        <div class="footer">
            © 2025 DocInsight. All rights reserved. | 
            <a href="https://www.docinsight.com" target="_blank">Visit Website</a> | 
            <a href="mailto:support@docinsight.com">Contact Support</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
