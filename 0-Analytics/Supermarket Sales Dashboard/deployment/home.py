import streamlit as st

def app():
    st.markdown('''
        <head>
            <style>
            .home {
                overflow-wrap: break-word;
                max-width: 720px;
                text-align: center;
                margin: auto;
            }
            </style>
        </head>
        
        <div class='home'>
            <h1>Homepage</h1> 
            <p>Dashboard ini dibuat untuk membantu mencapai tujuan perusahaan dalam meningkatkan profitabilitas dengan melakukan marketing campaign pada product line dengan total penjualan paling rendah.</p>
            <br>
            <p>Dataset yang digunakan untuk analisis dapat diakses pada link berikut:
            <a target="__blank" href="https://www.kaggle.com/aungpyaeap/supermarket-sales">https://www.kaggle.com/aungpyaeap/supermarket-sales</a></p>
            <br>
            <p>Author: Judan Syamsul Hadad
            <br>
            GitHub: <a target="__blank" href="https://github.com/Riezn">github.com/Riezn</a></p>
            
        </div>
    ''',unsafe_allow_html=True)

