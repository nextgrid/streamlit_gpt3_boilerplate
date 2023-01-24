import streamlit as st
# from model import GeneralModel

# checks if api key is valid


def valid_api_key(inp: str):
    try:
        st.session_state.pred.model_prediction(
            input="test", api_key=inp)
        return True
    except Exception as e:
        st.error("API Key check failed: " + str(e))
        return False

# updates api kei in session state


def update_api_key(inp: str):
    st.session_state.api_key = inp


def app():

    if st.session_state.api_key:
        col1, col2 = st.columns(2)

        @st.cache
        def process_prompt(inp):
            return st.session_state.pred.model_prediction(input=str(inp).strip(), api_key=st.session_state.api_key)

        with col1:
            # Setting up the Title
            st.title("Write a poem based on these words")

            # available options for poets and nouns
            region_list = ["Asia", "Europe"]

            nouns_list = ["sutd", "university education",
                          "engineering", "STEM", "test", "examinations"]
            eng_poets_list = ["Shakespeare", "Seamus Heaney", "Edgar Allan Poe", "William Blake", "Robert Frost",
                              "Emily Dickinson", "Oscar Wilde", "George Bernard Shaw", "William Wordsworth", "Sylvia Plath"]

            chi_poets = ["Li He", "Confucius", "Mencius", "LaoTzu"]

            chi_styles = ["Airs (风)", "Ode (雅)", "Hymn (颂)"]

            jap_poets = ["Matsuo Basho"]

            jap_styles = ["haiku", "tanka"]

            poetry_forms = ['free verse', 'sonnet', 'acrostic', 'limerick',
                            'ode', 'solliloquy', 'elegy', 'ballad', 'villanelle']

            # available options for poets and nouns
            region_list = ["Asia", "Europe"]

            # with st.sidebar:
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

        with col2:
            st.title("Output appears here")

            # for initializing textbox
            answer = st.text_area(
                "Use the example below or input your own text in English",
                key="textbox",
                max_chars=150
            )

            # submit button
            if st.button("Submit"):
                try:
                    with st.spinner(text="In progress"):
                        report_text = process_prompt(st.session_state.textbox)
                        st.markdown(report_text)
                except Exception as e:
                    st.error("Error: " + str(e))
                    restart = st.button("Re-enter API Key",
                                        on_click=update_api_key(""))
    else:
        with st.form("API_Key_Form"):
            api_key = st.text_input("APIkey", type="password")

            submitted = st.form_submit_button("Submit")
            if submitted:
                if valid_api_key(api_key):
                    update_api_key(api_key)
                    st.experimental_rerun()
        # st.error("🔑 Please enter API Key")
