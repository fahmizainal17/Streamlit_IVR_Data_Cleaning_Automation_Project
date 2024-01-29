import streamlit as st
from PIL import Image
from security_utils import check_password

if check_password():
    # The rest of your Streamlit app goes here
    st.write("Hai Faiq")
