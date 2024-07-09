import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the Excel file
@st.cache
def load_data(file_path):
    return pd.read_excel(file_path, sheet_name='GL')

# Calculate the IQR for each Account_key's Details corresponding 'Amount'
def calculate_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    return IQR, Q1, Q3

# Function to identify outliers using IQR
def identify_outliers(data, Q1, Q3, IQR):
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = data[(data < lower_bound) | (data > upper_bound)]
    return outliers

# Function to display outliers summary
def display_outliers_summary(gl_data, account_key, details):
    filtered_data = gl_data[(gl_data['Account_key'] == account_key) & (gl_data['Details'] == details)]
    if filtered_data.empty:
        st.write(f"No data found for Account_key: {account_key} and Details: {details}")
        return

    amount_data = filtered_data['Amount']
    IQR, Q1, Q3 = calculate_iqr(amount_data)
    outliers = identify_outliers(amount_data, Q1, Q3, IQR)

    summary = pd.DataFrame({
        'Account_key': [account_key],
        'Details': [details],
        'Total Data Points': [len(amount_data)],
        'Number of Outliers': [len(outliers)]
    })

    st.write(summary)

# Function to show boxplot
def show_boxplot(gl_data, account_key, details):
    filtered_data = gl_data[(gl_data['Account_key'] == account_key) & (gl_data['Details'] == details)]
    if filtered_data.empty:
        st.write(f"No data found for Account_key: {account_key} and Details: {details}")
        return

    plt.figure(figsize=(10, 6))
    plt.boxplot(filtered_data['Amount'], vert=False)
    plt.title(f'Boxplot for Account_key: {account_key} and Details: {details}')
    plt.xlabel('Amount')
    st.pyplot(plt)

# Main Streamlit app
def main():
    st.title('GL Data Analysis')
    
    # File upload
    uploaded_file = st.file_uploader("Choose an Excel file", type="xlsx")
    if uploaded_file is not None:
        gl_data = load_data(uploaded_file)

        account_key = st.number_input('Enter Account_key', min_value=1)
        details = st.text_input('Enter Details')

        if st.button('Show Outliers Summary'):
            display_outliers_summary(gl_data, account_key, details)
        
        if st.button('Show Boxplot'):
            show_boxplot(gl_data, account_key, details)

if __name__ == '__main__':
    main()