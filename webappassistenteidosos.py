import streamlit as st
import smtplib
import ssl
import datetime
import urllib.parse
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

# Lista para armazenar os horários dos remédios
horarios_remedios = []

# Função para adicionar CSS personalizado
def adicionar_css():
    st.markdown("""
    <style>
        /* Cor de fundo do aplicativo */
        .reportview-container {
            background-color: #eaf4e5;  /* Fundo verde suave */
        }

        /* Título da página */
        h1 {
            color: #2c3e50;  /* Cor do título */
            font-family: 'Arial', sans-serif;
        }

        /* Subtítulos */
        h2 {
            color: #3498db;  /* Cor dos subtítulos */
            font-family: 'Arial', sans-serif;
        }

        /* Texto normal */
        .markdown-text-container {
            color: #555555;  /* Cor do texto */
            font-family: 'Arial', sans-serif;
        }

        /* Cor dos botões */
        .stButton>button {
            background-color: #2980b9;  /* Cor do botão */
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }

        /* Efeito de hover no botão */
        .stButton>button:hover {
            background-color: #1c5980;
        }

        /* Adicionando uma borda arredondada nos campos de entrada de texto */
        .stTextInput>div>input, .stTextArea>div>textarea {
            border-radius: 5px;
            border: 2px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }

        /* Estilo para o Selectbox */
        .stSelectbox>div>select {
            border-radius: 5px;
            border: 2px solid #ddd;
            padding: 10px;
            font-size: 16px;
        }

        /* Cor de fundo principal */
        .stApp {
            background-color: #c1e2c1;  /* Fundo verde claro */
        }

        /* Adicionando uma camada de escurecimento para garantir que o texto fique legível */
        .reportview-container {
            background-color: rgba(255, 255, 255, 0.9);  /* Fundo translúcido claro */
        }
    </style>
    """, unsafe_allow_html=True)

# Função para enviar e-mail
def enviar_email(destinatario, assunto, corpo):
    sender_email = "gabriel.838383@gmail.com"
    receiver_email = destinatario
    password = "sua_senha"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            st.success(f"E-mail enviado com sucesso para {destinatario}.")
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {str(e)}")

# Função para a tela de boas-vindas
def tela_boas_vindas():
    st.title("Assistente para Idosos")
    st.image("https://via.placeholder.com/800x200.png?text=Bem-vindo+ao+Assistente", use_column_width=True)
    st.write(
        """
        Olá! Este é o Assistente para Idosos, um aplicativo criado para ajudar você a se conectar com seus amigos e familiares de forma fácil e rápida. 
        Escolha uma das opções abaixo e siga as instruções para realizar a ação desejada.
        """
    )

# Função para registrar os horários de remédios
def registrar_horarios_remedios():
    st.subheader("💊 Registre os Horários de Remédios")

    # Campo para o nome do remédio
    remedio_nome = st.text_input("Nome do remédio:")

    # Campo para o horário
    horario = st.time_input("Hora para tomar o remédio:", datetime.time(8, 0))

    if st.button("Adicionar Horário"):
        if remedio_nome:
            # Adicionar o remédio e horário à lista
            horarios_remedios.append({"remedio": remedio_nome, "horario": horario.strftime("%H:%M")})
            st.success(f"Horário para {remedio_nome} adicionado com sucesso!")
        else:
            st.error("Por favor, insira o nome do remédio.")

    # Exibir a lista de remédios e horários
    if horarios_remedios:
        st.write("### Horários dos Remédios:")
        for item in horarios_remedios:
            st.write(f"**{item['remedio']}** - {item['horario']}")

# Função para acionar membro da família em caso de mal-estar e enviar e-mail
def acionar_familia_emergencia():
    st.subheader("🚨 Acionar Família em Caso de Emergência")

    # Opções de sintomas
    sintoma = st.selectbox("Selecione o sintoma:", ["Dor", "Enjoo", "Tontura", "Mal-estar"])

    # Escolher o membro da família a ser acionado
    contato_familia = st.selectbox("Escolha o membro da família para acionar:",
                                   [f"{nome} ({numero})" for nome, numero in contatos.items() if nome != "Mãe" and nome != "Pai"])

    # Confirmar acionamento
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
    # Adicionando o CSS personalizado
    adicionar_css()

    # Exibição do título e da imagem de boas-vindas
    tela_boas_vindas()

    # Menu de opções organizado em um layout de 2 colunas
    col1, col2 = st.columns(2)
    with col1:
        opcao = st.selectbox("O que você gostaria de fazer?",
                             ["Ligar para um Contato via WhatsApp",
                              "Registrar Horários de Remédios",
                              "Acionar Família em Caso de Emergência"])
    with col2:
        st.image("https://via.placeholder.com/150.png?text=Icon", use_column_width=True)

    # Chamar a função correta com base na escolha do usuário
    if opcao == "Ligar para um Contato via WhatsApp":
        # Aqui você pode adicionar a lógica de WhatsApp novamente, se desejar
        pass
    elif opcao == "Registrar Horários de Remédios":
        registrar_horarios_remedios()
    elif opcao == "Acionar Família em Caso de Emergência":
        acionar_familia_emergencia()

# Execução do aplicativo
if __name__ == '__main__':
    main()
