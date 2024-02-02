import streamlit as st
import run as page1_run
import run as page2_run
import run as page3_run

def run():
    st.sidebar.title('Navigation')
    selection = st.sidebar.radio("Go to", ["IVR Data Cleaner & Pre-Processor", "Questionnaire Definer","Keypresses Decoder"])

    if selection == "IVR Data Cleaner & Pre-Processor":
        with st.spinner(f"Loading {selection} ..."):
            page1_run()
    
    elif selection == "Questionnaire Definer":
        with st.spinner(f"Loading {selection} ..."):
            page2_run()
            
    elif selection == "Keypresses Decoder":
        with st.spinner(f"Loading {selection} ..."):
            page3_run()

if __name__ == "__main__":
    run()

    