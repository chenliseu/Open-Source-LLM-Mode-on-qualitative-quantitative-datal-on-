# Import all libraries
from dotenv import load_dotenv
import os
import streamlit as st
from PyPDF2 import PdfReader
from PIL import Image
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

# Function to initialize or retrieve the history from session state
def get_or_init_history():
    if 'history' not in st.session_state:
        st.session_state.history = []
    return st.session_state.history

def main():

    # Load Huggingface API
    load_dotenv()
    st.title("Apply GenAI on your File")

    pdf = st.file_uploader("Insert your file", type="pdf")

    if pdf is not None:
        # save all pdf text into a character
        pdf_reader = PdfReader(pdf)
        content = ""
        for page in pdf_reader.pages:
            content += page.extract_text()

        # Splitting text that looks at characters.
        text_splitter = CharacterTextSplitter(separator="\n")
        splited_text = text_splitter.split_text(content)

        # Create embedding using huggingface API to convert text into vectors
        Huggingface_embeddings = HuggingFaceEmbeddings()

        # Conduct similarity search and clustering of dense vectors
        Similarity_Search = FAISS.from_texts(splited_text, Huggingface_embeddings)

        # Save all the past questions & answers
        history = get_or_init_history()
        request = st.text_input("Ask your question here")

        if request:
            # Perform similarity search in the knowledge base
            Result = Similarity_Search.similarity_search(request)

            # Load Question Answering chain using HuggingFace model, max_length controls the answers length
            Model = HuggingFaceHub(repo_id="google/flan-t5-large", model_kwargs={"max_length": 200})

            # Loads a chai to do QA on documents,
            QA = load_qa_chain(Model, chain_type="stuff")
            Answer = QA.run(input_documents=Result, question=request)

            # Append question and response to history
            history.append({"question": request, "answer": Answer})

            # Display the current question and answer
            st.write(Answer)

            # Display the history of questions and answers
            st.subheader("History")
            for idx, entry in enumerate(history):
                st.write(f"**Question {idx + 1}:** {entry['question']}")
                st.write(f"**Answer {idx + 1}:** {entry['answer']}")
                st.write("---")

        # Store updated history back to session state
        st.session_state.history = history

if __name__ == '__main__':
    main()
