import sanitize.docx as docx
import sanitize.pdf as pdf
import sanitize.txt as txt
import sanitize.csv as csv

def sanitize(uploaded_file):
    file_extension = uploaded_file.name.split(".")[-1].lower()
    
    if file_extension.endswith('docx'):
        docx.sanitize_docx(uploaded_file)
    elif file_extension.endswith('pdf'):
        pdf.sanitize_pdf(uploaded_file)
    elif file_extension.endswith('txt'):
        txt.sanitize_txt(uploaded_file)
    elif file_extension.endswith('csv'):
        csv.sanitize_csv(uploaded_file)
    else:
        print('File format not supported')
        
