import streamlit as st
import time
from random import shuffle

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

# Função para adicionar animações no texto
def animacao_pergunta(titulo):
    st.markdown(f"<h1 style='text-align: center; font-size: 3em; color: #FF6347; font-weight: bold;'>{titulo}</h1>", unsafe_allow_html=True)

def animacao_resposta(feedback):
    if feedback == "correto":
        st.markdown(f"<h2 style='text-align: center; color: #32CD32; font-size: 2em;'>Resposta Correta! ✅</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center; color: #FF6347; font-size: 2em;'>Resposta Errada! ❌</h2>", unsafe_allow_html=True)

# Função principal do Streamlit
def app():
    # Adicionar música de fundo
    st.audio("background_music.mp3", format="audio/mp3", start_time=0)

    # Título e introdução
    st.title("Quiz Animado")
    st.write("Responda as perguntas abaixo e veja seu desempenho! Boa sorte! 🎉")

    # Estado de sessão para armazenar as respostas do usuário
    if 'respostas_usuario' not in st.session_state:
        st.session_state.respostas_usuario = []
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0

    # Exibir uma pergunta por vez
    pergunta_atual = st.session_state.pergunta_atual

    # Verificar se a pergunta_atual não excede o número de perguntas
    if pergunta_atual < len(perguntas):
        pergunta = perguntas[pergunta_atual]

        # Exibir animação na tela
        animacao_pergunta(pergunta["pergunta"])

        # Embaralhar as respostas para tornar o quiz mais dinâmico
        shuffle(pergunta["respostas"])

        # Mostrar opções de resposta com cores
        resposta_usuario = st.radio(
            "Escolha a resposta:", pergunta["respostas"], key=pergunta["pergunta"], 
            help="Escolha a resposta correta"
        )

        # Armazenar a resposta e calcular pontuação
        if st.button("Próxima Pergunta"):
            # Verificar se a resposta do usuário está correta
            if resposta_usuario == pergunta["resposta_correta"]:
                st.session_state.pontuacao += 1
                animacao_resposta("correto")
            else:
                animacao_resposta("errado")

            # Armazenar resposta do usuário
            st.session_state.respostas_usuario.append({
                "pergunta": pergunta["pergunta"],
                "resposta_usuario": resposta_usuario,
                "resposta_correta": pergunta["resposta_correta"]
            })

            # Avançar para a próxima pergunta ou terminar
            st.session_state.pergunta_atual += 1

    # Se já tiver terminado o quiz, exibir o resultado
    if st.session_state.pergunta_atual == len(perguntas):
        st.write("Quiz Concluído!")
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas!")

        # Mostrar todas as perguntas com respostas corretas/erradas
        for resposta in st.session_state.respostas_usuario:
            if resposta["resposta_usuario"] == resposta["resposta_correta"]:
                st.write(f"**Pergunta**: {resposta['pergunta']}")
                st.write(f"**Sua resposta**: {resposta['resposta_usuario']} (Correta!)\n")
            else:
                st.write(f"**Pergunta**: {resposta['pergunta']}")
                st.write(f"**Sua resposta**: {resposta['resposta_usuario']} (Errada)")
                st.write(f"**Resposta correta**: {resposta['resposta_correta']}\n")

        # Feedback visual baseado na pontuação
        if st.session_state.pontuacao == len(perguntas):
            st.success("🥳 Parabéns! Você acertou todas as perguntas!")
        elif st.session_state.pontuacao >= len(perguntas) / 2:
            st.warning("👍 Bom trabalho! Você fez um bom desempenho!")
        else:
            st.error("😞 Parece que você precisa estudar mais! Tente novamente.")

# Executar o app
if __name__ == "__main__":
    app()
