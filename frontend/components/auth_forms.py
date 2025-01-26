# import streamlit as st
# from utils.api_client import login_user, register_user

# def render_auth_forms():
#     """Render Authentication Forms."""
#     st.title("Login or Register")
#     st.markdown(
#         """
#         Please login to access personalized features or register for a new account.
#         """
#     )
    
#     # Tabs for Login and Register
#     auth_tabs = st.tabs(["Login", "Register"])
    
#     with auth_tabs[0]:
#         st.subheader("Login")
#         username = st.text_input("Username", key="login_username")
#         password = st.text_input("Password", type="password", key="login_password")
        
#         if st.button("Login"):
#             if username and password:
#                 user = login_user(username, password)
#                 if user:
#                     st.session_state["user"] = user
#                     st.success(f"Welcome back, {user['username']}!")
#                     st.session_state["show_auth_forms"] = False
#                 else:
#                     st.error("Invalid credentials. Please try again.")
#             else:
#                 st.warning("Please enter both username and password.")

#     with auth_tabs[1]:
#         st.subheader("Register")
#         new_username = st.text_input("Username", key="register_username")
#         new_password = st.text_input("Password", type="password", key="register_password")
#         confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        
#         if st.button("Register"):
#             if new_password != confirm_password:
#                 st.error("Passwords do not match.")
#             elif new_username and new_password:
#                 user = register_user(new_username, new_password)
#                 if user:
#                     st.success("Registration successful! You can now log in.")
#                 else:
#                     st.error("Registration failed. Username might already be taken.")
#             else:
#                 st.warning("Please fill all fields.")

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
            st.success("Login successful!")  # Replace with actual authentication logic
            return {"email": email, "password": password}
        else:
            st.error("Please fill in all fields.")
            return None
    return None


def render_signup_form():
    """Renders the signup form and returns the user input."""
    st.subheader("Sign Up")
    with st.form(key="signup_form"):
        name = st.text_input("Name", placeholder="Enter your full name")
        email = st.text_input("Email", placeholder="Enter your email")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        submit_button = st.form_submit_button(label="Sign Up")

    if submit_button:
        if not name or not email or not password or not confirm_password:
            st.error("Please fill in all fields.")
            return None

        if password != confirm_password:
            st.error("Passwords do not match.")
            return None

        st.success("Sign up successful!")  # Replace with actual registration logic
        return {"name": name, "email": email, "password": password}

    return None
