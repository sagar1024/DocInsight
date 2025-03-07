import streamlit as st

def render_login_form():
    """Renders the login form and returns the user input."""
    st.subheader("Login")
    with st.form(key="login_form"):
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        submit_button = st.form_submit_button(label="Login")

    if submit_button:
        if email and password:
            st.success("Login successful!")  #Replace with actual authentication logic
            return {"email": email, "password": password}
        else:
            st.error("Please fill in all fields.")
            return None
    return None

def render_signup_form():
    """Renders the signup form and returns the user input."""
    st.subheader("Sign Up")
    with st.form(key="signup_form"):
        username = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        submit_button = st.form_submit_button(label="Sign Up")

    if submit_button:
        if not username or not email or not password or not confirm_password:
            st.error("Please fill in all fields.")
            return None

        if password != confirm_password:
            st.error("Passwords do not match.")
            return None

        st.success("Sign up successful!")  #Replace with actual registration logic
        return {"username": username, "email": email, "password": password}

    return None
