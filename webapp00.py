# MEU PRIMEIRO WEB APP
import streamlit as st
from ACTlib01 import *


# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Bem vindo/a ao seu assistente de navegação :) ")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("Vamos iniciar ?")

# Use st.subheader("") para adicionar um SUB CABEÇALHO ao seu Web app
st.subheader("O que deseja fazer hoje?")

# Use st.write("") para adicionar um texto ao seu Web app
st.writelist (" 1. Assistência para ligar para um contato 2. Assistência para enviar uma mensagem 3. Assistência para navegar na internet 4. Assistência para usar a câmera")

values = st.slider("Select a range of values", 0.0, 50.0, (5.0, 15.0))
st.write("Values:", values)

st.image("images.jpg", caption="Sunrise by the mountains")
page_bg_img = 'images.jpg'

