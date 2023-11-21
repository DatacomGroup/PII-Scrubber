from util.GPT import *
import streamlit as st
import pandas as pd
def sanitize_csv(uploaded_file):
    try:
        df = pd.read_csv(uploaded_file)  # Read the uploaded file  
    except:
        try:
            df = pd.read_csv(uploaded_file, encoding='latin1')
        except:
            try:
                df = pd.read_csv(uploaded_file, encoding='utf-8')
            except:
                try:
                    df = pd.read_csv(uploaded_file, encoding='cp1252')
                except:
                    try:
                        df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')
                    except:
                        st.write('your dataframe is trash try resaving in a new format or something??')
                        return 0
                    
    st.write('dataframe preview')
    st.write(df.head())  # Display the original data

    columns = df.columns
    columns_to_redact = st.multiselect("Select columns to sanitize", columns)
    # df = df.head()
    if st.button('Sanitize Data'):
        for col in columns_to_redact:
            
            
            tmp = df[col].tolist()
            # add text together
            txt = '\n'.join(tmp)
            # st.write(txt ) 
            # redact the text
            redacted_text = redact_with_chatGPT(txt)
            df[col] = redacted_text

        st.write('**Sanitized Data**')
        st.write(df)  # Display the sanitized data
        
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "Press to Download",
            csv,
            "sanitized.csv",
            "text/csv",
            key='download-csv'
        )      
      
    # get all rows from column 'text'
