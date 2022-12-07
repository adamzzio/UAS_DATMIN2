# IMPORT LIBRARY
import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import plotly.express as px
import requests
from PIL import Image
import networkx as nx
from pyvis.network import Network

# SET PAGE
pageicon = Image.open("aset_web/LOGO_WAZEEK.png")
st.set_page_config(page_title="Wazeek Web App", page_icon=pageicon, layout="centered")

# IMPORT DATASET
# df = pd.read_excel('DATA_DATMIN_KEL11_CREDIT SCORING.xlsx')

# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_0pfddxbb.json")

# HEADER
intro_column_left, intro_column_right = st.columns(2)
with st.container():
    with intro_column_left:
        # st.title(":bar_chart: Dashboard")
        st.markdown('<div style="text-align: justify; font-size:210%; line-height: 150%; margin-top: 10px;"> <b><br>Dashboard Analisis Sentimen Resesi Ekonomi 2023 di Indonesia </b> </div>',
            unsafe_allow_html=True)
    with intro_column_right:
        st_lottie(lottie_coding, height=250, key="dashboard")

st.markdown('<hr>', unsafe_allow_html=True)

# LOAD DATASET
@st.experimental_singleton
def load_datasets():
    data_label = pd.read_excel('data/KelB_Data_Labelled.xlsx')
    data_label = data_label[['Text', 'Label_Akhir']]
    data_label = data_label.rename(columns={'Label_Akhir':'Sentimen'})
    data_label = data_label[data_label['Sentimen'] != 999]
    data_label['Sentimen'] = data_label['Sentimen'].replace(0, 'Netral')
    data_label['Sentimen'] = data_label['Sentimen'].replace(1, 'Positif')
    data_label['Sentimen'] = data_label['Sentimen'].replace(-1, 'Negatif')
    data_network = pd.read_excel('data/KelB_Data_Network.xlsx')
    return data_label, data_network

data_label, data_network = load_datasets()

# ANGKA STATISTIK
left_column1, middle_column1, right_column1 = st.columns(3)
with left_column1:
    st.subheader("Jumlah Sentimen Positif")
    sum_pos = data_label[data_label['Sentimen'] == 'Positif']['Sentimen'].count()
    text_sum_pos = "### " + str(sum_pos)
    st.write(text_sum_pos)
with middle_column1:
    st.subheader("Jumlah Sentimen Netral")
    sum_net = data_label[data_label['Sentimen'] == 'Netral']['Sentimen'].count()
    text_sum_net = "### " + str(sum_net)
    st.write(text_sum_net)
with right_column1:
    st.subheader("Jumlah Sentimen Negatif")
    sum_neg = data_label[data_label['Sentimen'] == 'Negatif']['Sentimen'].count()
    text_sum_neg = "### " + str(sum_neg)
    st.write(text_sum_neg)

st.markdown('<hr>', unsafe_allow_html=True)

# PIE CHART PROPORSI SENTIMEN
prop_sentimen = data_label.groupby('Sentimen')['Sentimen'].count()
prop_sentimen = pd.DataFrame(prop_sentimen).rename(columns={'Sentimen':'Jumlah'})
fig_pie_sentimen = px.pie(prop_sentimen,
                           values="Jumlah",
                           names=prop_sentimen.index,
                           title="<b>Proporsi Sentimen Positif, Netral, dan Negatif</b>")
st.plotly_chart(fig_pie_sentimen, use_container_width=True)

st.markdown('<hr>', unsafe_allow_html=True)

# NETWORK GRAPH
st.write('### Social Media Network Analysis')
option = st.selectbox(
    '',
    ('Pilih data yang akan dianalisis network-nya: ', 'Keseluruhan Dataset', 'Dataset Sentimen Positif',
     'Dataset Sentimen Netral', 'Dataset Sentimen Negatif'))

if option == '':
    pass
elif option == 'Keseluruhan Dataset':
    HtmlFile = open('network/Viz_Network_All.html', encoding='utf-8')
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)
elif option == 'Dataset Sentimen Positif':
    HtmlFile = open('network/Viz_Network_Positive.html', encoding='utf-8')
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)
elif option == 'Dataset Sentimen Netral':
    HtmlFile = open('network/Viz_Network_Neutral.html', encoding='utf-8')
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)
elif option == 'Dataset Sentimen Negatif':
    HtmlFile = open('network/Viz_Network_Negative.html', encoding='utf-8')
    # Load HTML file in HTML component for display on Streamlit page
    components.html(HtmlFile.read(), height=435)

st.markdown('<hr>', unsafe_allow_html=True)
# WORDCLOUD
st.write("### WordCloud")
wc_pos = Image.open('aset_web/Viz_WordCloud_Positive_Dataset.png')
wc_net = Image.open('aset_web/Viz_WordCloud_Neutral_Dataset.png')
wc_neg = Image.open('aset_web/Viz_WordCloud_Negative_Dataset.png')
# left_column2, mid_column2, right_column2 = st.columns(3)
# left_column2.image(wc_pos, caption = "WordCloud Positive Sentiment Dataset", use_column_width=True)
# mid_column2.image(wc_net, caption = "WordCloud Neutral Sentiment Dataset", use_column_width=True)
# right_column2.image(wc_neg, caption = "WordCloud Negative Sentiment Dataset", use_column_width=True)

st.image(wc_pos, caption = "WordCloud Positive Sentiment Dataset", use_column_width=True)
st.image(wc_net, caption = "WordCloud Neutral Sentiment Dataset", use_column_width=True)
st.image(wc_neg, caption = "WordCloud Negative Sentiment Dataset", use_column_width=True)

st.markdown('<hr>', unsafe_allow_html=True)