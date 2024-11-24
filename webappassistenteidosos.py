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
        {
            "pergunta": "Qual é o valor de 'x' após executar: `x = 3; x += 2`?",
            "respostas": ["3", "5", "2", "0"],
            "resposta_correta": "5"
        },
        {
            "pergunta": "O que significa a sigla POO?",
            "respostas": ["Programação Orientada a Operações", "Programação Orientada a Objetos", "Processamento Operacional de Objetos", "Planejamento Organizado e Otimizado"],
            "resposta_correta": "Programação Orientada a Objetos"
        },
        {
            "pergunta": "Qual é a função do comando 'while'?",
            "respostas": ["Criar uma função", "Repetir código enquanto uma condição é verdadeira", "Declarar uma variável", "Interromper um programa"],
            "resposta_correta": "Repetir código enquanto uma condição é verdadeira"
        },
        {
            "pergunta": "Em qual estrutura podemos usar pares de chave-valor?",
            "respostas": ["Lista", "Dicionário", "Tupla", "Conjunto"],
            "resposta_correta": "Dicionário"
        },
        {
            "pergunta": "Qual é a principal função do comando 'if'?",
            "respostas": ["Criar um loop", "Executar código condicionalmente", "Declarar uma variável", "Importar bibliotecas"],
            "resposta_correta": "Executar código condicionalmente"
        },
        {
            "pergunta": "O que é um algoritmo?",
            "respostas": ["Um tipo de dado", "Uma sequência de instruções para resolver problemas", "Um comando para exibir texto", "Uma estrutura de repetição"],
            "resposta_correta": "Uma sequência de instruções para resolver problemas"
        },
        {
            "pergunta": "O que significa depuração (debugging)?",
            "respostas": ["Criar um programa", "Encontrar e corrigir erros", "Compilar código", "Usar bibliotecas externas"],
            "resposta_correta": "Encontrar e corrigir erros"
        }
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
        {
            "pergunta": "O que é um framework frontend popular?",
            "respostas": ["React", "Node.js", "Django", "Laravel"],
            "resposta_correta": "React"
        },
        {
            "pergunta": "Qual atributo é usado para definir um link em HTML?",
            "respostas": ["src", "alt", "href", "class"],
            "resposta_correta": "href"
        },
        {
            "pergunta": "O que significa 'responsividade' no desenvolvimento frontend?",
            "respostas": ["Carregar páginas rapidamente", "Ajustar o layout a diferentes dispositivos", "Proteger dados do usuário", "Criar APIs seguras"],
            "resposta_correta": "Ajustar o layout a diferentes dispositivos"
        },
        {
            "pergunta": "Qual unidade de medida em CSS é relativa ao tamanho da fonte?",
            "respostas": ["px", "em", "cm", "%"],
            "resposta_correta": "em"
        },
        {
            "pergunta": "Qual método em JavaScript adiciona um elemento ao final de um array?",
            "respostas": ["push()", "pop()", "shift()", "unshift()"],
            "resposta_correta": "push()"
        },
        {
            "pergunta": "O que significa DOM?",
            "respostas": ["Data Object Model", "Document Object Model", "Dynamic Object Module", "Document Operational Mode"],
            "resposta_correta": "Document Object Model"
        },
        {
            "pergunta": "Qual tag HTML cria um botão clicável?",
            "respostas": ["<div>", "<button>", "<a>", "<input>"],
            "resposta_correta": "<button>"
        }
    ],
    # Adicionar 10 perguntas em Banco de Dados, TypeScript e Segurança da Informação como acima
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
