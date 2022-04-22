import streamlit as st
import dataviz, hypotest, home
from PIL import Image

#read page icon file
im = Image.open('analytic-icon-11438.png')

#Page Config
st.set_page_config(
    page_title="Supermarket Data Visualization & Hypothesis Testing Dashboard",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Riezn',
        'Report a bug': None,
        'About': 'Data Viz & Hypothesis Testing Dashboard by Judan Syamsul Hadad - FTDS-009 https://github.com/Riezn'
    }
)

#sidebar navigation
st.sidebar.title('Site Navigation')
selection = st.sidebar.selectbox("Please select a page to view", ["Home","Data Visualization", "Hypothesis Testing"])

if selection == "Home":
    home.app()
elif selection == "Data Visualization":
    dataviz.app()
else:
    hypotest.app()