import streamlit as st
from security_utils import check_password
from PIL import Image


# configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
                page_title='Fahmi Hensem 🧮',
                layout="wide",
                page_icon = icon,
                initial_sidebar_state="expanded"
                )
st.write("faiq lagi hensem")
if check_password():
    
    st.write("fahmi hensem")