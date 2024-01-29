import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter
from datetime import datetime
from security_utils import check_password
from PIL import Image


# configure the default settings of the page.
icon = Image.open('./images/invoke_logo.png')
st.set_page_config(
                page_title='IVR Data Cleaner 🧮',
                layout="wide",
                page_icon = icon,
                initial_sidebar_state="expanded"
                )
if check_password():
    # Function to process each uploaded file
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
        total_pickups = len(df_complete)

        df_complete.columns = np.arange(len(df_complete.columns))
        df_complete['Set'] = 'IVR'
        df_complete = df_complete.loc[:, :'Set']
        df_complete = df_complete.loc[(df_complete.iloc[:, 2].str.len() == 10)]

        return df_complete, phonenum_list, total_calls, total_pickups


    # Streamlit File Uploader
    uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

    # Process each file if uploaded
    if uploaded_files:
        all_data = []
        all_phonenum = []
        total_calls_made = 0
        total_pickups = 0
        location_names = []

        for uploaded_file in uploaded_files:
            # Extract location name from file name
            location_name = uploaded_file.name.split('_for_')[1].split(' ')[0]
            location_names.append(location_name)

            df_complete, phonenum_list, total_calls, total_pickups_per_file = process_file(uploaded_file)
            all_data.append(df_complete)
            all_phonenum.append(phonenum_list)
            total_calls_made += total_calls
            total_pickups += total_pickups_per_file

        # Combine all processed data into one DataFrame
        combined_data = pd.concat(all_data, ignore_index=True)
        combined_phonenum = pd.concat(all_phonenum, axis=0)

        # Displaying the results
        st.write(f"Total calls made: {total_calls_made}")
        st.write(f"Total of pick-ups: {total_pickups}")
        st.write(f"Total count of phone numbers that need to be excluded in the next sampling: {combined_phonenum.shape[0]}")

        # Determine the most common location name
        most_common_location, _ = Counter(location_names).most_common(1)[0]

        # Determine the file name for download
        formatted_date = datetime.now().strftime("%Y%m%d")
        output_filename = f'ivr_{most_common_location}_survey2023_used_phonenum_v{formatted_date}.csv'

        # Option to download combined data
        data_as_csv = combined_data.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Processed Data as CSV",
            data=data_as_csv,
            file_name=output_filename,
            mime='text/csv'
        )
