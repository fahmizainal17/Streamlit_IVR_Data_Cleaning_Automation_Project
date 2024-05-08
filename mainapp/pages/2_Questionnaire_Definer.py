import streamlit as st
from PIL import Image
import json
import re
from modules.questionnaire_utils_page2 import parse_questions_and_answers, parse_text_to_json, rename_columns

# Configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
    page_title='IVR Data Cleaner 🧮',
    layout="wide",
    page_icon=icon,
    initial_sidebar_state="expanded"
)

def set_dark_mode_css():
    # Apply dark mode CSS to the Streamlit app.
    dark_mode_css = """
    <style>
        html, body, [class*="View"] {
            color: #ffffff;  /* Text Color */
            background-color: #111111;  /* Background Color */
        }
        .stTextInput > div > div > input, .stFileUploader > div > div > button {
            color: #ffffff;
            background-color: #111111;
        }
        .stCheckbox > label, .stButton > button {
            color: #ffffff;
        }
        /* Add other widget-specific styles here */
    </style>
    """
    st.markdown(dark_mode_css, unsafe_allow_html=True)

set_dark_mode_css()  # Call the function to apply the dark mode CSS

def run1():
    st.title('Questionnaire Definer🎡')
    st.markdown("### Upload Script Files (.txt, .json format)")

    uploaded_file = st.file_uploader("Choose a txt with formatting or json with flow-mapping file", type=['txt','json'])
    file_parsed = False  # Track if a file has been parsed

    if uploaded_file is not None:
        file_contents = uploaded_file.getvalue().decode("utf-8")

        if uploaded_file.type == "application/json":
            try:
                json_data = json.loads(file_contents)
                parsed_data = parse_questions_and_answers(json_data)
                st.session_state['qa_dict'] = parsed_data
                st.success("JSON questions and answers parsed successfully.✨")
                file_parsed = True
            except json.JSONDecodeError:
                st.error("Error decoding JSON. Please ensure the file is a valid JSON format.")
        else:  # For text format
            parsed_data = parse_text_to_json(file_contents)
            st.session_state['qa_dict'] = parsed_data
            st.success("Text questions and answers parsed successfully.✨")
            file_parsed = True

     # Section for manual and auto-filled renaming
    st.markdown("## Rename Columns")
    if 'cleaned_data' not in st.session_state:
        st.warning("No cleaned data available for renaming.")
    else:
        cleaned_data = st.session_state['cleaned_data']
        column_names_to_display = [col for col in cleaned_data.columns]  # Placeholder for actual column names

        # Manual input for renaming columns, with special handling for the first and last columns
        new_column_names = []
        for idx, default_name in enumerate(column_names_to_display):
            if idx == 0:
                # First column reserved for "phonenum"
                default_value = "phonenum"
            elif idx == len(column_names_to_display) - 1:
                # Last column reserved for "Set"
                default_value = "Set"
            elif file_parsed:
                # Adjust question numbering to start from column 1, not 0
                question_key = f"Q{idx}"  # Adjusted to match questions starting from 1
                default_value = st.session_state['qa_dict'].get(question_key, {}).get('question', default_name)
            else:
                default_value = default_name

            new_name = st.text_input(f"Column {idx+1}: {default_name}", value=default_value, key=f"new_name_{idx}")
            new_column_names.append(new_name)

        if st.button("Apply New Column Names"):
            updated_df = rename_columns(cleaned_data, new_column_names)
            st.session_state['renamed_data'] = updated_df
            st.write("DataFrame with Renamed Columns:")
            st.dataframe(updated_df.head())

if __name__ == "__main__":
    run1()


