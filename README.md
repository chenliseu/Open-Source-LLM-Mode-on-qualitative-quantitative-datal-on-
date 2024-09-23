# Free LLM model On Qualitative & Quatitative Data 
This model offers a free open source Large Language model applied on Qualitative & Quatitative Data
* Qualitative Data: Pre-trained google/flan-t5-large model from huggingface along with Meta/FAISS for similarity search. The prompt is applied on files in pdf format
* Quatitative Data: LLM Starcoder Model for code generation from huggingface that is pretained on license data, along with PandasAI to generate plot. The prompt is applied on files in csv format

## Installation
Follow the [installation guide](https://github.com/chenliseu/Open-Source-LLM-on-qualitative-and-quantitative-data/blob/main/Installation_Guide.txt)
* Download and Unzip the files in one folder on laptop
* Install Python: https://www.python.org/downloads/
* Open Command Prompt
* Create virual environment: python -m venv env
* Used CD command to move to folder where all files are unzipped
* Install all packages: pip install -r requirements.txt
* Register and request a free API token from Huggingface: https://huggingface.co/settings/tokens
* Using notepad app, type `HUGGINGFACEHUB_API_TOKEN = "your_API_Token", then save as .env file in your unzip folder with all the source files

## Run the Model 
Run: streamlit run main.py. You shall the see the main page where it can direct you to two pages to apply LLM on Qualitative & Quatitative Data
#### Main Page
<img src="https://github.com/chenliseu/Open-Source-LLM-on-qualitative-and-quantitative-data/raw/main/main.png" alt="Main Page" width="400">
<img src="https://github.com/chenliseu/Open-Source-LLM-on-qualitative-and-quantitative-data/raw/main/model_intro.png" alt="Detailed Model" width="400">
![Main Page](https://github.com/chenliseu/Open-Source-LLM-on-qualitative-and-quantitative-data/blob/main/main.png)
![Detailed Model](https://github.com/chenliseu/Open-Source-LLM-on-qualitative-and-quantitative-data/blob/main/model_intro.png)

# Reference
* [PandasAI Starcoder](https://github.com/Sinaptik-AI/pandas-ai/discussions/60)
* [google/flan-t5-large Model](https://huggingface.co/google/flan-t5-large)
* [Streamlit File Uploader](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader)
