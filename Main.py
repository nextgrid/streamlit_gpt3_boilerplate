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

        eng_poets_list = ["Shakespeare", "Seamus Heaney", "Edgar Allan Poe", "William Blake", "Robert Frost", "Emily Dickinson", "Oscar Wilde", "George Bernard Shaw", "William Wordsworth", "Sylvia Plath"]
        
        chi_poets = ["Li He", "Confucius", "Mencius", "LaoTzu"]
        
        chi_styles = ["Airs (风)", "Ode (雅)", "Hymn (颂)"]
        
        jap_poets = ["Matsuo Basho"]
        
        jap_styles = ["haiku", "tanka"]
        
        poetry_forms = ['free verse', 'sonnet', 'acrostic', 'limerick', 'ode', 'solliloquy', 'elegy', 'ballad', 'villanelle']
        
        # available options for poets and nouns
        region_list = ["Asia", "Europe"]

        nouns_list = ["sutd", "university education",
                      "engineering", "STEM", "test", "examinations"]

        with st.sidebar:
            region_option = st.selectbox(
                "Select a region", region_list)

            #  selected region will release the available choices
            if region_option == "Asia":
                poet_option = st.radio("Available Genre", options=[
                    "Haiku", "Syair", "Yadu", "Sijo", "Kural"])  # Japan, Malaysia, Myanmar, Korea, India & Sri Lanka
            elif region_option == "Europe":
                poet_option = st.radio(
                    "Available Genre", options=["Victorian", "Edwardian", "Georgian", "Surrealistic", "Shakespearean"])

            # choices available for nouns
            noun_option = st.multiselect("Available Nouns", nouns_list)
            noun_option

            if st.button("Confirm choices"):  # finalised decision
                # string the list
                filtered = ""
                for noun in noun_option:
                    filtered += f"{noun}, "
                filtered = filtered.strip()
                if len(filtered) > 0:
                    if filtered[-1] == ",":
                        filtered = filtered[:-1]
                    # st.write(filtered) # debug

                st.session_state.textbox = "Write a " + poet_option + \
                    " poem about the benefits of " + filtered

        # for initializing textbox
        st.text_area(
            "Use the example below or input your own text in English",
            key="textbox",
            max_chars=150
        )

        # submit button
        if st.button("Submit"):
            with st.spinner(text="In progress"):
                report_text = process_prompt(st.session_state.textbox)
                st.markdown(report_text)
    else:
        st.error("🔑 Please enter API Key")
