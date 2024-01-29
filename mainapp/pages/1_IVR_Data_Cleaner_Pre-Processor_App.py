import streamlit as st
import pandas as pd
from datetime import datetime
from security_utils import check_password  # Assuming this is a custom module
from PIL import Image
import numpy as np

# Configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
    page_title='IVR Data Cleaner 🧮',
    layout="wide",
    page_icon=icon,
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
    all_data = []  # List to store DataFrames from each file for final display
    all_phonenum = []  # List to store phone numbers from each file for final display
    file_count = 0  # Counter for the number of files processed

    def process_file(uploaded_file):
        df = pd.read_csv(uploaded_file, skiprows=1, names=range(24), engine='python')
        df.dropna(axis='columns', how='all', inplace=True)
        df.columns = df.iloc[0]
        df_phonenum = df[['PhoneNo']]
        df_response = df.loc[:, 'UserKeyPress':]
        df_results = pd.concat([df_phonenum, df_response], axis='columns')
        
        total_calls = len(df_results)
        phonenum_recycle = df_results.dropna(subset=['UserKeyPress'])
        phonenum_list = phonenum_recycle[['PhoneNo']]
        
        df_complete = df_results.dropna(axis='index')
        total_pickup = len(df_complete)

        # Additional processing steps
        df_complete.columns = np.arange(len(df_complete.columns))
        df_complete['Set'] = 'IVR'
        df_complete = df_complete.loc[:, :'Set']
        df_complete = df_complete.loc[(df_complete.iloc[:, 2].str.len() == 10)]

        return df_complete, phonenum_list, total_calls, total_pickup

    uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

    if uploaded_files:
        total_calls_made = 0
        total_pickups = 0

        for uploaded_file in uploaded_files:
            df_complete, phonenum_list, total_calls, total_pickup = process_file(uploaded_file)
            all_data.append(df_complete)
            all_phonenum.append(phonenum_list)
            total_calls_made += total_calls
            total_pickups += total_pickup
            file_count += 1

        # Final concatenation
        combined_data = pd.concat(all_data, axis='index', ignore_index=True)
        combined_phonenum = pd.concat(all_phonenum, axis=0).drop_duplicates()
        combined_phonenum.rename(columns={'PhoneNo': 'phonenum'}, inplace=True)

        default_location = 'PETALING JAYA'
        survey_name = st.text_input("Edit the name of the eg. State, District, DUN that you study", value=default_location)
        
        combined_data = pd.concat(all_data, ignore_index=True)
        combined_phonenum = pd.concat(all_phonenum, axis=0).drop_duplicates()
        combined_phonenum.rename(columns={'PhoneNo': 'phonenum'}, inplace=True)
        
        total_CRs = combined_data.shape[0]
        pick_up_rate = total_pickups / total_calls_made if total_calls_made > 0 else 0
        cr_rate = total_CRs / total_pickups if total_pickups > 0 else 0
        
        st.write(f"Total calls made: {total_calls_made}")
        st.write(f"Total of pick-ups: {total_pickups}")
        st.write(f"Total CRs: {total_CRs}")
        st.write(f"Pick-up Rate: {pick_up_rate:.2f}")
        st.write(f"CR Rate: {cr_rate:.2f}")
        st.write(f"Total count of phone numbers that need to be excluded in the next sampling: {combined_phonenum.shape[0]}")
        st.write(f"Total files processed: {file_count}")

        formatted_date = datetime.now().strftime("%Y%m%d")
        output_filename = f'ivr_{survey_name}_survey2023_used_phonenum_v{formatted_date}.csv'

        data_as_csv = combined_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Processed Data as CSV",
            data=data_as_csv,
            file_name=output_filename,
            mime='text/csv'
        )
