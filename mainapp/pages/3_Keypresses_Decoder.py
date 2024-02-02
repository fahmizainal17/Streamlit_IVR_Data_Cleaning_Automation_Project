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

# import streamlit as st

# def run():
#     st.title('Keypresses Decoder')

#     # Retrieve the renamed data from the session state
#     if 'renamed_data' in st.session_state:
#         renamed_data = st.session_state['renamed_data']
#         st.write("Preview of Renamed Data:")
#         st.dataframe(renamed_data.head())

#         # Perform further processing if necessary
#         # ...

#     else:
#         st.error("No renamed data found. Please go back to the previous step and rename your data first.")

# if __name__ == "__main__":
#     run()

# page3.py

# import streamlit as st
# import pandas as pd

# def apply_mappings_to_dataframe(df, mappings):
#     for col in df.columns:
#         if col in mappings:
#             # Apply the mapping to the column
#             df[col] = df[col].map(mappings[col])
#     return df

# def run():
#     st.title('Keypresses Definer')

#     if 'renamed_data' in st.session_state:
#         # Retrieve the data with renamed columns
#         data = st.session_state['renamed_data']

#         # Dictionary to hold the mappings for each FlowNo_n
#         mappings = {}

#         for col in data.columns:
#             if col.startswith('FlowNo_'):
#                 # Display current column and its unique values to help define mappings
#                 st.write(f"Current column: {col}")
#                 st.write("Unique values in this column:")
#                 st.write(data[col].unique())

#                 # Create input fields for defining mappings
#                 keys = st.text_input(f"Enter keys for {col} separated by comma", key=f'keys_{col}')
#                 values = st.text_input(f"Enter values for {col} separated by comma", key=f'values_{col}')
                
#                 # Splitting the input strings by comma and stripping whitespace
#                 keys_list = [k.strip() for k in keys.split(',') if k]
#                 values_list = [v.strip() for v in values.split(',') if v]

#                 # Ensure keys and values lists are of same length before creating mapping
#                 if len(keys_list) == len(values_list):
#                     col_mappings = dict(zip(keys_list, values_list))
#                     mappings[col] = col_mappings
#                 else:
#                     st.error(f"The number of keys and values for {col} do not match. Please enter matching pairs.")

#         if st.button("Apply Mappings"):
#             # Apply mappings to the DataFrame
#             updated_data = apply_mappings_to_dataframe(data.copy(), mappings)
            
#             # Save the updated data to the session state
#             st.session_state['decoded_data'] = updated_data
            
#             # Display the updated DataFrame
#             st.write("DataFrame with Applied Mappings:")
#             st.dataframe(updated_data.head())
#     else:
#         st.error("No renamed data found. Please go back to the previous step and rename your data first.")

# if __name__ == "__main__":
#     run()

# page3.py

# import streamlit as st
# import pandas as pd

# def run():
#     st.title('Keypresses Decoder')

#     # Retrieve the renamed data from the session state
#     if 'renamed_data' in st.session_state:
#         renamed_data = st.session_state['renamed_data']
#         st.write("Preview of Renamed Data:")
#         st.dataframe(renamed_data.head())

#         # Dictionary to store the mappings
#         keypress_mappings = {}

#         # Generate input fields for each 'FlowNo_' column
#         for col in renamed_data.columns:
#             if col.startswith('FlowNo_'):
#                 st.write(f"Define keypress mappings for {col}:")
#                 # Extract the number part from the column name e.g., 'FlowNo_2' -> 2
#                 number = col.split('_')[-1]
#                 # Create text input for keys
#                 keys_input = st.text_input(f"Enter keys for {col} (comma-separated):", key=f'keys_{number}')
#                 # Create text input for values
#                 values_input = st.text_input(f"Enter values for {col} (comma-separated):", key=f'values_{number}')

#                 # Split the input strings by comma and stripping whitespace
#                 keys = [k.strip() for k in keys_input.split(',') if k]
#                 values = [v.strip() for v in values_input.split(',') if v]
                
#                 # Ensure keys and values lists are of same length before creating mapping
#                 if len(keys) == len(values):
#                     mappings = dict(zip(keys, values))
#                     keypress_mappings[col] = mappings
#                 else:
#                     st.error(f"The number of keys and values for {col} do not match. Please enter matching pairs.")

#         # Button to apply mappings
#         if st.button("Decode Keypresses"):
#             # Apply the mappings to the DataFrame
#             for col, mapping in keypress_mappings.items():
#                 if mapping:  # Check if mapping is not empty
#                     renamed_data[col] = renamed_data[col].map(mapping)
            
#             # Save the updated DataFrame to the session state
#             st.session_state['decoded_data'] = renamed_data
#             st.write("Data with Decoded Keypresses:")
#             st.dataframe(renamed_data.head())

#     else:
#         st.error("No renamed data found. Please go back to the previous step and rename your data first.")

# if __name__ == "__main__":
#     run()


# page3.py

import streamlit as st
import pandas as pd

def run():
    st.title('Keypresses Decoder')

    # Check if the data with renamed columns exists in the session state
    if 'renamed_data' in st.session_state:
        renamed_data = st.session_state['renamed_data']
        st.write("Preview of Renamed Data:")
        st.dataframe(renamed_data.head())

        # A dictionary to hold the mappings for each keypress
        keypress_mappings = {}

        # Iterate through each column in the DataFrame
        for col in renamed_data.columns:
            # Display the question (column name)
            st.subheader(f"Question: {col}")
            # Get unique keypress values for the current column
            unique_values = renamed_data[col].unique()
            # Create a container to hold the text inputs
            container = st.container()
            all_mappings = {}
            # Iterate over unique values and create a text input for each
            for val in unique_values:
                if pd.notna(val):  # Skip NaN values
                    # The user can define the mapping for each keypress value
                    readable_val = container.text_input(f"Rename '{val}' to:", value="", key=f"{col}_{val}")
                    if readable_val:  # Only add non-empty mappings
                        all_mappings[val] = readable_val
            if all_mappings:
                keypress_mappings[col] = all_mappings

        if st.button("Decode Keypresses"):
            # Apply the mappings to the DataFrame
            for col, col_mappings in keypress_mappings.items():
                renamed_data[col] = renamed_data[col].map(col_mappings).fillna(renamed_data[col])

            # Save the updated DataFrame to the session state
            st.session_state['decoded_data'] = renamed_data

            # Display the updated DataFrame
            st.write("Data with Decoded Keypresses:")
            st.dataframe(renamed_data.head())

            # Display the answer proportions for each question
            for col in renamed_data.columns:
                st.write(f"Answer Proportions for {col}:")
                proportions = renamed_data[col].value_counts(normalize=True)
                st.bar_chart(proportions)

    else:
        st.error("No renamed data found. Please go back to the previous step and rename your data first.")

if __name__ == "__main__":
    run()
