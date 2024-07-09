import streamlit as st

def main():
    st.title('Basic Streamlit App')

    # Simple text input
    account_key = st.number_input('Enter Account_key', min_value=1)
    details = st.text_input('Enter Details')

    st.write("Account Key:", account_key)
    st.write("Details:", details)

if __name__ == '__main__':
    main()