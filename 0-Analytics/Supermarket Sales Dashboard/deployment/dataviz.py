import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

def app():
    st.markdown('''
    # <center>Data Visualization</center>
    ## Pendahuluan
    Agar marketing campaign bisa berlangsung secara efektif, perusahaan harus menentukan strategi marketing terlebih dahulu. Berikut beberapa langkah untuk membantu menyusun strategi marketing perusahaan:
    - Menentukan product line yang paling rendah menghasilkan gross income
    - Menentukan target metode pembayaran preferensi pelanggan
    - Menentukan cabang yang akan dilakukan marketing campaign
    - Menentukan hari marketing campaign
    - Menentukan tanggal marketing campaign di tiap bulan
    ''',unsafe_allow_html=True)

    @st.cache
    def get_data():
        return pd.read_csv('cleandf.csv')
    #pendahuluan
    ##read dataframe
    df = get_data()
    
    ##checkbox show dataframe
    show_df = st.checkbox('Lihat Dataset')
    
    ##multiselect column
    defaultcols= ['Invoice ID','City','Customer type','Gender','Product line','Total','Date','Time','Day Name','Payment','gross income','Rating']
    if show_df:
        cols= st.multiselect('Pilih kolom untuk ditampilkan', df.columns.tolist(), default=defaultcols)
        st.write(df[cols]) 

##########################################

    #menentukan product line
    st.markdown('''
    ## Menentukan Product Line
    ''')

    ##radio button
    gender_prod_radio = st.radio('Pilih gender customer untuk ditampilkan pada bar chart product line',('All','Male','Female'))

    ##conditional berdasarkan radio button
    if gender_prod_radio == 'All':       
        yax=df[['Product line','gross income']].groupby('Product line').sum().sort_values('gross income',ascending=False)['gross income']
    else:
        yax=df[df['Gender']==gender_prod_radio][['Product line','gross income']].groupby('Product line').sum().sort_values('gross income',ascending=False)['gross income']
    
    #deklarasi variabel untuk bar chart dan properties-nya
    xax = df[['Product line','gross income']].groupby('Product line').sum().sort_values('gross income',ascending=False).index
    color_discrete_sequence = ['#1f77b4','#1f77b4','#1f77b4','#1f77b4','#1f77b4','#d62728']

    ##bar chart
    fig = px.bar(x=xax,y=yax.astype(int),text_auto=True,color=xax,color_discrete_sequence=color_discrete_sequence)
    
    ##properties bar chart
    fig.update_layout(
        title="Total Gross Income Berdasarkan Product Line",
        xaxis_title="Product Line",
        yaxis_title="Total Gross Income",
        showlegend=False,
        height=600,
        font=dict(size=15,family='sans-serif')
        )
    fig.update_xaxes(tickangle=-90)
    fig.update_yaxes(automargin=True)   
    st.plotly_chart(fig,use_container_width=True)

##########################################

    #menentukan preferensi metode pembayaran
    st.markdown('''
    ## Menentukan Preferensi Metode Pembayaran
    ''')

    ##select button
    payment_gender_select = st.selectbox('Pilih gender customer untuk ditampilkan pada  Pie Chart Metode Pembayaran',options=['All','Male','Female'])    
    payment_branch_select = st.selectbox('Pilih cabang supermarket untuk ditampilkan pada Pie Chart Metode Pembayaran',options=['All','Yangon','Mandalay','Naypyitaw'])

    ##conditional berdasarkan selectbox
    if payment_branch_select == 'All':
        if payment_gender_select == 'All':
            pie_data = df['Payment'].value_counts()
        else:
            pie_data = df[df['Gender']==payment_gender_select]['Payment'].value_counts()
    else:
        if payment_gender_select == 'All':
            pie_data = df[df['City']==payment_branch_select]['Payment'].value_counts()
        else:
            pie_data = df[(df['City']==payment_branch_select) & (df['Gender']==payment_gender_select)]['Payment'].value_counts()

    ##pie chart
    pie = px.pie(values=pie_data,names=df['Payment'].value_counts().keys())
    pie.update_layout(
        title="Pie Chart Metode Pembayaran",
        height=600,
        font=dict(size=15,family='sans-serif')
        )
    st.plotly_chart(pie,use_container_width=True)

##########################################

    #menentukan cabang
    st.markdown('''
    ## Menentukan Cabang untuk Marketing Campaign Berdasarkan Gross Income
    ''')

    ##ubah kolom tanggal menjadi tipe datetime64, lalu terima input dari slider tanggal
    df['Date'] = pd.to_datetime(df['Date']).dt.date
    startdate, enddate = st.select_slider(
        'Tentukan tanggal awal dan akhir untuk visualisasi gross income kumulatif',
        options=df['Date'].unique(),
        value=(df['Date'].min(),df['Date'].max()))    

    ##filter data berdasarkan callback streamlit
    gi = df[(df['Date']<=enddate)&(df['Date']>=startdate)][['City','gross income']].groupby('City').sum()
    
    ## bar chart dari data yang sudah di-filter
    ax = px.bar(y=gi.index,x=gi['gross income'],color=gi.index,orientation='h',text_auto=True)
    
    ## properties dari bar chart
    ax.update_layout(
        title="Gross Income Kumulatif Ketiga Cabang",
        xaxis_title="Gross Income Kumulatif, USD",
        yaxis_title="Kota",
        height=400,
        font=dict(size=15,family='sans-serif')
        )
    st.plotly_chart(ax,use_container_width=True)

##########################################

    #menentukan hari marketing campaign
    st.markdown('''
    ## Menentukan Hari untuk Marketing Campaign Berdasarkan Jumlah Transaksi
    ''')

    ##radio button
    day_branch_radio = st.radio('Pilih kota untuk ditampilkan pada line chart',('All','Yangon','Mandalay','Naypyitaw'))
    days = ['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu']

    ##conditional berdasarkan radio button
    if day_branch_radio == 'All':       
        daily = pd.DataFrame(df[['Day','Invoice ID']].groupby(['Day']).count())
    else:
        daily = pd.DataFrame(df[df['City']==day_branch_radio][['Day','Invoice ID']].groupby(['Day']).count()) 
    daily['Days'] = days

    ##line chart
    lifig = px.line(y=daily['Invoice ID'],x=daily['Days'])
    
    ##properties line chart
    lifig.update_layout(
        title="Tren Jumlah Transaksi Harian",
        xaxis_title="Hari",
        yaxis_title="Jumlah Transaksi",
        showlegend=False,
        height=600,
        font=dict(size=15,family='sans-serif')
        )
    lifig.update_xaxes(tickangle=-90)
    lifig.update_yaxes(automargin=True)   

    st.plotly_chart(lifig,use_container_width=True)