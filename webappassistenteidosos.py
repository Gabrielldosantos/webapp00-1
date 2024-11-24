import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
        {"pergunta": "Qual é o comando usado para exibir algo na tela em Python?", "respostas": ["echo", "printf", "print", "output"], "resposta_correta": "print"},
        {"pergunta": "Qual desses é um tipo de dado primitivo em Python?", "respostas": ["Lista", "Dicionário", "Inteiro", "Conjunto"], "resposta_correta": "Inteiro"},
        {"pergunta": "Qual é a estrutura de controle que permite repetir um bloco de código várias vezes?", "respostas": ["if", "else", "for", "def"], "resposta_correta": "for"},
          
        # Adicione mais perguntas para completar as 10
    ],
    "Frontend": [
        {"pergunta": "Qual tag é usada para criar um parágrafo no HTML?", "respostas": ["<div>", "<p>", "<h1>", "<span>"], "resposta_correta": "<p>"},
        {"pergunta": "Qual propriedade CSS é usada para alterar a cor de fundo de um elemento?", "respostas": ["background-color", "color", "border", "font-style"], "resposta_correta": "background-color"},
        {"pergunta": "Qual tecnologia é usada para criar comportamento dinâmico em páginas da web?", "respostas": ["HTML", "CSS", "JavaScript", "SQL"], "resposta_correta": "JavaScript"},
        # Adicione mais perguntas para completar as 10
    ],
    "Banco de Dados": [
        {"pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?", "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"], "resposta_correta": "SELECT"},
        {"pergunta": "O que significa a sigla SQL?", "respostas": ["Simple Query Language", "Structured Query Language", "Secure Query Language", "Server Query Language"], "resposta_correta": "Structured Query Language"},
        {"pergunta": "Qual comando SQL é usado para adicionar um registro em uma tabela?", "respostas": ["ADD", "INSERT INTO", "APPEND", "CREATE"], "resposta_correta": "INSERT INTO"},
        # Adicione mais perguntas para completar as 10
    ],
    "TypeScript": [
        {"pergunta": "O que é TypeScript?", "respostas": ["Uma linguagem de programação interpretada", "Um superconjunto de JavaScript com tipagem estática", "Um framework para JavaScript", "Um banco de dados relacional"], "resposta_correta": "Um superconjunto de JavaScript com tipagem estática"},
        {"pergunta": "Qual a extensão padrão dos arquivos TypeScript?", "respostas": [".ts", ".js", ".tsx", ".jsx"], "resposta_correta": ".ts"},
        {"pergunta": "Qual comando é usado para compilar arquivos TypeScript para JavaScript?", "respostas": ["tsc", "npm build", "node build", "compile-ts"], "resposta_correta": "tsc"},
        # Adicione mais perguntas para completar as 10
    ],
    "Segurança da Informação": [
        {"pergunta": "O que significa a sigla CIA em segurança da informação?", "respostas": ["Confidentiality, Integrity, Availability", "Control, Integrity, Authentication", "Confidentiality, Integrity, Authorization", "Confidentiality, Identification, Authorization"], "resposta_correta": "Confidentiality, Integrity, Availability"},
        {"pergunta": "O que é um ataque de phishing?", "respostas": ["Um ataque de força bruta", "Uma tentativa de obter informações sensíveis se passando por uma entidade confiável", "Um ataque de negação de serviço (DDoS)", "Uma exploração de vulnerabilidade em software"], "resposta_correta": "Uma tentativa de obter informações sensíveis se passando por uma entidade confiável"},
        {"pergunta": "Qual é o objetivo de um firewall?", "respostas": ["Armazenar dados com segurança", "Proteger uma rede ao controlar o tráfego de entrada e saída", "Gerar senhas seguras automaticamente", "Proteger contra ataques de phishing"], "resposta_correta": "Proteger uma rede ao controlar o tráfego de entrada e saída"},
        # Adicione mais perguntas para completar as 10
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
        st.session_state.feedback = ""  # Inicializando o feedback como uma string vazia

    # Exibir perguntas
    if st.session_state.pergunta_atual < len(perguntas):
        pergunta_atual = perguntas[st.session_state.pergunta_atual]
        st.write(f"**Pergunta {st.session_state.pergunta_atual + 1}:** {pergunta_atual['pergunta']}")

        for opcao in pergunta_atual["respostas"]:
            if st.button(opcao, key=f"resposta_{st.session_state.pergunta_atual}_{opcao}"):
                # Verificar se a resposta está correta
                if opcao == pergunta_atual["resposta_correta"]:
                    st.session_state.feedback = "Correto!"
                    st.session_state.pontuacao += 1
                else:
                    st.session_state.feedback = f"Errado! A resposta correta era: {pergunta_atual['resposta_correta']}"
                
                st.session_state.respostas_usuario.append({
                    "pergunta": pergunta_atual["pergunta"],
                    "resposta_usuario": opcao,
                    "resposta_correta": pergunta_atual["resposta_correta"]
                })
                st.session_state.pergunta_atual += 1

    # Exibir feedback da resposta
    if st.session_state.feedback:
        st.write(f"**Feedback:** {st.session_state.feedback}")
        st.session_state.feedback = ""  # Resetar feedback para a próxima pergunta

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
            st.session_state.feedback = ""  # Resetar feedback

# Executar o app
if __name__ == "__main__":
    app()
