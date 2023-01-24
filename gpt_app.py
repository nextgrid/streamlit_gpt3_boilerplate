import Main
import streamlit as st
from model import GeneralModel

st.set_page_config(page_title="GPT-3 Boilerplate", page_icon=":shark:", layout="wide")
if "api_key" not in st.session_state:
  st.session_state['api_key'] = ""
if "pred" not in st.session_state:
  st.session_state['pred'] = GeneralModel()
st.set_page_config(page_title="Write a Poem: OH23", page_icon=":shark:", layout="wide")

Main.app()

# streamlit run gpt_app.py on cli