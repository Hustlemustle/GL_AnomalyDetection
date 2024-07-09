
import pandas as pd
import streamlit as st

# Load the Excel file
@st.cache_data
def load_data(file_path):
    return pd.read_excel(file_path, sheet_name='GL')

def main():
    st.title('GL Data Analysis')

    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    if uploaded_file is not None:
        gl_data = load_data(uploaded_file)

        account_key = st.number_input('Enter Account_key', min_value=1)
        details = st.text_input('Enter Details')

        st.write("Account Key:", account_key)
        st.write("Details:", details)

if __name__ == '__main__':
    main()