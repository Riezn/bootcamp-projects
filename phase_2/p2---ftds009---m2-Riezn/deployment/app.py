import streamlit as st
from PIL import Image
import base64
from tensorflow.keras.models import load_model

#read page icon file
im = Image.open('icon.png')


#Page Config
st.set_page_config(
    page_title="COVID-19 Tweet Sentiment Checker",
    page_icon=im,
    # layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Riezn',
        'Report a bug': None,
        'About': 'Predict our customer retention by Judan Syamsul Hadad - FTDS-009 https://github.com/Riezn'
    }
)

#set background
def set_bg_hack(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
set_bg_hack('background.png')

#modify sidebar
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 500px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 500px;
        margin-left: -500px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

#sidebar
st.sidebar.markdown('''
    # <center>COVID-19 Tweet Sentiment Checker</center>
    ''',unsafe_allow_html=True)
tweet = st.sidebar.text_area(
    # label = '',
    max_chars = 280,
    label = 'Type your sample tweet here to check the sentiment'
)

#prediction
pred = st.sidebar.button("Predict")

saved_model = load_model('tensormodel')
sentiment = {0: 'negative', 1: 'neutral', 2: 'positive'}

if pred==True:
    response = sentiment[(saved_model.predict([tweet]).argmax(axis=1))[0]]
    st.sidebar.write('The above tweet is a ', '*{}*'.format(response), ' tweet')