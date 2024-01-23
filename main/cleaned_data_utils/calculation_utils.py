import streamlit as st
from PIL import Image
from security_utils import check_password

# Page configuration must be at the top
try:
    icon = Image.open('invoke_logo.png')
    st.set_page_config(
        layout="wide",
        page_icon=icon,
        initial_sidebar_state="expanded"
    )
except FileNotFoundError:
    st.error("Error loading the logo. Please check the file path.")

# Authentication check
if check_password():
    # The rest of your Streamlit app goes here
    st.write("Hai Faiq")
