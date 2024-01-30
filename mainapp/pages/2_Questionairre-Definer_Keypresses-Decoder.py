import streamlit as st
from PIL import Image
from security_utils import check_password

# Configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
    page_title="Questionairre-Definer-Keypresses-Decoder 🧮",
    page_icon="icon",
    layout="wide",
    initial_sidebar_state="expanded"
   )

def set_dark_mode_css():
    # Define CSS for dark mode
    dark_mode_css = """
    <style>
        html, body, [class*="View"] {
            color: #ffffff;  /* Text Color */
            background-color: #111111;  /* Background Color */
        }
        .stTextInput > div > div > input {
            color: #ffffff;
            background-color: #111111;
        }
        .stCheckbox > label {
            color: #ffffff;
        }
        /* Add other widget-specific styles here */
    </style>
    """
    # Inject CSS into the Streamlit app
    st.markdown(dark_mode_css, unsafe_allow_html=True)

# Call the function to apply the dark mode
set_dark_mode_css()

if check_password():
   st.write(f"Total files processed:")

