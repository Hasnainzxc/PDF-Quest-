import streamlit as st
from dotenv import load_dotenv

def main ():
    load_dotenv
    st.set_page_config(page_title="Chat with multiple Pdf's", page_icon=":books:")


st.header("Chat With Multiple PDF'S :books:")
st.text_input("Ask a Question about your Documents:")


with st.sidebar:
    st.subheader("Your Documents")
    st.file_uploader("upload your PDFs here and click on 'Process'")
    st.button("process")
    
    if __name__ == '__main__':
        main()