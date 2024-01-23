import streamlit as st
from PIL import Image

def password_entered():
    """Checks whether a password entered by the user is correct."""
    # Ensure 'password' key exists in session state and secrets are configured properly
    if "password" in st.session_state and "login" in st.secrets and "LOGIN_PASSWORD" in st.secrets["login"]:
        if st.session_state["password"] == st.secrets["login"]["LOGIN_PASSWORD"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Remove password from session state for security
        else:
            st.session_state["password_correct"] = False
    else:
        st.error("Password checking failed. Please check your Streamlit secrets configuration.")

def check_password():
    """Displays a password input and checks the password."""
    if "password_correct" not in st.session_state or not st.session_state["password_correct"]:
        st.header("INVOKE Automation Survey 🧑‍⚖️")
        
        # Load and display image (include error handling for image loading)
        try:
            image = Image.open('images/invoke_logo.png')
            st.image(image)
        except FileNotFoundError:
            st.error("Error loading the logo. Please check the file path.")
        
        # Password input field
        st.text_input("Please enter your password", type="password", on_change=password_entered, key="password")
        
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("😕 Password incorrect")
        
        return False
    else:
        # Password is correct
        return True
