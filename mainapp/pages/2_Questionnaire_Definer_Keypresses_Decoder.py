import streamlit as st
from PIL import Image
from modules.security_utils import check_password

# Configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
    page_title='IVR Data Cleaner 🧮',
    layout="wide",
    page_icon=icon,
    initial_sidebar_state="expanded"
)

def set_dark_mode_css():
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
    st.markdown(dark_mode_css, unsafe_allow_html=True)

# Call the function to apply the dark mode CSS
set_dark_mode_css()

def run():
    st.title('Page 2: Data Analysis')

    if 'cleaned_data' in st.session_state:
        cleaned_data = st.session_state['cleaned_data']
        st.write("Preview of Cleaned Data:")
        st.dataframe(cleaned_data.head())
    else:
        st.error("No cleaned data found. Please go back to Page 1 and process your data first.")

if __name__ == "__main__":
    run()
