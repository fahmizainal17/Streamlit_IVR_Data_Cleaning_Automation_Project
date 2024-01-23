import streamlit as st
import pandas as pd
import numpy as np
import io

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

    for uploaded_file in uploaded_files:
        df_complete, phonenum_list, total_calls, total_pickups_per_file = process_file(uploaded_file)
        all_data.append(df_complete)
        all_phonenum.append(phonenum_list)
        total_calls_made += total_calls
        total_pickups += total_pickups_per_file

    # Calculate Pick-up Rate
    if total_calls_made > 0:
        pickup_rate = total_pickups / total_calls_made
    else:
        pickup_rate = 0

    # Combine and display results
    combined_data = pd.concat(all_data, axis=0)
    combined_phonenum = pd.concat(all_phonenum, axis=0)

    st.write(f"Total calls made: {total_calls_made}")
    st.write(f"Total of pick-ups: {total_pickups}")
    st.write(f"Pick-up Rate: {pickup_rate:.2%}")  # Display as a percentage
    st.write(f"Total count of phone numbers that need to be excluded in the next sampling: {combined_phonenum.shape[0]}")

    # Option to download combined data
    data_as_csv = combined_data.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Processed Data as CSV",
        data=data_as_csv,
        file_name='processed_data.csv',
        mime='text/csv'
    )
