import streamlit as st
from components.auth_forms import render_login_form, render_signup_form

def render_auth_page():
    """Renders the authentication page with login and signup options."""
    st.title("Welcome to DocInsight!")
    auth_option = st.radio("Choose an option:", ["Login", "Sign Up"])

    if auth_option == "Login":
        user_data = render_login_form()
        if user_data:
            st.write(f"User {user_data['email']} logged in!")  # Replace with authentication handling
    elif auth_option == "Sign Up":
        user_data = render_signup_form()
        if user_data:
            st.write(f"User {user_data['email']} signed up!")  # Replace with registration handling
