import random
import streamlit as st

# Perguntas organizadas por disciplina
perguntas_gerais = [
    # Lógica de Programação
    {
        "pergunta": "Qual é o comando usado para exibir algo na tela em Python?",
        "respostas": ["echo", "printf", "print", "output"],
        "resposta_correta": "print"
    },
    {
        "pergunta": "Qual desses é um tipo de dado primitivo em Python?",
        "respostas": ["Lista", "Dicionário", "Inteiro", "Conjunto"],
        "resposta_correta": "Inteiro"
    },
    {
        "pergunta": "Qual é a estrutura de controle que permite repetir um bloco de código várias vezes?",
        "respostas": ["if", "else", "for", "def"],
        "resposta_correta": "for"
    },
    # Frontend
    {
        "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
        "respostas": ["<div>", "<p>", "<h1>", "<span>"],
        "resposta_correta": "<p>"
    },
    {
        "pergunta": "Qual propriedade CSS é usada para alterar a cor de fundo de um elemento?",
        "respostas": ["background-color", "color", "border", "font-style"],
        "resposta_correta": "background-color"
    },
    {
        "pergunta": "Qual tecnologia é usada para criar comportamento dinâmico em páginas da web?",
        "respostas": ["HTML", "CSS", "JavaScript", "SQL"],
        "resposta_correta": "JavaScript"
    },
    # Banco de Dados
    {
        "pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?",
        "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"],
        "resposta_correta": "SELECT"
    },
    {
        "pergunta": "O que significa a sigla SQL?",
        "respostas": ["Simple Query Language", "Structured Query Language", "Secure Query Language", "Server Query Language"],
        "resposta_correta": "Structured Query Language"
    },
    {
        "pergunta": "Qual comando SQL é usado para adicionar um registro em uma tabela?",
        "respostas": ["ADD", "INSERT INTO", "APPEND", "CREATE"],
        "resposta_correta": "INSERT INTO"
    },
    {
        "pergunta": "Em qual tipo de banco de dados as informações são organizadas em tabelas?",
        "respostas": ["NoSQL", "Relacional", "Hierárquico", "Em cache"],
        "resposta_correta": "Relacional"
    }
]

# Função principal do Streamlit
def app():
    st.title("Quiz Interativo de Estudo")
    st.write("Responda às perguntas e veja seu resultado no final! Boa sorte! 🎉")

    # Inicializar o estado da sessão
    if "quiz_iniciado" not in st.session_state:
        st.session_state.quiz_iniciado = False
        st.session_state.perguntas_sorteadas = []
        st.session_state.pergunta_atual = 0
        st.session_state.respostas_usuario = []
        st.session_state.pontuacao = 0

    # Iniciar o quiz
    if not st.session_state.quiz_iniciado:
        if st.button("Iniciar Quiz"):
            st.session_state.quiz_iniciado = True
            st.session_state.perguntas_sorteadas = random.sample(perguntas_gerais, 10)

    # Exibir perguntas
    if st.session_state.quiz_iniciado and st.session_state.pergunta_atual < 10:
        pergunta_atual = st.session_state.perguntas_sorteadas[st.session_state.pergunta_atual]
        st.write(f"**Pergunta {st.session_state.pergunta_atual + 1}:** {pergunta_atual['pergunta']}")

        # Opções de resposta
        for opcao in pergunta_atual["respostas"]:
            if st.button(opcao, key=f"resposta_{st.session_state.pergunta_atual}_{opcao}"):
                st.session_state.respostas_usuario.append({
                    "pergunta": pergunta_atual["pergunta"],
                    "resposta_usuario": opcao,
                    "resposta_correta": pergunta_atual["resposta_correta"]
                })
                if opcao == pergunta_atual["resposta_correta"]:
                    st.session_state.pontuacao += 1
                st.session_state.pergunta_atual += 1

    # Mostrar resultado ao final
    if st.session_state.pergunta_atual == 10:
        st.write("### Quiz Concluído!")
        st.write(f"Você acertou {st.session_state.pontuacao} de 10 perguntas.")

        # Exibir respostas corretas e do usuário
        st.write("### Respostas:")
        for idx, resposta in enumerate(st.session_state.respostas_usuario):
            st.write(f"**Pergunta {idx + 1}:** {resposta['pergunta']}")
            st.write(f"- Sua resposta: {resposta['resposta_usuario']}")
            st.write(f"- Resposta correta: {resposta['resposta_correta']}")

        # Exibir pontuação final
        score = (st.session_state.pontuacao / 10) * 10
        st.write(f"### Pontuação Final: {score:.1f}/10")

        if score == 10:
            st.success("🥳 Excelente! Você acertou todas!")
        elif score >= 7:
            st.success("👍 Bom trabalho!")
        elif score >= 5:
            st.warning("🙂 Pode melhorar. Continue praticando!")
        else:
            st.error("😞 Precisa estudar mais. Tente novamente!")

        # Botão para reiniciar o quiz
        if st.button("Reiniciar Quiz"):
            st.session_state.quiz_iniciado = False
            st.session_state.perguntas_sorteadas = []
            st.session_state.pergunta_atual = 0
            st.session_state.respostas_usuario = []
            st.session_state.pontuacao = 0

# Executar o app
if __name__ == "__main__":
    app()
