import streamlit as st
import urllib.parse
import datetime

# Lista de contatos com nomes e números de telefone
contatos = {
    "Ingred": "+5511944701187",
    "Gabriel": "+5511945329796",
    "Pedro": "+5511950815157"
}

# Lista para armazenar os horários dos remédios
horarios_remedios = []

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

# Função para ligar para um contato via WhatsApp
def ligar_contato_whatsapp():
    st.subheader("📞 Ligar para um Contato via WhatsApp")
    contato_selecionado = st.selectbox("Selecione um contato para ligar:", [f"{nome} ({numero})" for nome, numero in contatos.items()])
    
    # Extrair o número do contato selecionado
    contato_numero = contatos[contato_selecionado.split(' (')[0]]
    
    if st.button("Ligar pelo WhatsApp", key="call"):
        whatsapp_url = f"https://wa.me/{contato_numero}"
        st.markdown(f"[Clique aqui para ligar pelo WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
        st.success(f"Você será redirecionado para o WhatsApp para ligar para {contato_selecionado.split(' (')[0]}.")

# Função para enviar uma mensagem via WhatsApp
def enviar_mensagem_whatsapp():
    st.subheader("💬 Enviar Mensagem via WhatsApp")
    contato_selecionado = st.selectbox("Escolha o contato para enviar a mensagem:", [f"{nome} ({numero})" for nome, numero in contatos.items()])
    
    # Extrair o número do contato selecionado
    contato_numero = contatos[contato_selecionado.split(' (')[0]]
    
    mensagem = st.text_area("Digite a mensagem que deseja enviar:")
    
    if st.button("Enviar Mensagem", key="send_message"):
        if mensagem:
            # Codificar a mensagem para URL
            mensagem_codificada = urllib.parse.quote(mensagem)
            whatsapp_url = f"https://wa.me/{contato_numero}?text={mensagem_codificada}"
            st.markdown(f"[Clique aqui para enviar a mensagem pelo WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
            st.success(f"A mensagem foi enviada para {contato_selecionado.split(' (')[0]}.")
        else:
            st.error("Por favor, digite uma mensagem antes de enviar.")

# Função para navegar na internet
def navegar_internet():
    st.subheader("🌐 Navegar na Internet")
    url = st.text_input("Digite o site que deseja visitar (ex: www.google.com):")
    
    if st.button("Navegar", key="navigate"):
        if url:
            st.success(f"Abrindo o site {url}...")
            st.markdown(f"[Clique aqui para acessar {url}](http://{url})", unsafe_allow_html=True)
        else:
            st.error("Por favor, insira um URL válido.")

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
                              "Enviar uma Mensagem via WhatsApp", 
                              "Navegar na Internet", 
                              "Registrar Horários de Remédios"])
    with col2:
        st.image("https://via.placeholder.com/150.png?text=Icon", use_column_width=True)
    
    # Chamar a função correta com base na escolha do usuário
    if opcao == "Ligar para um Contato via WhatsApp":
        ligar_contato_whatsapp()
    elif opcao == "Enviar uma Mensagem via WhatsApp":
        enviar_mensagem_whatsapp()
    elif opcao == "Navegar na Internet":
        navegar_internet()
    elif opcao == "Registrar Horários de Remédios":
        registrar_horarios_remedios()

# Execução do aplicativo
if __name__ == '__main__':
    main()
