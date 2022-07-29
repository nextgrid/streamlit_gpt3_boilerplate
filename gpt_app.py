import Main
import streamlit as st

st.set_page_config(page_title="Social Media Helper", page_icon=":shark:", layout="wide", menu_items={
         'Report a bug': "https://github.com/nextgrid/Social-MediaHelper_gpt3/issues",
         'About': "## This is a social media post generator, made by NewNative https://github.com/nextgrid/Social-MediaHelper_gpt3"
     })

Main.app()
