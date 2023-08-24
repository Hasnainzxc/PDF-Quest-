import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS



def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    
    chunks = text_splitter.split_text(raw_text)  # Use 'raw_text' as the input text
    
    return chunks   

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore
    

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple Pdf's", page_icon=":books:")

    st.header("Chat With Multiple PDF'S :books:")
    st.text_input("Ask a Question about your Documents:")

    with st.sidebar:
        st.subheader("Your Documents")
        pdf_docs = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get the pdf text
                raw_text = get_pdf_text(pdf_docs)
                
                
                # st.write(raw_text)
                # Get the text chunks
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)
                
                
                # Create vector store
                
                vectorstore = get_vectorstore(text_chunks)

if __name__ == '__main__':
    main()
