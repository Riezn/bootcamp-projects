import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
from scipy import stats

def app():
    st.markdown('''
    # <center>Hypothesis Testing</center>
    Untuk menentukan target marketing campaign, uji hipotesis akan dilakukan untuk memastikan tipe customer mana yang sebaiknya menjadi target utama. Umumnya customer tipe Member berbelanja dengan Total belanja lebih besar dibandingkan customer tipe Normal. Untuk menguji pernyataan tersebut, akan disusun uji hipotesis menggunakan paired test one tailed dengan rumusan hipotesis sebagai berikut:
    - **H0: μMember <= μNormal**
    - **H1: μMember > μNormal**
    
    ''',unsafe_allow_html=True)
    
    #load data
    @st.cache
    def get_data():
        return pd.read_csv('cleandf.csv')
    df = get_data()
    df = df[['Total','Customer type']]

##########################################

    st.markdown('''
    ---
    Visualisasikan data menggunakan violin plot untuk memastikan ada outlier atau tidak pada data.
    ''')

    #violin plot
    fig = px.violin(df,y='Total',color='Customer type',box=True,points='all')
    
    #properties violin plot
    fig.update_layout(
        title="Violin Plot Dataset Member dan Normal",
        height=800,
        font=dict(size=15,family='sans-serif')
    )
    fig.update_xaxes(tickangle=-90)
    fig.update_yaxes(automargin=True)   
    st.plotly_chart(fig,use_container_width=True)

    st.markdown('''
    Pada violin plot kita temukan ada outlier. Kita coba hapus outlier tersebut berdasarkan IQR.
    ''')

##########################################

    #IQR Member
    ##deklarasi quartil
    Q1 = df[df['Customer type']=='Member']['Total'].quantile(0.25)
    Q3 = df[df['Customer type']=='Member']['Total'].quantile(0.75)
    IQR = Q3 - Q1

    ##deklarasi batas bawah dan batas atas data menggunakan IQR
    lower_limit_member = Q1 - 1.5 * IQR
    upper_limit_member = Q3 + 1.5 * IQR
    st.write("IQR Member: ", round(lower_limit_member,2), ("Lower dan "),  round(upper_limit_member,2), "Upper")

    df_member = df[df['Customer type']=='Member']

    ##filter data member
    df_member = df_member[(df_member['Total']<upper_limit_member)]
    df_member = df_member[(df_member['Total']>lower_limit_member)]
    st.write(df_member)
    
##########################################

    #IQR Normal
    ##deklarasi quartil
    Q1 = df[df['Customer type']=='Normal']['Total'].quantile(0.25)
    Q3 = df[df['Customer type']=='Normal']['Total'].quantile(0.75)
    IQR = Q3 - Q1

    ##deklarasi batas bawah dan batas atas data menggunakan IQR
    lower_limit_member = Q1 - 1.5 * IQR
    upper_limit_member = Q3 + 1.5 * IQR
    lower_limit_member, upper_limit_member
    st.write("IQR Normal: ", round(lower_limit_member,2), ("Lower dan "),  round(upper_limit_member,2), "Upper")

    df_normal = df[df['Customer type']=='Normal']

    ##filter data member
    df_normal = df_normal[(df_normal['Total']<upper_limit_member)]
    df_normal = df_normal[(df_normal['Total']>lower_limit_member)]
    st.write(df_normal)


##########################################

    st.markdown('''
    ---
    Sekarang kita akan lakukan uji hipotesis dengan confidence interval 95% atau critical value 0.05. Berikut hasil uji statistiknya:      
    ''')

    #paired t test one tailed
    t_stat,p_val = stats.ttest_rel((df_member['Total']).sample(490),(df_normal['Total']).sample(490),alternative='greater')
    st.write('P-value:',round(p_val,3),'\n')
    st.write('Karena p-value lebih besar dibandingkan critical value, maka kita terima pernyataan **rata-rata total belanja Member dan Normal tidak berbeda signifikan secara statistik**.')

    #deklarasi populasi menggunakan mean dan stdev dari sampel
    df_member_pop = np.random.normal((df_member['Total']).mean(), (df_member['Total']).std(), 10000)
    df_normal_pop = np.random.normal((df_normal['Total']).mean(), (df_normal['Total']).std(), 10000)

    #distribution plot
    fig = plt.figure(figsize=(15,6))
    ax = plt.axes()
    ci = stats.norm.interval(0.95, (df_member['Total']).mean(), (df_member['Total']).std()) #confidence interval 95% dengan critical value 0.05 atau 0.025 di dua sisi
    
    sns.distplot(df_member_pop, label='Log Total Member (Population)', color='blue') #data populasi
    sns.distplot(df_normal_pop, label='Log Total Normal (Population)', color='red') #data populasi

    ax.axvline((df_member['Total']).mean(), color='blue', linewidth=2, label='Log Total Member (Mean)') #rata-rata sampel
    ax.axvline((df_normal['Total']).mean(), color='red', linewidth=2, label='Log Total Normal (Mean)') #rata-rata sampel

    ax.axvline(ci[1], color='green', linestyle='dashed', linewidth=2, label='Confidence Threshold of 95%') #garis batas confidence interval
    ax.axvline(ci[0], color='green', linestyle='dashed', linewidth=2) #garis batas confidence interval
    fig.legend()

    st.pyplot(fig)

    st.markdown('''
    ---
    ## Kesimpulan
    Berdasarkan analisis yang telah dilakukan pada halaman Data Visualization dan Hypothesis Testing, berikut kesimpulan yang didapat:
    1. Product line yang akan ditingkatkan penjualannya adalah health and beauty
    2. Tidak perlu menyasar metode pembayaran tertentu untuk marketing campaign ini
    3. Tidak perlu menyasar cabang supermarket tertentu untuk marketing campaign ini
    4. Marketing campaign sebaiknya dilakukan di hari Sabtu atau Selasa
    5. Target customer pada marketing campaign ini adalah member dan normal
    ''')