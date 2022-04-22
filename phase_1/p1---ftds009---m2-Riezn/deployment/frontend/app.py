import streamlit as st
import requests
from PIL import Image

#read page icon file
im = Image.open('analytic-icon-11438.png')

#Page Config
st.set_page_config(
    page_title="Health Insurance Prediction",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Riezn',
        'Report a bug': None,
        'About': 'Predict your health insurance fee by Judan Syamsul Hadad - FTDS-009 https://github.com/Riezn'
    }
)

image = Image.open('healthimg.jpg')

st.markdown('''
    # <center>Health Insurance Prediction</center>
    #### <center>Your Health, Our Future</center>
    ''',unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image(image, use_column_width=True)
    st.markdown('''
    <center>Please answer the following questions to predict your insurance fee.</center>
    ''',unsafe_allow_html=True)

left, right = st.columns(2)
with left:
    age = st.number_input("How old are you?", min_value=18, max_value=100, value=18)
    height = st.number_input("How much is your height in centimeter?", min_value=100, max_value=250, value=170, step=1)
    weight = st.number_input("How much is your weight in kilogram?", min_value=20, max_value=250, value=70, step=1)    
    children = st.number_input("How many children do you have?", min_value=0, max_value=20, value=0, step=1)

with right:
    gender = st.selectbox("What is your gender?", ["Male", "Female"]).lower()
    smoker = st.selectbox("Do you smoke?", ["Yes", "No"]).lower()
    region = st.selectbox("Which region do you currently reside in?", ["Southeast", "Southwest", "Northwest", "Northeast"]).lower()



bmi = weight / ((height/100)**2)

# inference
data = {'age':age,
        'bmi':bmi,
        'children': children,
        'gender':gender,
        'smoker':smoker,
        'region':region}

URL = "https://judan-ftds-009-p1m2-be.herokuapp.com/predict"

# komunikasi
pred = st.button("Predict")

if pred==True:
    r = requests.post(URL, json=data)
    res = r.json()
    if res['code'] == 200:
        st.subheader('Your predicted insurance fee is:')
        st.title(str(int(res['result']['prediction'])) + ' USD')
    else:
        st.write("There is an error.")
        st.write(f"The following error occurred: {res['result']['error_msg']}")