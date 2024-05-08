import streamlit as st
import pandas as pd
from datetime import datetime
from modules.security_utils import check_password
from modules.data_cleaner_utils_page1 import process_file
from PIL import Image
import numpy as np

st.set_page_config(
    page_title='IVR Data Cleaner 🧮',
    layout="wide",
    page_icon=Image.open('./images/invoke_logo.png'),
    initial_sidebar_state="expanded",
)

def set_dark_mode_css():
    # Define CSS for dark mode with broader coverage
    dark_mode_css = """
    <style>
        html, body, [class*="View"] {
            color: #ffffff !important;  /* Text Color */
            background-color: #111111 !important;  /* Background Color */
        }
        .streamlit-container {
            background-color: #111111 !important;
        }
        .stTextInput > div > div > input {
            color: #ffffff !important;
        }
        /* You can add additional CSS rules here */
    </style>
    """
    # Inject CSS into the Streamlit app
    st.markdown(dark_mode_css, unsafe_allow_html=True)

# Apply the dark mode CSS
set_dark_mode_css()

def run():
    """
    Processes the metrics functions
    """
    if 'processed' not in st.session_state:
        st.session_state['processed'] = False
        st.session_state['total_calls_made'] = 0
        st.session_state['total_pickups'] = 0
        st.session_state['total_CRs'] = 0

    if 'df_merge' not in st.session_state:
        st.session_state['df_merge'] = pd.DataFrame()
        
    if 'phonenum_combined' not in st.session_state:
        st.session_state['phonenum_combined'] = pd.DataFrame()
        
    # Check if data is already processed and available in session state
    if 'processed' not in st.session_state:
        st.session_state['processed'] = False
        st.session_state['all_data'] = []
        st.session_state['all_phonenum'] = []
        st.session_state['total_calls_made'] = 0
        st.session_state['total_pickups'] = 0
        st.session_state['file_count'] = 0

    if check_password():
        st.title('IVR Data Cleaner🏹')
        # Using markdown to create a top heading (H2)
        st.markdown("### Upload IVR Files (.csv format)")

        # Setting up the file uploader widget with the new label
        uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

        # Display the count of uploaded files
        if uploaded_files:
            st.write(f"Number of files uploaded: {len(uploaded_files)}")

        if st.button('Process'):
            with st.spinner("Processing the files..."):
                # Reset counters and lists
                st.session_state['all_data'] = []
                st.session_state['all_phonenum'] = []
                st.session_state['total_calls_made'] = 0
                st.session_state['total_pickups'] = 0
                st.session_state['file_count'] = 0
                st.session_state['processed'] = True

                # Correctly unpack returned values from process_file
                for uploaded_file in uploaded_files:
                    df_complete, phonenum_list, total_calls_made, total_of_pickups, df_merge = process_file(uploaded_file)

                    # Append or aggregate the results as needed
                    st.session_state['all_data'].append(df_complete)
                    st.session_state['all_phonenum'].append(phonenum_list)
                    st.session_state['total_calls_made'] += total_calls_made
                    st.session_state['total_pickups'] += total_of_pickups
                    st.session_state['file_count'] += 1
                    st.session_state['total_CRs'] += len(df_complete)
                     # Aggregate the results
                    st.session_state['df_merge'] = pd.concat([st.session_state['df_merge'], df_complete], ignore_index=True)
                    st.session_state['phonenum_combined'] = pd.concat([st.session_state['phonenum_combined']], ignore_index=True).drop_duplicates()
                    
                # After processing all files:
                # Aggregate df_complete DataFrames
                if st.session_state['all_data']:
                    st.session_state['df_merge'] = pd.concat(st.session_state['all_data'], ignore_index=True)
                else:
                    st.session_state['df_merge'] = pd.DataFrame()

                # Aggregate phonenum_df DataFrames
                if st.session_state['all_phonenum']:
                    st.session_state['phonenum_combined'] = pd.concat(st.session_state['all_phonenum'], ignore_index=True).drop_duplicates()
                else:
                    st.session_state['phonenum_combined'] = pd.DataFrame()
                                
                st.session_state['processed'] = True

        if st.session_state['processed']:
            # Use data from session state
            combined_data = pd.concat(st.session_state['all_data'], axis='index', ignore_index=True)
            combined_phonenum = pd.concat(st.session_state['all_phonenum'], axis=0).drop_duplicates()
            combined_phonenum.rename(columns={'PhoneNo': 'phonenum'}, inplace=True)

            # Save statistics in session state
            st.session_state['total_CRs'] = combined_data.shape[0]
            st.session_state['pick_up_rate_percentage'] = (st.session_state['total_pickups'] / st.session_state['total_calls_made']) * 100 if st.session_state['total_calls_made'] > 0 else 0
            st.session_state['cr_rate_percentage'] = (st.session_state['total_CRs'] / st.session_state['total_pickups']) * 100 if st.session_state['total_pickups'] > 0 else 0
                    
            # Update the placeholder with the new message after processing is complete
            st.success("Files have been processed successfully.✨")
            
            st.markdown("### IVR Campaign Basic Statistics:")
            
            # Organizing your data into a dictionary
            data = {
                "Metric": ["Total calls made", "Total of pick-ups", "Pick-up Rate", "CR Rate"],
                "Value": [
                    f"{st.session_state['total_calls_made']:,}",
                    f"{st.session_state['total_pickups']:,}",
                    # f"{st.session_state['total_CRs']:,}", nnti kene leatk kat Table balik value dia Total CRs
                    f"{st.session_state['pick_up_rate_percentage']:.2f}%",
                    f"{st.session_state['cr_rate_percentage']:.2f}%"
                ]
            }

            # Convert the dictionary to a pandas DataFrame
            df_stats = pd.DataFrame(data)

            # Adjust the DataFrame's index to start from 1 instead of 0
            df_stats.index = df_stats.index + 1

            # Display the DataFrame as a table in Streamlit
            st.table(df_stats)

            # Display a snippet of the cleaned data
            st.markdown("### Cleaned Data Preview:")
            st.dataframe(combined_data.head())  # Show the first 5 rows as a preview

            # Current date for the filename
            formatted_date = datetime.now().strftime("%Y%m%d")

            # Format the default filename
            default_filename = f'IVR_Cleaned_Data_v{formatted_date}.csv'

            # Use the default filename in the text input, allowing the user to edit it
            output_filename = st.text_input("Edit the filename for download", value=default_filename)

            # Check if the output filename ends with '.csv', if not append '.csv'
            if not output_filename.lower().endswith('.csv'):
                output_filename += '.csv'
            
            # After data processing
            st.session_state['cleaned_data'] = combined_data

            # Download button
            data_as_csv = combined_data.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="Download Cleaned Data as CSV",
                data=data_as_csv,
                file_name=output_filename,
                mime='text/csv'
            )
        
            if st.session_state['processed']:
                # Concatenate all phone numbers from processed data
                phonenum_combined = pd.concat(st.session_state['all_phonenum'], axis=0)
                
                # Check and report duplicated numbers before dropping them to correctly report total and duplicated counts
                dup = phonenum_combined.duplicated().sum()
                
                # Drop duplicated numbers for the updated total
                phonenum_combined_cleaned = phonenum_combined.drop_duplicates()

                # Display a preview of these used phone numbers
                st.markdown("### Preview of Phone Numbers to be Excluded in the Next Sampling:")
                st.dataframe(phonenum_combined_cleaned.head())  # Show the first 5 rows as a preview

                # Organizing your data into a dictionary for phone numbers
                phone_data = {
                    "Metric": [
                        "Total count of phone numbers that need to be excluded in the next sampling", 
                        "Total duplicated numbers", 
                        "Total numbers after dropping duplicate numbers"
                    ],
                    "Count": [
                        f"{phonenum_combined.shape[0]}",
                        f"{dup}",
                        f"{phonenum_combined_cleaned.shape[0]}"
                    ]
                }

                # Convert the dictionary to a pandas DataFrame
                df_phone_stats = pd.DataFrame(phone_data)

                # Adjust the DataFrame's index to start from 1 instead of 0
                df_phone_stats.index = df_phone_stats.index + 1

                # Display the DataFrame as a table in Streamlit
                st.table(df_phone_stats)
                
                # Prepare for downloading the used phone numbers
                # Current date for the filename specific to unique phone numbers
                formatted_date = datetime.now().strftime("%Y%m%d")
                default_filename_phonenum = f'IVR_Dialed_Phonenum_v{formatted_date}.csv'
                output_filename_phonenum = st.text_input("Edit the filename for download", value=default_filename_phonenum)

                # Ensure the filename ends with '.csv'
                if not output_filename_phonenum.lower().endswith('.csv'):
                    output_filename_phonenum += '.csv'

                # Convert the unique phone numbers dataframe to CSV for download
                phonenum_data_as_csv = phonenum_combined.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download Dialed Phone Numbers as CSV",
                    data=phonenum_data_as_csv,
                    file_name=output_filename_phonenum,
                    mime='text/csv'
                )

        
            # Add instructions for navigating to the next page
            st.write("To continue to the Questionnaire Definition, please navigate to the 'Questionairre-Definer & Keypresses-Decoder🎉' app.")

        
if __name__ == "__main__":
    run()
#Fz
