import streamlit as st
import smtplib
import ssl
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Lista de contatos com nomes e números de telefone (incluindo membros da família para emergências)
contatos = {
    "Ingred": "+5511944701187",
    "Gabriel": "+5511945329796",
    "Pedro": "+5511950815157",
    "Mãe": "+5511945432145",  # Exemplo de um contato de emergência
    "Pai": "+5511945323456"
}

# Lista para armazenar os horários dos remédios (persistência simples no Streamlit)
if 'horarios_remedios' not in st.session_state:
    st.session_state.horarios_remedios = []

# Função para adicionar CSS personalizado
def adicionar_css():
    st.markdown("""
    <style>
        .reportview-container {
            background-color: #eaf4e5;  /* Fundo verde suave */
        }
        h1 {
            color: #2c3e50;  /* Cor do título */
            font-family: 'Arial', sans-serif;
        }
        h2 {
            color: #3498db;  /* Cor dos subtítulos */
            font-family: 'Arial', sans-serif;
        }
        .markdown-text-container {
            color: #555555;  /* Cor do texto */
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #2980b9;  /* Cor do botão */
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #1c5980;
        }
        .stTextInput>div>input, .stTextArea>div>textarea {
            border-radius: 5px;
            border: 2px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }
        .stSelectbox>div>select {
            border-radius: 5px;
            border: 2px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }
        .stApp {
            background-color: #c1e2c1;  /* Fundo verde claro */
        }
        .reportview-container {
            background-color: rgba(255, 255, 255, 0.9);  /* Fundo translúcido claro */
        }
    </style>
    """, unsafe_allow_html=True)

# Função para enviar e-mail (uso de cache para evitar envios duplicados)
@st.cache_resource
def enviar_email(destinatario, assunto, corpo):
    sender_email = "gabriel.838383@gmail.com"
    password = "sua_senha"  # A senha não deve ser hardcoded em produção. Use variáveis de ambiente.
    
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, destinatario, msg.as_string())
            st.success(f"E-mail enviado com sucesso para {destinatario}.")
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {str(e)}")

# Função para a tela de boas-vindas
def tela_boas_vindas():
    st.title("Assistente para Idosos")
    st.image("https://via.placeholder.com/800x200.png?tex
