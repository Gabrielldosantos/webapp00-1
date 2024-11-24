import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
        {
            "pergunta": "Qual é o comando usado para exibir algo na tela em Python?",
            "respostas": ["echo", "printf", "print", "output"],
            "resposta_correta": "print"
        },
        # Adicione mais 9 perguntas aqui...
    ],
    "Frontend": [
        {
            "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
            "respostas": ["<div>", "<p>", "<h1>", "<span>"],
            "resposta_correta": "<p>"
        },
        # Adicione mais 9 perguntas aqui...
    ],
    "Banco de Dados": [
        {
            "pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?",
            "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"],
            "resposta_correta": "SELECT"
        },
        # Adicione mais 9 perguntas aqui...
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
        # Adicione mais 9 perguntas aqui...
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
        # Adicione mais 9 perguntas aqui...
    ]
}

# Função principal do Streamlit
def app():
    st.title("Quiz Interativo por Disciplina")

    # Inicializar estado de sessão para a disciplina
    if 'disciplina_escolhida' not in st.session_state:
        st.session_state.disciplina_escolhida = None

    # Seleção da disciplina (se não houver uma já selecionada)
    if st.session_state.disciplina_escolhida is None:
        disciplina = st.selectbox(
            "Escolha a disciplina que deseja estudar:", 
            list(disciplinas.keys())
        )
        if st.button("Confirmar Disciplina"):  # Só define a disciplina ao clicar no botão
            st.session_state.disciplina_escolhida = disciplina
            st.experimental_rerun()  # Recarrega a página após selecionar

    # Somente prosseguir se uma disciplina foi escolhida
    if st.session_state.disciplina_escolhida is not None:
        st.write(f"Você está estudando: **{st.session_state.disciplina_escolhida}**")

        # Perguntas da disciplina selecionada
        perguntas = disciplinas[st.session_state.disciplina_escolhida]

        # Inicializar estado da sessão para perguntas
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

            # Permitir reiniciar o quiz
            if st.button("Escolher outra disciplina"):
                del st.session_state.disciplina_escolhida
                del st.session_state.respostas_usuario
                del st.session_state.pergunta_atual
                st.experimental_rerun()

# Rodar o app
if __name__ == "__main__":
    app()
