import streamlit as st
from utils.api_client import login_user, register_user

def render_auth_forms():
    """Render Authentication Forms."""
    st.title("Login or Register")
    st.markdown(
        """
        Please login to access personalized features or register for a new account.
        """
    )
    
    # Tabs for Login and Register
    auth_tabs = st.tabs(["Login", "Register"])
    
    with auth_tabs[0]:
        st.subheader("Login")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Login"):
            if username and password:
                user = login_user(username, password)
                if user:
                    st.session_state["user"] = user
                    st.success(f"Welcome back, {user['username']}!")
                    st.session_state["show_auth_forms"] = False
                else:
                    st.error("Invalid credentials. Please try again.")
            else:
                st.warning("Please enter both username and password.")

    with auth_tabs[1]:
        st.subheader("Register")
        new_username = st.text_input("Username", key="register_username")
        new_password = st.text_input("Password", type="password", key="register_password")
        confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
        
        if st.button("Register"):
            if new_password != confirm_password:
                st.error("Passwords do not match.")
            elif new_username and new_password:
                user = register_user(new_username, new_password)
                if user:
                    st.success("Registration successful! You can now log in.")
                else:
                    st.error("Registration failed. Username might already be taken.")
            else:
                st.warning("Please fill all fields.")
