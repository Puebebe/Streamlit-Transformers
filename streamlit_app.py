import streamlit as st
import pandas as pd
import time
import matplotlib as plt
import os
# zaczynamy od zaimportowania bibliotek

st.set_page_config(
    page_title="NLP - Natural Language Processing",
    page_icon=":speech_balloon:",
    menu_items={
        'Report a Bug': None,
        'Get Help': 'https://share.streamlit.io/aipogodzinach/streamlit_pjatk/main',
        'About': "### This is an example Streamlit app.\n#### This app uses *🤗 Transformers* for Natural Language Processing (NLP).\nMore about 🤗 Transformers: \n - https://huggingface.co/transformers/index.html\n - https://huggingface.co/transformers/usage.html\n - https://github.com/huggingface/transformers\n\n"
    }
) # podstawowe informacje o stronie

st.success('Gratulacje! Z powodzeniem uruchomiłeś aplikację')
# streamlit jest wykorzystywany do tworzenia aplikacji
# z tego powodu dobrą praktyką jest informowanie użytkownika o postępie, błędach, etc.

st.title('Streamlit + 🤗 Transformers')

st.header('Wprowadzenie')

st.subheader('O Streamlit')
st.text('To przykładowa aplikacja z wykorzystaniem Streamlit')
st.write('Streamlit jest biblioteką pozwalającą na uruchomienie modeli uczenia maszynowego.')

st.header('Przetwarzanie języka naturalnego :scroll: :speech_balloon:')

import streamlit as st
from transformers import pipeline

options = ["Wydźwięk emocjonalny tekstu (eng)", "Tłumaczenie tekstu z języka angielskiego na język niemiecki"]

option = st.selectbox(
    "Opcje",
    [
        options[0],
        options[1],
    ],
)

if option == options[0]:
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text='Analizuję...'):
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            st.success('Analiza tekstu "' + text + '":\n\n' + 'etykieta -> ' + answer[0]['label'] + '\n\nwynik -> ' + str(answer[0]['score']))
elif option == options[1]:
    text = st.text_area(label="Wpisz tekst")
    if text:
        with st.spinner(text='Tłumaczę...'):
            translator = pipeline("translation_en_to_de")
            answer = translator(text)
            st.success('Tłumaczenie:\n\n' + text + ' -> ' + answer[0]['translation_text'])

st.caption("@ Bartłomiej Kawa, s18581")