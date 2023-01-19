import streamlit as st
from model import GeneralModel


def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache

    @st.cache
    def process_prompt(inp):
        return pred.model_prediction(input=str(inp).strip(), api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Write a poem based on these words")

        poets_list = [" ", "shakespeare", "confucious",
                      "seamus heaney", "edgar allan poe"]
        nouns_list = ["sutd", "university education",
                      "engineering", "STEM", "test", "examinations"]

        # st.write("---")
        # st.text_area(
        #     "Use the example below or input your own text in English",
        #     key="textbox",
        #     max_chars=150
        # )

        with st.sidebar:
            poet_option = st.selectbox(
                "Available Poets", poets_list)
            noun_option = st.multiselect("Available Nouns", nouns_list)
            poet_option
            noun_option

            if st.button("Confirm choices"):
                # cur_value = st.session_state.textbox
                selected = str(noun_option)
                filtered = selected.replace("'", "")
                filtered = filtered.replace("[", "")
                filtered = filtered.replace("]", "")

                st.session_state.textbox = "Write a " + poet_option + \
                    " poem about the benefits of " + filtered

        # st.write("---")
        st.text_area(
            "Use the example below or input your own text in English",
            key="textbox",
            max_chars=150
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(st.session_state.textbox)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
