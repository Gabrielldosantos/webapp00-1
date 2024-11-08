import streamlit as st
import urllib.parse
import datetime

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
            background-color: rgba(255, 255, 255, 0.7);  /* Fundo translúcido para melhorar contraste */
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

        /* Estilo para a imagem */
        .stApp {
            background-image: url("https://images.unsplash.com/photo-1592205787671-4417b2ca9ee1?crop=entropy&cs=tinysrgb&fit=max&ixid=MnwzNjEyOXwwfDF8c2VhY2h8OXx8bmljZSUyMGxhbmRzY2FwZXxlbnwwfHx8fDE2ODU4Mjg2NTI&ixlib=rb-1.2.1&q=80&w=1500"); /* Paisagem de campo ou parque */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            height: 100vh;
        }

        /* Adicionando uma camada de escurecimento para garantir que o texto fique legível */
        .reportview-container {
            background-color: rgba(255, 255, 255, 0.8);  /* Fundo semi-transparente */
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

    if st.button("Ligar pelo WhatsApp"):
        whatsapp_url = f"https://wa.me/{contato_numero}"
        st.markdown(f"[Clique aqui para ligar pelo WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
        st.success(f"Você será redirecionado para o WhatsApp para ligar para {contato_selecionado.split(' (')[0]}.")

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

# Função para acionar membro da família em caso de mal-estar
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
            numero_familia = contatos[contato_familia.split(' (')[0]]
            mensagem = f"URGENTE: O idoso está com {sintoma}. Favor verificar."

            # Codificar a mensagem para URL
            mensagem_codificada = urllib.parse.quote(mensagem)
            whatsapp_url = f"https://wa.me/{numero_familia}?text={mensagem_codificada}"

            st.markdown(f"[Clique aqui para acionar {nome_familia} pelo WhatsApp]({whatsapp_url})", unsafe_allow_html=True)
            st.success(f"A mensagem foi enviada para {nome_familia}.")
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
        ligar_contato_whatsapp()
    elif opcao == "Registrar Horários de Remédios":
        registrar_horarios_remedios()
    elif opcao == "Acionar Família em Caso de Emergência":
        acionar_familia_emergencia()

# Execução do aplicativo
if __name__ == '__main__':
    main()
