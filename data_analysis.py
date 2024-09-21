# Import all libraries
from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
import matplotlib.pyplot as plt
from pandasai.llm.starcoder import Starcoder

def main():

    st.title('Automated Data Analysis with AI')

    # Load Huggingface API key
    load_dotenv()
    API_KEY = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    if not API_KEY:
        st.error("HuggingFace API key not found. Please set it in the environment variables.")
        return 

    # Use LLM Starcoder Model from huggingface that is trained on liceensed data
    Model = Starcoder(api_token=API_KEY)

    # Load Pandas AI model compatible with LLM Model
    PandasAI_Model = PandasAI(Model)

    # Load data file
    Doc = st.file_uploader('Upload the CSV file', type=['csv'])
   
    if Doc is not None:
        df = pd.read_csv(Doc)
        st.write(df.head(5))

        Question = st.text_input('Ask your question here')

        if st.button('Analyze'):
            if Question:
                with st.spinner("Analyzing the results..."):
                    try:
                        Result = PandasAI_Model.run(df, prompt=Question)
                        if isinstance(Result, plt.Axes):
                            fig = Result.figure
                            st.pyplot(fig)
                        else:
                            st.write(Result)
                    except Exception as e:
                        st.error(f"An error occurred: {e}")
            else:
                st.warning("Please ask your question.")
    else:
        st.info("Please upload a CSV file to proceed.")

if __name__ == '__main__':
    main()
