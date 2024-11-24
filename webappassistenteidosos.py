import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
        {
            "pergunta": "Qual é o comando usado para exibir algo na tela em Python?",
            "respostas": ["echo", "printf", "print", "output"],
            "resposta_correta": "print"
        },
        # Outras perguntas de lógica de programação...
    ],
    "Frontend": [
        {
            "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
            "respostas": ["<div>", "<p>", "<h1>", "<span>"],
            "resposta_correta": "<p>"
        },
        # Outras perguntas de Frontend...
    ],
    "Banco de Dados": [
        {
            "pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?",
            "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"],
            "resposta_correta": "SELECT"
        },
        # Outras perguntas de Banco de Dados...
    ]
}

# Função para exibir animação no texto
def animacao_pergunta(titulo):
    st.markdown(f"<h1 style='text-align: center; font-size: 3em; color: #FF6347; font-weight: bold;'>{titulo}</h1>", unsafe_allow_html=True)

# Função principal do Streamlit
def app():
    st.title("Quiz Interativo para Estudo")
    st.write("Escolha uma disciplina e teste seus conhecimentos! 🎓")

    # Selecionar disciplina
    disciplina_escolhida = st.selectbox("Selecione uma disciplina", list(disciplinas.keys()))
    perguntas = disciplinas[disciplina_escolhida]

    # Inicializar estado de sessão
    if 'respostas_usuario' not in st.session_state:
        st.session_state.respostas_usuario = []
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0

    # Exibir uma pergunta por vez
    pergunta_atual = st.session_state.pergunta_atual

    if pergunta_atual < len(perguntas):
        pergunta = perguntas[pergunta_atual]

        animacao_pergunta(pergunta["pergunta"])

        for opcao in pergunta["respostas"]:
            if st.button(opcao, key=f"resposta_{pergunta_atual}_{opcao}"):
                st.session_state.respostas_usuario.append({
                    "pergunta": pergunta["pergunta"],
                    "resposta_usuario": opcao,
                    "resposta_correta": pergunta["resposta_correta"]
                })
                if opcao == pergunta["resposta_correta"]:
                    st.session_state.pontuacao += 1
                st.session_state.pergunta_atual += 1
                break

    # Se terminar o quiz
    if st.session_state.pergunta_atual == len(perguntas):
        st.write("Quiz Concluído!")
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas!")
        score = (st.session_state.pontuacao / len(perguntas)) * 10
        st.write(f"Sua pontuação final é: {score:.1f}/10")

        if score == 10:
            st.success("🥳 Excelente! Você acertou todas!")
        elif score >= 7:
            st.success("👍 Bom trabalho!")
        elif score >= 5:
            st.warning("🙂 Pode melhorar. Continue praticando!")
        else:
            st.error("😞 Precisa estudar mais!")

        # Botão para reiniciar o quiz
        if st.button("Reiniciar"):
            st.session_state.pergunta_atual = 0
            st.session_state.pontuacao = 0
            st.session_state.respostas_usuario = []

# Executar o app
if __name__ == "__main__":
    app()
