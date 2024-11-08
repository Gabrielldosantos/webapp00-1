import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Lista de contatos com nomes, e-mails e números de telefone (incluindo membros da família para emergências)
contatos = {
    "Ingred": {"numero": "+5511944701187", "email": "ingred@exemplo.com"},
    "Gabriel": {"numero": "+5511945329796", "email": "gabriel.838383@gmail.com"},
    "Pedro": {"numero": "+5511950815157", "email": "pedro@exemplo.com"},
    "Mãe": {"numero": "+5511945432145", "email": "mae@exemplo.com"},  # Exemplo de um contato de emergência
    "Pai": {"numero": "+5511945323456", "email": "pai@exemplo.com"}
}

# Função para enviar um e-mail
def enviar_email(subject, body, to_email):
    # Credenciais do servidor SMTP (Exemplo usando Gmail)
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_user = "seuemail@gmail.com"  # Seu e-mail
    smtp_password = "suasenha"  # Sua senha de aplicativo ou senha normal

    # Criar o objeto de mensagem
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Adicionar o corpo do e-mail
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Conectar ao servidor SMTP
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Criptografar a conexão
        server.login(smtp_user, smtp_password)  # Login no servidor de e-mail
        text = msg.as_string()
        server.sendmail(smtp_user, to_email, text)  # Enviar o e-mail
        server.quit()  # Fechar a conexão com o servidor SMTP
        return True
    except Exception as e:
        st.error(f"Erro ao enviar e-mail: {e}")
        return False

# Função para adicionar CSS personalizado
def adicionar_css():
    st.markdown("""
    <style>
        /* Cor de fundo do aplicativo */
        .reportview-container {
            background-color: #f4f4f9;  /* Cor de fundo do corpo */
        }

        /* Título da página */
        h1 {
            color: #1f4f6b;  /* Cor do título */
            font-family: 'Arial', sans-serif;
        }

        /* Subtítulos */
        h2 {
            color: #3e7b8e;  /* Cor dos subtítulos */
            font-family: 'Arial', sans-serif;
        }

        /* Texto normal */
        .markdown-text-container {
            color: #333333;  /* Cor do texto */
            font-family: 'Arial', sans-serif;
        }

        /* Cor dos botões */
        .stButton>button {
            background-color: #0066cc;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 10px 20px;
        }

        /* Efeito de hover no botão */
        .stButton>button:hover {
            background-color: #0057a0;
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

        /* Imagem de fundo da tela */
        .stApp {
            background-image: url("https://via.placeholder.com/1500x1000.png?text=Background+Image");
            background-size: cover;
            background-position: center;
        }
    </style>
    """, unsafe_allow_html=True)

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

# Função para acionar membro da família em caso de mal-estar
def acionar_familia_emergencia():
    st.subheader("🚨 Acionar Família em Caso de Emergência")

    # Opções de sintomas
    sintoma = st.selectbox("Selecione o sintoma:", ["Dor", "Enjoo", "Tontura", "Mal-estar"])

    # Escolher o membro da família a ser acionado
    contato_familia = st.selectbox("Escolha o membro da família para acionar:", 
                                   [f"{nome} ({contatos[nome]['email']})" for nome in contatos if nome != "Mãe" and nome != "Pai"])

    # Confirmar acionamento
    if st.button("Acionar Membro da Família"):
        if sintoma and contato_familia:
            nome_familia = contato_familia.split(' (')[0]
            email_familia = contatos[nome_familia]["email"]
            mensagem = f"URGENTE: O idoso está com {sintoma}. Favor verificar."
            
            # Enviar o e-mail de emergência
            assunto = f"Emergência - Sintoma de {sintoma} do Idoso"
            sucesso = enviar_email(assunto, mensagem, email_familia)
            
            if sucesso:
                st.success(f"A mensagem de emergência foi enviada para {nome_familia}!")
            else:
                st.error("Ocorreu um erro ao enviar a mensagem de emergência.")
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
                             ["Registrar Horários de Remédios", 
                              "Acionar Família em Caso de Emergência"])
    with col2:
        st.image("https://via.placeholder.com/150.png?text=Icon", use_column_width=True)
    
    # Chamar a função correta com base na escolha do usuário
    if opcao == "Registrar Horários de Remédios":
        st.write("Função para registrar horários de remédios será implementada em breve.")
    elif opcao == "Acionar Família em Caso de Emergência":
        acionar_familia_emergencia()

# Execução do aplicativo
if __name__ == '__main__':
    main()
