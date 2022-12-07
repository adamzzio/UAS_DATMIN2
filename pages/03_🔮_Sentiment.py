import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
from sklearn import preprocessing
from PIL import Image
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')
import re, string
import requests

# SET PAGE
pageicon = Image.open("aset_web/LOGO_WAZEEK.png")
st.set_page_config(page_title="Wazeek Web App", page_icon=pageicon, layout="centered")

# SET TITLE
st.title('Yuk Cek Sentimen Terbaru Mengenai Tweet/Opini yang Anda Temukan!')

# DESCRIPTION
st.markdown('<div style="text-align: justify; font-size:160%"> Ayo berikan opini Anda tentang resesi ekonomi yang sedang terjadi! Dengan memberikan masukan yang bermanfaat, Anda dapat membantu kami menganalisis sentimen terkait resesi ini dan memahami pandangan masyarakat tentang masalah ini. Sampaikan opini Anda sekarang juga dan dukung kami dalam menganalisis sentimen terkait resesi ekonomi ini!</div>',
            unsafe_allow_html=True)
st.write('')

# DEFINE PIPELINE TEXT PREPROCESSING
def remove_mention(text):
  return re.sub(r'@[A-Za-z0-9]+\s?', '', str(text))
def remove_hashtag(text):
  return re.sub(r'#[A-Za-z0-9]+\s?', '', str(text))
def remove_https(text):
  return re.sub(r'https:\/\/.*', '', str(text))
def remove_number(text):
  return re.sub(r'\d+', '', str(text))
def remove_punc(text):
  return text.translate(str.maketrans('','',string.punctuation+"“"+"🫶"))
def remove_whitespace(text):
  return text.strip()
def remove_whitespace_multi(text):
  return re.sub('\s+', ' ', text)
def remove_single_char(text):
  return re.sub(r'\b[a-zA-Z]\b', '', text)
def word_tokenize_wrapper(text):
  return word_tokenize(text)

list_stopwords = stopwords.words('indonesian')
list_stopwords = set(list_stopwords)
def remove_stopwords(words):
  return [word for word in words if word not in list_stopwords]

# LOAD MODEL HOAX & CLICKBAIT CLASSIFICATION
filename_model = 'model/Model_Sentimen_SVM.sav'
filename_tfidf = 'model/TFIDF_Sentimen.pickle'

@st.experimental_singleton
def load_model():
    model = pkl.load(open(filename_model, 'rb'))
    tfidf = pkl.load(open(filename_tfidf, 'rb'))
    return model, tfidf

model, tfidf = load_model()

opini = st.text_input('Opini Anda mengenai isu Resesi 2023?',
                          placeholder='Contoh : Menurut saya, resesi kal ini dapat menjadi suatu opportunity yang menarik')
submit = st.button("Submit")

## SAVE INPUT IN DATAFRAME
data_result = pd.DataFrame({'Opini': [opini]})
data_result['Opini'] = data_result['Opini'].str.lower()
data_result['Opini'] = data_result['Opini'].apply(remove_mention)
data_result['Opini'] = data_result['Opini'].apply(remove_hashtag)
data_result['Opini'] = data_result['Opini'].apply(remove_https)
data_result['Opini'] = data_result['Opini'].apply(remove_number)
data_result['Opini'] = data_result['Opini'].apply(remove_punc)
data_result['Opini'] = data_result['Opini'].apply(remove_whitespace)
data_result['Opini'] = data_result['Opini'].apply(remove_whitespace_multi)
data_result['Opini'] = data_result['Opini'].apply(remove_single_char)
data_result['Opini'] = data_result['Opini'].apply(word_tokenize_wrapper)
data_result['Opini'] = data_result['Opini'].apply(remove_stopwords)
data_result['Opini'] = data_result['Opini'].agg(lambda x: ','.join(map(str, x)))
y_pred = model.predict(tfidf.transform(data_result['Opini'].values).toarray())
y_pred_proba = model.predict_proba(tfidf.transform(data_result['Opini'].values).toarray())

if submit:
    y_pred = str(y_pred)
    y_pred_proba = np.max(y_pred_proba[0])
    y_pred_proba = np.round(y_pred_proba, 2)
    y_pred_proba = y_pred_proba * 100
    if y_pred[1] == '0':
        text_result = 'Opini Anda ' + str(y_pred_proba) + '% Netral'
        st.info(text_result)
    elif y_pred[1] == '1':
        text_result = 'Opini Anda ' + str(y_pred_proba) + '% Positif'
        st.success(text_result)
    else:
        text_result = 'Opini Anda ' + str(y_pred_proba) + '% Negatif'
        st.error(text_result)
