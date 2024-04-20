import streamlit as st
from PIL import Image

def set_page_config():
    icon_path = "icons/cakir.png"

    st.set_page_config(
        page_title="Cakirsolutions",
        page_icon=icon_path,
        layout="wide",
        initial_sidebar_state='expanded'
    )
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 





