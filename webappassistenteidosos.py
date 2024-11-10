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

# Função principal do Streamlit
def app():
    st.title("Quiz de Perguntas e Respostas")
    st.write("Responda as perguntas abaixo:")

    # Estado de sessão para armazenar as respostas do usuário
    if 'respostas_usuario' not in st.session_state:
        st.session_state.respostas_usuario = []
        st.session_state.pergunta_atual = 0

    # Exibir uma pergunta por vez
    pergunta_atual = st.session_state.pergunta_atual
    pergunta = perguntas[pergunta_atual]

    # Exibir a pergunta e opções de resposta
    resposta_usuario = st.radio(pergunta["pergunta"], pergunta["respostas"], key=pergunta["pergunta"])

    # Armazenar a resposta
    if st.button("Próxima Pergunta"):
        st.session_state.respostas_usuario.append({
            "pergunta": pergunta["pergunta"],
            "resposta_usuario": resposta_usuario,
            "resposta_correta": pergunta["resposta_correta"]
        })

        # Avançar para a próxima pergunta
        if pergunta_atual < len(perguntas) - 1:
            st.session_state.pergunta_atual += 1
        else:
            st.session_state.pergunta_atual = len(perguntas)  # Fim do quiz

    # Se já tiver terminado o quiz, exibir o resultado
    if st.session_state.pergunta_atual == len(perguntas):
        st.write("Quiz Concluído!")
        pontuacao = 0

        # Mostrar as respostas
        for resposta in st.session_state.respostas_usuario:
            if resposta["resposta_usuario"] == resposta["resposta_correta"]:
                pontuacao += 1
                st.write(f"**Pergunta**: {resposta['pergunta']}")
                st.write(f"**Sua resposta**: {resposta['resposta_usuario']} (Correta!)\n")
            else:
                st.write(f"**Pergunta**: {resposta['pergunta']}")
                st.write(f"**Sua resposta**: {resposta['resposta_usuario']} (Errada)")
                st.write(f"**Resposta correta**: {resposta['resposta_correta']}\n")

        # Mostrar a pontuação final
        st.write(f"Você acertou {pontuacao} de {len(perguntas)} perguntas!")

        if pontuacao == len(perguntas):
            st.success("Parabéns! Você acertou todas as perguntas!")
        elif pontuacao >= len(perguntas) / 2:
            st.warning("Você fez um bom trabalho, mas ainda há espaço para melhorar!")
        else:
            st.error("Precisa estudar mais! Tente novamente.")

# Executar o app
if __name__ == "__main__":
    app()
