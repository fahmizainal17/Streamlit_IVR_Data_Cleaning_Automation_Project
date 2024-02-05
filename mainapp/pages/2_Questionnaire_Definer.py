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

# def run():
#     st.title('Questionnaire Definer & Keypresses Decoder')

#     if 'cleaned_data' in st.session_state:
#         cleaned_data = st.session_state['cleaned_data']
#         st.write("Preview of Cleaned Data:")
#         st.dataframe(cleaned_data.head())
#     else:
#         st.error("No cleaned data found. Please go back to Page 1 and process your data first.")

# if __name__ == "__main__":
#     run()

# # 2
# # Function to rename columns based on user input
# def rename_columns(df, new_column_names):
#     mapping = {old: new for old, new in zip(df.columns, new_column_names) if new}  # Create a mapping only for non-empty entries
#     return df.rename(columns=mapping, inplace=False)

# def run():
#     st.title('Questionnaire Definer & Keypresses Decoder')

#     if 'cleaned_data' in st.session_state:
#         cleaned_data = st.session_state['cleaned_data']
#         st.write("Preview of Cleaned Data:")
#         st.dataframe(cleaned_data.head())

#         # Input fields for new column names
#         st.subheader("Rename Columns")
#         new_column_names = []
#         for idx, col in enumerate(cleaned_data.columns):
#             new_col_name = st.text_input(f"Q{idx+1}: Rename '{col}' to:", key=f"new_name_{idx}")
#             new_column_names.append(new_col_name)
        
#         # Rename Button
#         if st.button("Rename Columns"):
#             # Rename the DataFrame columns
#             updated_df = rename_columns(cleaned_data, new_column_names)
#             st.session_state['cleaned_data'] = updated_df  # Update the session state with the renamed DataFrame
            
#             # Display updated DataFrame
#             st.write("Updated DataFrame:")
#             st.dataframe(updated_df.head())
#     else:
#         st.error("No cleaned data found. Please go back to Page 1 and process your data first.")

# if __name__ == "__main__":
#     run()



# # Function to rename columns based on user input
# def rename_columns(df, new_column_names):
#     mapping = {old: new for old, new in zip(df.columns, new_column_names) if new}  # Create a mapping only for non-empty entries
#     return df.rename(columns=mapping, inplace=False)

# def run():
#     st.title('Questionnaire Definer')

#     if 'cleaned_data' in st.session_state:
#         cleaned_data = st.session_state['cleaned_data']
#         st.write("Preview of Cleaned Data:")
#         st.dataframe(cleaned_data.head())

#         # Create a two-column layout
#         col1, col2 = st.columns(2)

#         with col1:
#             st.write("Rename Columns:")
#             new_column_names = []
#             for idx, col in enumerate(cleaned_data.columns):
#                 new_col_name = st.text_input(f"Q{idx+1}:", value=col, key=f"new_name_{idx}")
#                 new_column_names.append(new_col_name)

#         with col2:
#             st.write(" ")  # Just to align with the left column
#             st.write(" ")  # Adding extra space for alignment

#         if st.button("Apply New Column Names"):
#             updated_df = rename_columns(cleaned_data, new_column_names)
#             st.session_state['cleaned_data'] = updated_df  # Update the session state with the renamed DataFrame

#             st.write("DataFrame with Renamed Columns:")
#             st.dataframe(updated_df.head())

#     else:
#         st.error("No cleaned data found. Please go back to the previous step and process your data first.")

# if __name__ == "__main__":
#     run()


# page2.py

import streamlit as st

# Function to rename columns based on user input
def rename_columns(df, new_column_names):
    mapping = {old: new for old, new in zip(df.columns, new_column_names) if new}
    return df.rename(columns=mapping, inplace=False)

def run():
    st.title('Questionnaire Definer')

    if 'cleaned_data' in st.session_state:
        cleaned_data = st.session_state['cleaned_data']
        st.write("Preview of Cleaned Data:")
        st.dataframe(cleaned_data.head())

        # Create a two-column layout
        col1, col2 = st.columns(2)

        with col1:
            st.write("Rename Columns:")
            new_column_names = [st.text_input(f"Q{idx+1}:", value=col, key=f"new_name_{idx}") for idx, col in enumerate(cleaned_data.columns)]

        with col2:
            st.write(" ")  # Just to align with the left column

        if st.button("Apply New Column Names"):
            updated_df = rename_columns(cleaned_data, new_column_names)
            st.session_state['renamed_data'] = updated_df  # Save the DataFrame with renamed columns

            st.write("DataFrame with Renamed Columns:")
            st.dataframe(updated_df.head())

    else:
        st.error("No cleaned data found. Please go back to the previous step and process your data first.")

if __name__ == "__main__":
    run()
