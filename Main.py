import streamlit as st
from model import GeneralModel

def press_poet_button(button_label):
    if st.button(button_label):
        cur_value = st.session_state.textbox 
        st.session_state.textbox = cur_value+ "Write a " + button_label + " poem about the benefits of "
def press_noun_button(button_label):
    if st.button(button_label):
        cur_value = st.session_state.textbox 
        st.session_state.textbox = cur_value + button_label

def app():

    # Creating an object of prediction service
    pred = GeneralModel()

    api_key = st.sidebar.text_input("APIkey", type="password")
    # Using the streamlit cache
    @st.cache
    def process_prompt(inp):
        return pred.model_prediction(input=str(inp).strip() , api_key=api_key)

    if api_key:

        # Setting up the Title
        st.title("Write a poem based on these words")

        poets_list = ["shakespeare", "confucious", "seamus heaney", "edgar allan poe"]
        nouns_list = ["sutd", "university education", "engineering", "STEM", "test"]

        with st.sidebar:
            st.write("all poets")
            for poet in poets_list:
                press_poet_button(poet)
            
            st.write("all nouns/descriptions")
            for noun in nouns_list:
                press_noun_button(noun)

        # st.write("---")
        st.text_area(
            "Use the example below or input your own text in English", 
            key="textbox",
            max_chars=150
        )

        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(st.session_state.textbox )
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
