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

# Inne przykłady do wypróbowania:
# st.balloons() # animowane balony ;)
# st.error('Błąd!') # wyświetla informację o błędzie
# st.warning('Ostrzeżenie, działa, ale chyba tak sobie...')
# st.info('Informacja...')
# st.success('Udało się!')

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
        classifier = pipeline("sentiment-analysis")
        answer = classifier(text)
        st.write(answer)
elif option == options[1]:
    text = st.text_area(label="Wpisz tekst")
    if text:
        translator = pipeline("translation_en_to_de")
        answer = translator(text)
        st.write(answer)

st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/transformers/usage.html')
st.write('✅ ~~Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?~~')
st.write('✅ ~~Dodaj krótką instrukcję i napisz do czego służy aplikacja~~')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('✅ ~~Na końcu umieść swój numer indeksu~~')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')

st.caption("@ Bartłomiej Kawa, s18581")