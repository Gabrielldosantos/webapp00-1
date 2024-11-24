import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
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
        # ... Mais perguntas (total 10) ...
    ],
    "Frontend": [
        {
            "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
            "respostas": ["<div>", "<p>", "<h1>", "<span>"],
            "resposta_correta": "<p>"
        },
        {
            "pergunta": "Qual propriedade CSS altera a cor de fundo de um elemento?",
            "respostas": ["background-color", "color", "border", "font-style"],
            "resposta_correta": "background-color"
        },
        {
            "pergunta": "Qual tecnologia cria comportamento dinâmico em páginas da web?",
            "respostas": ["HTML", "CSS", "JavaScript", "SQL"],
            "resposta_correta": "JavaScript"
        },
        # ... Mais perguntas (total 10) ...
    ],
    "Banco de Dados": [
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
            "pergunta": "Qual é a função da chave primária em um banco de dados?",
            "respostas": ["Identificar de forma única um registro", "Proteger os dados", "Permitir valores duplicados", "Criar índices"],
            "resposta_correta": "Identificar de forma única um registro"
        },
        {
            "pergunta": "O que é um banco de dados relacional?",
            "respostas": [
                "Um banco de dados que armazena dados em forma de documentos",
                "Um banco que organiza dados em tabelas relacionadas",
                "Um banco que só armazena texto",
                "Um banco de dados não estruturado"
            ],
            "resposta_correta": "Um banco que organiza dados em tabelas relacionadas"
        },
        {
            "pergunta": "Qual é a função do comando SQL 'DELETE'?",
            "respostas": ["Remover tabelas", "Inserir registros", "Excluir registros", "Atualizar dados"],
            "resposta_correta": "Excluir registros"
        },
        {
            "pergunta": "Qual é a diferença entre 'WHERE' e 'HAVING' no SQL?",
            "respostas": [
                "'WHERE' filtra registros antes do agrupamento, 'HAVING' após o agrupamento",
                "'WHERE' é usado apenas em tabelas grandes",
                "'HAVING' é usado apenas com 'ORDER BY'",
                "Não há diferença entre os dois"
            ],
            "resposta_correta": "'WHERE' filtra registros antes do agrupamento, 'HAVING' após o agrupamento"
        },
        {
            "pergunta": "O que significa 'normalização' em bancos de dados?",
            "respostas": [
                "Remover valores duplicados",
                "Organizar dados para reduzir redundância",
                "Aumentar a velocidade do banco",
                "Proteger dados contra perda"
            ],
            "resposta_correta": "Organizar dados para reduzir redundância"
        },
        {
            "pergunta": "Qual é o comando para criar uma tabela no SQL?",
            "respostas": ["MAKE TABLE", "CREATE TABLE", "ADD TABLE", "INSERT TABLE"],
            "resposta_correta": "CREATE TABLE"
        },
        {
            "pergunta": "O que é um índice em um banco de dados?",
            "respostas": [
                "Um tipo de tabela especial",
                "Uma estrutura para acelerar buscas",
                "Uma tabela que contém chaves estrangeiras",
                "Uma forma de organizar backups"
            ],
            "resposta_correta": "Uma estrutura para acelerar buscas"
        }
    ],
    "TypeScript": [
        # ... Adicione 10 perguntas aqui ...
    ],
    "Segurança da Informação": [
        # ... Adicione 10 perguntas aqui ...
    ]
}

# Função principal do Streamlit
def app():
    st.title("Quiz Interativo de Estudo")
    st.write("Escolha uma disciplina e teste seus conhecimentos! 🎓")

    # Selecionar disciplina
    disciplina_escolhida = st.selectbox("Selecione uma disciplina", list(disciplinas.keys()))
    perguntas = disciplinas[disciplina_escolhida]

    # Inicializar estado de sessão
    if 'pergunta_atual' not in st.session_state:
        st.session_state.pergunta_atual = 0
        st.session_state.respostas_usuario = []
        st.session_state.pontuacao = 0

    # Exibir perguntas
    if st.session_state.pergunta_atual < len(perguntas):
        pergunta_atual = perguntas[st.session_state.pergunta_atual]
        st.write(f"**Pergunta {st.session_state.pergunta_atual + 1}:** {pergunta_atual['pergunta']}")

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

    # Mostrar resultados ao final
    if st.session_state.pergunta_atual == len(perguntas):
        st.write("### Quiz Concluído!")
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas.")

        st.write("### Respostas:")
        for idx, resposta in enumerate(st.session_state.respostas_usuario):
            st.write(f"**Pergunta {idx + 1}:** {resposta['pergunta']}")
            st.write(f"- Sua resposta: {resposta['resposta_usuario']}")
            st.write(f"- Resposta correta: {resposta['resposta_correta']}")

        # Reiniciar quiz
        if st.button("Reiniciar"):
            st.session_state.pergunta_atual = 0
            st.session_state.respostas_usuario = []
            st.session_state.pontuacao = 0

# Executar o app
if __name__ == "__main__":
    app()
