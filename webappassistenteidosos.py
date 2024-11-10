import streamlit as st
import time
from random import shuffle

# Definir as perguntas de lógica de programação
perguntas = [
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
        "pergunta": "O que é uma variável em programação?",
        "respostas": ["Um tipo de dado", "Uma operação matemática", "Um espaço na memória para armazenar dados", "Uma função"],
        "resposta_correta": "Um espaço na memória para armazenar dados"
    },
    {
        "pergunta": "Qual é a estrutura de controle que permite repetir um bloco de código várias vezes?",
        "respostas": ["if", "else", "for", "def"],
        "resposta_correta": "for"
    },
    {
        "pergunta": "Qual é o valor de 'x' após executar o seguinte código? `x = 5; x += 2`",
        "respostas": ["7", "5", "2", "10"],
        "resposta_correta": "7"
    },
    {
        "pergunta": "Qual comando em Python é usado para criar uma função?",
        "respostas": ["def", "function", "create", "func"],
        "resposta_correta": "def"
    },
    {
        "pergunta": "O que é um loop infinito?",
        "respostas": ["Um loop que nunca termina", "Um loop que termina após um número fixo de iterações", "Um loop usado apenas em funções", "Um tipo de estrutura condicional"],
        "resposta_correta": "Um loop que nunca termina"
    },
    {
        "pergunta": "Em qual tipo de estrutura de dados podemos armazenar pares de chave e valor?",
        "respostas": ["Lista", "Dicionário", "Tupla", "Conjunto"],
        "resposta_correta": "Dicionário"
    },
    {
        "pergunta": "Qual é a principal função do comando 'if'?",
        "respostas": ["Executar repetidamente um código", "Executar um código condicionalmente", "Definir uma variável", "Criar um loop"],
        "resposta_correta": "Executar um código condicionalmente"
    },
    {
        "pergunta": "O que é um algoritmo?",
        "respostas": ["Um tipo de dado", "Uma sequência de instruções para resolver um problema", "Um comando para exibir na tela", "Uma estrutura de repetição"],
        "resposta_correta": "Uma sequência de instruções para resolver um problema"
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
    # Título e introdução
    st.title("Quiz de Lógica de Programação")
    st.write("Responda as perguntas sobre lógica de programação e veja seu desempenho! Boa sorte! 🎉")

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
