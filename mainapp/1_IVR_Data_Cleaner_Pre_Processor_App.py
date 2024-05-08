# import streamlit as st
# import pandas as pd
# from datetime import datetime
# from modules.security_utils import check_password
# from PIL import Image
# import numpy as np

# def run():
#     # Configure the default settings of the page.
#     icon = Image.open('./images/invoke_logo.png')
#     st.set_page_config(
#         page_title='IVR Data Cleaner 🧮',
#         layout="wide",
#         page_icon=icon,
#         initial_sidebar_state="expanded"
#     )

#     def set_dark_mode_css():
#         # Define CSS for dark mode
#         dark_mode_css = """
#         <style>
#             html, body, [class*="View"] {
#                 color: #ffffff;  /* Text Color */
#                 background-color: #111111;  /* Background Color */
#             }
#             .stTextInput > div > div > input {
#                 color: #ffffff;
#                 background-color: #111111;
#             }
#             .stCheckbox > label {
#                 color: #ffffff;
#             }
#             /* Add other widget-specific styles here */
#         </style>
#         """
#         # Inject CSS into the Streamlit app
#         st.markdown(dark_mode_css, unsafe_allow_html=True)

#     # Apply the dark mode CSS
#     set_dark_mode_css()

#     if 'data' not in st.session_state:
#         st.session_state['data'] = None  # Initialize the session state

#     all_data = []  # List to store DataFrames from each file for final display
#     all_phonenum = []  # List to store phone numbers from each file for final display
#     file_count = 0  # Counter for the number of files processed

#     def process_file(uploaded_file):
#         df = pd.read_csv(uploaded_file, skiprows=1, names=range(24), engine='python')
#         df.dropna(axis='columns', how='all', inplace=True)
#         df.columns = df.iloc[0]
#         df_phonenum = df[['PhoneNo']]
#         df_response = df.loc[:, 'UserKeyPress':]
#         df_results = pd.concat([df_phonenum, df_response], axis='columns')
        
#         total_calls = len(df_results)
#         phonenum_recycle = df_results.dropna(subset=['UserKeyPress'])
#         phonenum_list = phonenum_recycle[['PhoneNo']]
        
#         df_complete = df_results.dropna(axis='index')
#         total_pickup = len(df_complete)

#         # Additional processing steps
#         df_complete.columns = np.arange(len(df_complete.columns))
#         df_complete['Set'] = 'IVR'
#         df_complete = df_complete.loc[:, :'Set']
#         df_complete = df_complete.loc[(df_complete.iloc[:, 2].str.len() == 10)]

#         return df_complete, phonenum_list, total_calls, total_pickup

#     if check_password():
#         # Using markdown to create a top heading (H2)
#         st.markdown("## Upload IVR Files (.csv format)")

#         # Setting up the file uploader widget with the new label
#         uploaded_files = st.file_uploader("Choose CSV files", accept_multiple_files=True)

#         # Display the count of uploaded files
#         if uploaded_files:
#             st.write(f"Number of files uploaded: {len(uploaded_files)}")
            
#             # Create a 'Process' button
#             if st.button('Process'):
#                 with st.spinner("Processing the files..."):
#                     total_calls_made = 0
#                     total_pickups = 0

#                     for uploaded_file in uploaded_files:
#                         df_complete, phonenum_list, total_calls, total_pickup = process_file(uploaded_file)
#                         all_data.append(df_complete)
#                         all_phonenum.append(phonenum_list)
#                         total_calls_made += total_calls
#                         total_pickups += total_pickup
#                         file_count += 1

#                 # Final concatenation
#                 combined_data = pd.concat(all_data, axis='index', ignore_index=True)
#                 combined_phonenum = pd.concat(all_phonenum, axis=0).drop_duplicates()
#                 combined_phonenum.rename(columns={'PhoneNo': 'phonenum'}, inplace=True)
                
#                 total_CRs = combined_data.shape[0]
#                 pick_up_rate_percentage = (total_pickups / total_calls_made) * 100 if total_calls_made > 0 else 0
#                 cr_rate_percentage = (total_CRs / total_pickups) * 100 if total_pickups > 0 else 0
                
#                 # Update the placeholder with the new message after processing is complete
#                 st.success("Files have been processed successfully.✨")
                
#                 st.markdown("## **IVR Campaign Basic Statistics:**")
#                 st.write(f"Total calls made: {total_calls_made:,}")
#                 st.write(f"Total of pick-ups: {total_pickups:,}")
#                 st.write(f"Total CRs: {total_CRs:,}")
#                 st.write(f"Pick-up Rate: {pick_up_rate_percentage:.2f}%")
#                 st.write(f"CR Rate: {cr_rate_percentage:.2f}%")

#                 # Display a snippet of the cleaned data
#                 st.markdown("## Cleaned Data Preview:")
#                 st.dataframe(combined_data.head())  # Show the first 5 rows as a preview#

#                 # Current date for the filename
#                 formatted_date = datetime.now().strftime("%Y%m%d")

#                 # Format the default filename
#                 default_filename = f'IVR_Petaling_Jaya_Survey2023_Used_Phonenum_v{formatted_date}.csv'

#                 # Use the default filename in the text input, allowing the user to edit it
#                 output_filename = st.text_input("Edit the filename for download", value=default_filename)

#                 # Check if the output filename ends with '.csv', if not append '.csv'
#                 if not output_filename.lower().endswith('.csv'):
#                     output_filename += '.csv'
                
#                 # After data processing
#                 st.session_state['cleaned_data'] = combined_data

#                 # Download button
#                 data_as_csv = combined_data.to_csv(index=False).encode('utf-8')
#                 st.download_button(
#                     label="Download Cleaned Data as CSV",
#                     data=data_as_csv,
#                     file_name=output_filename,
#                     mime='text/csv'
#                 )

#                 # Add instructions for navigating to the next page
#                 st.write("To continue to the Questionnaire Definition, please navigate to the 'Questionairre-Definer_Keypresses-Decoder' app.")
# if __name__ == "__main__":
#    run()



import streamlit as st
import pandas as pd
from datetime import datetime
from modules.security_utils import check_password  # Assuming this is a custom module
from PIL import Image
import numpy as np
print("🧹 🏹 🎥")
def run():
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

    # Apply the dark mode CSS
    set_dark_mode_css()


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

def run():
    # Check if data is already processed and available in session state
    if 'processed' not in st.session_state:
        st.session_state['processed'] = False
        st.session_state['all_data'] = []
        st.session_state['all_phonenum'] = []
        st.session_state['total_calls_made'] = 0
        st.session_state['total_pickups'] = 0
        st.session_state['file_count'] = 0

    if check_password():
        # Using markdown to create a top heading (H2)
        st.markdown("## Upload IVR Files (.csv format)")

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

                # Process files and update session state
                for uploaded_file in uploaded_files:
                    df_complete, phonenum_list, total_calls, total_pickup = process_file(uploaded_file)
                    st.session_state['all_data'].append(df_complete)
                    st.session_state['all_phonenum'].append(phonenum_list)
                    st.session_state['total_calls_made'] += total_calls
                    st.session_state['total_pickups'] += total_pickup
                    st.session_state['file_count'] += 1

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
            
            st.markdown("## **IVR Campaign Basic Statistics:**")
            st.write(f"Total calls made: {st.session_state['total_calls_made']:,}")
            st.write(f"Total of pick-ups: {st.session_state['total_pickups']:,}")
            st.write(f"Total CRs: {st.session_state['total_CRs']:,}")
            st.write(f"Pick-up Rate: {st.session_state['pick_up_rate_percentage']:.2f}%")
            st.write(f"CR Rate: {st.session_state['cr_rate_percentage']:.2f}%")

            # Display a snippet of the cleaned data
            st.markdown("## Cleaned Data Preview:")
            st.dataframe(combined_data.head())  # Show the first 5 rows as a preview

            # Current date for the filename
            formatted_date = datetime.now().strftime("%Y%m%d")

            # Format the default filename
            default_filename = f'IVR_Petaling_Jaya_Survey2023_Used_Phonenum_v{formatted_date}.csv'

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

            # Add instructions for navigating to the next page
            st.write("To continue to the Questionnaire Definition, please navigate to the 'Questionairre-Definer_Keypresses-Decoder' app.")
    
        # ... [Rest of your code] ...

if __name__ == "__main__":
    run()
