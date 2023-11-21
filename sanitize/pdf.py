from util.GPT import find_sensitive_data, new_file_path 
import re
import fitz  # PyMuPDF
import streamlit as st

def get_sensitive_words(pdf_doc):
    full_text = []
    for page_num in range(pdf_doc.page_count):
        page = pdf_doc.load_page(page_num)
        full_text.append(page.get_text("text"))

    highlighted = find_sensitive_data('\n'.join(full_text))

    return highlighted

def sanitize_pdf(uploaded_file):
    import json
    pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    words = get_sensitive_words(pdf_document)
    # Remove newline characters and extra spaces
    single_line_json = words.replace('\n', '').replace('  ', '')
    json_NEW = json.loads(single_line_json)
    word_identified = []
    for key in json_NEW:
        if json_NEW[key] != "N/A":
        
            for string in json_NEW[key]:
                word_identified.append(string)
          
    st.write(word_identified)           
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        for word in word_identified:
            annotations = page.search_for(word)
            for annot in annotations:
                rect = annot  # The annotation object itself represents the rectangle
                # Annotating the word with a redaction block
                page.add_redact_annot(rect)

        page.apply_redactions()  # Apply redactions to the page

 
    new_filename = new_file_path(uploaded_file.name)
    
    # download the new pdf file
    st.download_button(label="Download Redacted File", data=pdf_document.write(), file_name=new_filename)
    
        


