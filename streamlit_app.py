import streamlit as st
import matplotlib.pyplot as plt

def main():
    st.title('Test Matplotlib')

    # Simple plot
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
    ax.set_title('Simple Plot')

    # Display plot
    st.pyplot(fig)

if __name__ == '__main__':
    main()