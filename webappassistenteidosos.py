import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
        {
            "pergunta": "Qual é o comando usado para exibir algo na tela em Python?",
            "respostas": ["echo", "printf", "print", "output"],
            "resposta_correta": "print"
        },
        # ... mais 9 perguntas de lógica de programação
    ],
    "Frontend": [
        {
            "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
            "respostas": ["<div>", "<p>", "<h1>", "<span>"],
            "resposta_correta": "<p>"
        },
        # ... mais 9 perguntas de Frontend
    ],
    "Banco de Dados": [
        {
            "pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?",
            "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"],
            "resposta_correta": "SELECT"
        },
        # ... mais 9 perguntas de Banco de Dados
    ],
    "TypeScript": [
        {
            "pergunta": "O que é TypeScript?",
            "respostas": [
                "Um framework de frontend",
                "Uma linguagem baseada em JavaScript com tipagem estática opcional",
                "Uma biblioteca de desenvolvimento backend",
                "Um sistema de banco de dados"
            ],
            "resposta_correta": "Uma linguagem baseada em JavaScript com tipagem estática opcional"
        },
        # ... mais 9 perguntas de TypeScript
    ],
    "Segurança da Informação": [
        {
            "pergunta": "O que é criptografia?",
            "respostas": [
                "O processo de proteger dados em repouso",
                "O processo de converter dados legíveis em um formato ilegível",
                "Uma técnica de compactação de arquivos",
                "Uma prática de backup de dados"
            ],
            "resposta_correta": "O processo de converter dados legíveis em um formato ilegível"
        },
        # ... mais 9 perguntas de Segurança da Informação
    ]
}

# Função principal do Streamlit
def app():
    st.title("Quiz Interativo por Disciplina")

    # Seleção da disciplina
    disciplina_escolhida = st.selectbox("Escolha a disciplina que deseja estudar:", list(disciplinas.keys()))

    # Perguntas da disciplina selecionada
    perguntas = disciplinas[disciplina_escolhida]

    # Inicializar estado da sessão
    if 'respostas_usuario' not in st.session_state:
        st.session_state.respostas_usuario = []
        st.session_state.pergunta_atual = 0
        st.session_state.respondido = False

    # Lógica do quiz
    pergunta_atual = st.session_state.pergunta_atual

    if pergunta_atual < len(perguntas):
        pergunta = perguntas[pergunta_atual]

        st.subheader(f"Pergunta {pergunta_atual + 1}: {pergunta['pergunta']}")

        for opcao in pergunta["respostas"]:
            if st.button(opcao, key=f"resposta_{pergunta_atual}_{opcao}"):
                st.session_state.respostas_usuario.append({
                    "pergunta": pergunta["pergunta"],
                    "resposta_usuario": opcao,
                    "resposta_correta": pergunta["resposta_correta"]
                })

                if opcao == pergunta["resposta_correta"]:
                    st.success("Resposta correta!")
                else:
                    st.error("Resposta incorreta!")

                st.session_state.pergunta_atual += 1
                break

    else:
        st.write("Você completou o quiz!")
        st.write(f"Acertos: {len([r for r in st.session_state.respostas_usuario if r['resposta_usuario'] == r['resposta_correta']])} de {len(perguntas)}")
        st.write("Respostas do quiz:")
        for r in st.session_state.respostas_usuario:
            st.write(f"Pergunta: {r['pergunta']}")
            st.write(f"Sua resposta: {r['resposta_usuario']} (Correta: {r['resposta_correta']})")

# Rodar o app
if __name__ == "__main__":
    app()
