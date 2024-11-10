import streamlit as st

# Definir as 10 perguntas e respostas
perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "respostas": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador"],
        "resposta_correta": "Brasília"
    },
    {
        "pergunta": "Quem escreveu 'Dom Casmurro'?",
        "respostas": ["Machado de Assis", "José de Alencar", "Clarice Lispector", "Guimarães Rosa"],
        "resposta_correta": "Machado de Assis"
    },
    {
        "pergunta": "Qual é o maior planeta do sistema solar?",
        "respostas": ["Terra", "Júpiter", "Saturno", "Marte"],
        "resposta_correta": "Júpiter"
    },
    {
        "pergunta": "Em que ano o Brasil conquistou sua independência?",
        "respostas": ["1822", "1889", "1500", "1900"],
        "resposta_correta": "1822"
    },
    {
        "pergunta": "Quem pintou a Mona Lisa?",
        "respostas": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "resposta_correta": "Leonardo da Vinci"
    },
    {
        "pergunta": "Qual é a fórmula da água?",
        "respostas": ["H2O", "CO2", "O2", "H2O2"],
        "resposta_correta": "H2O"
    },
    {
        "pergunta": "Em que continente fica o Egito?",
        "respostas": ["África", "Ásia", "Europa", "América"],
        "resposta_correta": "África"
    },
    {
        "pergunta": "Quem foi o primeiro homem a pisar na lua?",
        "respostas": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "Alan Shepard"],
        "resposta_correta": "Neil Armstrong"
    },
    {
        "pergunta": "Qual é o maior oceano do mundo?",
        "respostas": ["Atlântico", "Índico", "Ártico", "Pacífico"],
        "resposta_correta": "Pacífico"
    },
    {
        "pergunta": "Qual é o símbolo químico do ouro?",
        "respostas": ["Au", "Ag", "Fe", "Pb"],
        "resposta_correta": "Au"
    }
]

# Função para calcular o número de respostas corretas
def calcular_pontuacao(respostas_usuario):
    pontuacao = 0
    for i, resposta in enumerate(respostas_usuario):
        if resposta == perguntas[i]["resposta_correta"]:
            pontuacao += 1
    return pontuacao

# Função principal do Streamlit
def app():
    st.title("Quiz de Perguntas e Respostas")
    st.write("Responda as perguntas abaixo:")

    respostas_usuario = []

    # Exibir perguntas e capturar as respostas
    for pergunta in perguntas:
        resposta = st.radio(pergunta["pergunta"], pergunta["respostas"], key=pergunta["pergunta"])
        respostas_usuario.append(resposta)

    # Quando o usuário submeter as respostas
    if st.button("Verificar Respostas"):
        pontuacao = calcular_pontuacao(respostas_usuario)
        total_perguntas = len(perguntas)
        
        # Mostrar a pontuação
        st.write(f"Você acertou {pontuacao} de {total_perguntas} perguntas!")
        
        # Feedback adicional
        if pontuacao == total_perguntas:
            st.success("Parabéns! Você acertou todas as perguntas!")
        elif pontuacao >= total_perguntas / 2:
            st.warning("Você fez um bom trabalho, mas ainda há espaço para melhorar!")
        else:
            st.error("Precisa estudar mais! Tente novamente.")
            
# Executar o app
if __name__ == "__main__":
    app()
