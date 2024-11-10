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
    st.image("https://via.placeholder.com/800x200.png?text=Bem-vindo+ao+Assistente", use_column_width=True)
    st.write("""
        Olá! Este é o Assistente para Idosos, um aplicativo criado para ajudar você a se conectar com seus amigos e familiares de forma fácil e rápida. 
        Escolha uma das opções abaixo e siga as instruções para realizar a ação desejada.
    """)

# Função para registrar os horários de remédios
def registrar_horarios_remedios():
    st.subheader("💊 Registre os Horários de Remédios")
    remedio_nome = st.text_input("Nome do remédio:")
    horario = st.time_input("Hora para tomar o remédio:", datetime.time(8, 0))

    if st.button("Adicionar Horário") and remedio_nome:
        # Adicionar o remédio e horário à lista, que agora está armazenada no session_state
        st.session_state.horarios_remedios.append({"remedio": remedio_nome, "horario": horario.strftime("%H:%M")})
        st.success(f"Horário para {remedio_nome} adicionado com sucesso!")

    # Exibir a lista de remédios e horários
    if st.session_state.horarios_remedios:
        st.write("### Horários dos Remédios:")
        for item in st.session_state.horarios_remedios:
            st.write(f"**{item['remedio']}** - {item['horario']}")

# Função para acionar membro da família em caso de mal-estar
def acionar_familia_emergencia():
    st.subheader("🚨 Acionar Família em Caso de Emergência")
    sintoma = st.selectbox("Selecione o sintoma:", ["Dor", "Enjoo", "Tontura", "Mal-estar"])
    contato_familia = st.selectbox("Escolha o membro da família para acionar:", 
                                   [f"{nome} ({numero})" for nome, numero in contatos.items() if nome != "Mãe" and nome != "Pai"])

    if st.button("Acionar Membro da Família"):
        if sintoma and contato_familia:
            nome_familia = contato_familia.split(' (')[0]
            email_familia = "email_do_familia@example.com"  # Substitua com o e-mail do membro da família
            mensagem = f"URGENTE: O idoso está com {sintoma}. Favor verificar."
            # Enviar e-mail
            enviar_email(email_familia, f"Sintoma de {sintoma} detectado", mensagem)
        else:
            st.error("Por favor, selecione um sintoma e um membro da família.")

# Função principal que controla a navegação
def main():
    adicionar_css()
    tela_boas_vindas()

    col1, col2 = st.columns(2)
    with col1:
        opcao = st.selectbox("O que você gostaria de fazer?", [
            "Ligar para um Contato via WhatsApp",
            "Registrar Horários de Remédios",
            "Acionar Família em Caso de Emergência"
        ])
    with col2:
        st.image("https://via.placeholder.com/150.png?text=Icon", use_column_width=True)

    if opcao == "Ligar para um Contato via WhatsApp":
        pass  # Implementar a lógica de WhatsApp se necessário
    elif opcao == "Registrar Horários de Remédios":
        registrar_horarios_remedios()
    elif opcao == "Acionar Família em Caso de Emergência":
        acionar_familia_emergencia()

if __name__ == '__main__':
    main()
