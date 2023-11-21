import streamlit as st
# from pii_sanitization import sanitize_all
from sanitize.sanitize_docs import sanitize


def main():
    st.title('PII Sanitization Tool for New Zealand Data')
    st.write('Python-based tool that sanitizes Personally Identifiable Information (PII) from user-selected columns within CSV or Excel files. This tool is intended to handle data specific to New Zealand.')

    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv', 'xlsx', 'docx', 'PDF', 'txt'])
    if uploaded_file is not None:
        st.write(uploaded_file.name)
        sanitize(uploaded_file)    
        
if __name__ == '__main__':
    main()
