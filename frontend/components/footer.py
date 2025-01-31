# import streamlit as st

# def render_footer():
#     """Renders the footer."""
#     st.markdown(
#         """
#         <hr style="margin-top: 30px; margin-bottom: 10px;">
#         <div style="text-align: center; font-size: 14px; color: gray;">
#             © 2025 DocInsight. All rights reserved. | 
#             <a href="https://www.docinsight.com" target="_blank" style="text-decoration: none; color: gray;">Visit Website</a> |
#             <a href="mailto:support@docinsight.com" style="text-decoration: none; color: gray;">Contact Support</a>
#         </div>
#         """,
#         unsafe_allow_html=True,
#     )

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
                background-color: white;
                text-align: center;
                font-size: 14px;
                color: gray;
                padding: 10px 0;
                z-index: 1000;
                border-top: 1px solid #e1e1e1;
            }
            .footer a {
                text-decoration: none;
                color: gray;
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
