import streamlit as st
import requests
from PIL import Image

#read page icon file
im = Image.open('analytic-icon-11438.png')

#Page Config
st.set_page_config(
    page_title="Telco Customer Retention Program",
    page_icon=im,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/Riezn',
        'Report a bug': None,
        'About': 'Predict our customer retention by Judan Syamsul Hadad - FTDS-009 https://github.com/Riezn'
    }
)

image = Image.open('connection.jpg')

st.markdown('''
    # <center>Customer Retention Program</center>
    #### <center>Stay Connedted</center>
    ''',unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,3,1])
with col2:
    st.image(image, use_column_width=True)
    st.markdown('''
    <center>Please answer the following questions to predict customer churn behavior.</center>
    ''',unsafe_allow_html=True)

left, right = st.columns(2)
with right:
    MultipleLines = st.selectbox("Does our customer use multiple lines phone service?", ['No phone service', 'No', 'Yes'])

    InternetService = st.selectbox("Which of our internet service does our customer use?", ['DSL', 'Fiber optic', 'None'])
    if InternetService == 'None':
        InternetService = 'No'

    PaperlessBilling = st.selectbox("Does our customer use paperless billing?", ['Yes', 'No'])

    Contract = Partner = st.selectbox("Which type of contract does our customer is currently undergoing?", ['Month-to-month', 'One year', 'Two year'])
    
    PaymentMethod = Partner = st.selectbox("What is the preferred payment method of our customer?", ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'])
    
with left:
    gender = st.selectbox("What is the gender of our customer?", ["Male", "Female"])
    
    SeniorCitizen = st.selectbox("Is the customer a senior citizen?", ["Yes", "No"])
    if SeniorCitizen == 'Yes':
        SeniorCitizen = 1
    else:
        SeniorCitizen = 0
        
    Partner = st.selectbox("Does our customer currently have a partner?", ["Yes", "No"])

    Dependents = st.selectbox("Does our customer currently have any dependent(s)?", ["Yes", "No"])

    tenure = st.slider("How many months has our customer subscribed to our service?", min_value=0, max_value=100, value=0, step=1)

    MonthlyCharges = st.slider("How much does our customer pay to  stay subscribed to our service in USD?", min_value=10, max_value=200, value=0, step=1)

# inference
data = {'gender':gender,
        'SeniorCitizen':SeniorCitizen,
        'Partner': Partner,
        'Dependents':Dependents,
        'Contract':Contract,
        'PaperlessBilling':PaperlessBilling,
        'PaymentMethod':PaymentMethod,
        'MultipleLines':MultipleLines,
        'InternetService':InternetService,
        'tenure':tenure,
        'MonthlyCharges':MonthlyCharges}

URL = "https://p2m1-backend-judan.herokuapp.com/"

# komunikasi
pred = st.button("Predict")

if pred==True:
    r = requests.post(URL, json=data)
    res = r.json()
    if res['code'] == 200:
        st.title('The customer will ' + str(res['result']['description']) + ' using our service.')
    else:
        st.write("There is an error.")
        st.write(f"The following error occurred: {res['result']['error_msg']}")