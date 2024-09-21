import streamlit as st
from PIL import Image

def main():
    st.title("GenAI Model")
    image = Image.open('GenAI copy.jpg')
    st.image(image, width=50)

    st.write("Welcome to the my test site. I would like to apply....")

    st.markdown("[GenAI on my PDF file](?page=GenAI)")
    st.markdown("[Data Analysis on my CSV file](?page=data_analysis)")


if __name__ == '__main__':
    params = st.experimental_get_query_params()
    page = params.get("page", ["main"])[0]

    if page == "data_analysis":
        import data_analysis
        data_analysis.main()
    elif page == "GenAI":
        import GenAI
        GenAI.main()
    else:
        main()
