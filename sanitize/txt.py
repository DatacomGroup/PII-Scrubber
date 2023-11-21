from util.GPT import *
import streamlit as st

def sanitize_txt(filename):
    txt_file = filename.read().decode('utf-8')
    # read dara as string
    txt_file = str(txt_file)
    new_txt = redact_with_chatGPT(txt_file)
    # save the new txt file
    new_filename = new_file_path(filename.name)
    st.download_button(label="Download Redacted File", data=new_txt, file_name=new_filename)