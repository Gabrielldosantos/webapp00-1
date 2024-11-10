import streamlit as st
import random
import matplotlib.pyplot as plt

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

# Função para exibir animação no texto
def animacao_pergunta(titulo):
    st.markdown(f"<h1 style='text-align: center; font-size: 3em; color: #FF6347; font-weight: bold;'>{titulo}</h1>", unsafe_allow_html=True)

# Função para exibir gráfico de desempenho
def exibir_grafico():
    acertos = [1 if resposta["resposta_usuario"] == resposta["resposta_correta"] else 0 for resposta in st.session_state.respostas_usuario]
    fig, ax = plt.subplots()
    ax.plot(range(1, len(acertos) + 1), acertos, marker='o', linestyle='-', color='b')
    ax.set_title("Desempenho nas Perguntas")
    ax.set_xlabel("Pergunta")
    ax.set_ylabel("Acertos")
    st.pyplot(fig)

# Função principal do Streamlit
def app():
    # Título e introdução
    st.title("Quiz de Lógica de Programação")
    st.write("Responda as perguntas sobre lógica de programação e veja seu desempenho! Boa sorte! 🎉")

    # Embaralhar perguntas para que fiquem em ordem aleatória
    random.shuffle(perguntas)

    # Inicializar o estado de sessão
    if 'respostas_usuario' not in st.session_state:
        st.session_state.respostas_usuario = []
        st.session_state.pergunta_atual = 0
        st.session_state.pontuacao = 0
        st.session_state.respondido = False  # Controla se a pergunta já foi respondida

    # Barra de progresso
    st.progress(st.session_state.pergunta_atual / len(perguntas))

    # Botões de "Seguir" e "Voltar"
    col1, col2 = st.columns([1, 10])
    with col1:
        if st.button("Voltar", disabled=st.session_state.pergunta_atual == 0):
            if st.session_state.pergunta_atual > 0:
                st.session_state.pergunta_atual -= 1

    with col2:
        if st.button("Seguir", disabled=st.session_state.pergunta_atual == len(perguntas)):
            if st.session_state.pergunta_atual < len(perguntas):
                st.session_state.pergunta_atual += 1

    # Exibir uma pergunta por vez
    pergunta_atual = st.session_state.pergunta_atual

    if pergunta_atual < len(perguntas):
        pergunta = perguntas[pergunta_atual]

        # Exibir animação no título
        animacao_pergunta(pergunta["pergunta"])

        # Mostrar as opções de resposta como botões
        for opcao in pergunta["respostas"]:
            if st.button(opcao, key=f"resposta_{pergunta_atual}_{opcao}", disabled=st.session_state.respondido):
                # Armazenar a resposta do usuário
                st.session_state.respostas_usuario.append({
                    "pergunta": pergunta["pergunta"],
                    "resposta_usuario": opcao,
                    "resposta_correta": pergunta["resposta_correta"]
                })
                
                # Feedback imediato
                if opcao == pergunta["resposta_correta"]:
                    st.success("Resposta Correta! 🎉")
                    st.session_state.pontuacao += 1
                else:
                    st.error("Resposta Errada 😞")
                
                # Controlar se a pergunta foi respondida
                st.session_state.respondido = True
                break  # Evitar múltiplos cliques

        # Passar automaticamente para a próxima pergunta após resposta
        if st.session_state.respondido:
            st.session_state.respondido = False  # Resetar o controle de pergunta respondida
            st.session_state.pergunta_atual += 1

    # Exibir o resultado final do quiz
    if st.session_state.pergunta_atual == len(perguntas):
        st.write("Quiz Concluído!")
        st.write(f"Você acertou {st.session_state.pontuacao} de {len(perguntas)} perguntas!")

        # Exibir a pontuação final
        score = (st.session_state.pontuacao / len(perguntas)) * 10
        st.write(f"Sua pontuação final é: {score:.1f}/10")

        # Comentário baseado na pontuação
        if score == 10:
            st.success("🥳 Excelente! Você acertou todas as perguntas!")
        elif score >= 7:
            st.success("👍 Bom trabalho! Você tem uma boa compreensão de lógica de programação!")
        elif score >= 5:
            st.warning("🙂 Você se saiu bem, mas pode melhorar. Continue praticando!")
        else:
            st.error("😞 Parece que você precisa estudar mais. Tente novamente!")

        # Exibir gráfico de desempenho
        exibir_grafico()

        # Botão para reiniciar o quiz
        if st.button("Reiniciar Quiz"):
            st.session_state.pergunta_atual = 0
            st.session_state.pontuacao = 0
            st.session_state.respostas_usuario = []

# Executar o app
if __name__ == "__main__":
    app()
