import streamlit as st

# Perguntas organizadas por disciplina
disciplinas = {
    "Lógica de Programação": [
        {"pergunta": "Qual é o comando usado para exibir algo na tela em Python?", "respostas": ["echo", "printf", "print", "output"], "resposta_correta": "print"},
        {"pergunta": "Qual desses é um tipo de dado primitivo em Python?", "respostas": ["Lista", "Dicionário", "Inteiro", "Conjunto"], "resposta_correta": "Inteiro"},
        {"pergunta": "Qual é a estrutura de controle que permite repetir um bloco de código várias vezes?", "respostas": ["if", "else", "for", "def"], "resposta_correta": "for"},
        {"pergunta": "O que é uma variável em programação?", "respostas": ["Um tipo de dado", "Uma referência para armazenar dados", "Uma função", "Um comando"], "resposta_correta": "Uma referência para armazenar dados"},  
        {"pergunta": "Qual é a diferença entre listas e tuplas em Python?", "respostas": ["Listas são imutáveis, tuplas são mutáveis", "Tuplas são imutáveis, listas são mutáveis", "Listas e tuplas são ambas mutáveis", "Nenhuma das alternativas"], "resposta_correta": "Tuplas são imutáveis, listas são mutáveis"},
        {"pergunta": "O que é uma função em Python?", "respostas": ["Um tipo de dado", "Um comando que repete uma operação", "Um bloco de código que executa uma tarefa específica", "Uma estrutura de controle"], "resposta_correta": "Um bloco de código que executa uma tarefa específica"},
        {"pergunta": "Como se chama uma estrutura de repetição que continua até que uma condição seja falsa?", "respostas": ["for", "while", "do-while", "repeat"], "resposta_correta": "while"},
        {"pergunta": "Qual é a finalidade do comando `return` em uma função?", "respostas": ["Para retornar um valor de uma função", "Para fazer um loop", "Para imprimir um valor", "Para encerrar a execução do programa"], "resposta_correta": "Para retornar um valor de uma função"},
        {"pergunta": "Qual estrutura de controle é usada para verificar se uma condição é verdadeira ou falsa?", "respostas": ["for", "if", "while", "try"], "resposta_correta": "if"},
        {"pergunta": "O que é um dicionário em Python?", "respostas": ["Um tipo de dado que armazena pares de chave-valor", "Um tipo de dado que armazena elementos em ordem", "Uma estrutura de controle", "Um comando de repetição"], "resposta_correta": "Um tipo de dado que armazena pares de chave-valor"},
        
],
    "Frontend": [
        {"pergunta": "Qual tag é usada para criar um parágrafo no HTML?", "respostas": ["<div>", "<p>", "<h1>", "<span>"], "resposta_correta": "<p>"},
        {"pergunta": "Qual propriedade CSS é usada para alterar a cor de fundo de um elemento?", "respostas": ["background-color", "color", "border", "font-style"], "resposta_correta": "background-color"},
        {"pergunta": "Qual tecnologia é usada para criar comportamento dinâmico em páginas da web?", "respostas": ["HTML", "CSS", "JavaScript", "SQL"], "resposta_correta": "JavaScript"},
        {"pergunta": "Qual tag HTML é usada para criar links?", "respostas": ["<a>", "<link>", "<href>", "<url>"], "resposta_correta": "<a>"},
        {"pergunta": "Qual unidade de medida é relativa ao tamanho da fonte do elemento pai?", "respostas": ["px", "em", "%", "rem"], "resposta_correta": "em"},
        {"pergunta": "Qual propriedade CSS é usada para centralizar texto dentro de um elemento?", "respostas": ["align-items", "justify-content", "text-align", "font-style"], "resposta_correta": "text-align"},
        {"pergunta": "Qual atributo HTML é usado para definir uma imagem em uma página?", "respostas": ["src", "alt", "href", "link"], "resposta_correta": "src"},
        {"pergunta": "Qual é a função do atributo 'alt' em uma tag de imagem?", "respostas": ["Adicionar um link à imagem", "Definir um texto alternativo caso a imagem não carregue", "Definir o tamanho da imagem", "Alterar o estilo da imagem"], "resposta_correta": "Definir um texto alternativo caso a imagem não carregue"},
        {"pergunta": "O que é o 'box model' no CSS?", "respostas": ["Uma técnica de flexbox", "Uma maneira de organizar tabelas", "Um modelo para representar margens, bordas, preenchimentos e conteúdo de um elemento", "Um tipo de layout específico para grids"], "resposta_correta": "Um modelo para representar margens, bordas, preenchimentos e conteúdo de um elemento"},
        {"pergunta": "Qual atributo CSS é usado para esconder completamente um elemento na página?", "respostas": ["display: none;", "visibility: hidden;", "opacity: 0;", "hidden: true;"], "resposta_correta": "display: none;"}
        

],
    "Banco de Dados": [
        {"pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?", "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"], "resposta_correta": "SELECT"},
        {"pergunta": "O que significa a sigla SQL?", "respostas": ["Simple Query Language", "Structured Query Language", "Secure Query Language", "Server Query Language"], "resposta_correta": "Structured Query Language"},
        {"pergunta": "Qual comando SQL é usado para adicionar um registro em uma tabela?", "respostas": ["ADD", "INSERT INTO", "APPEND", "CREATE"], "resposta_correta": "INSERT INTO"},
        {"pergunta": "Qual comando SQL é usado para remover todos os registros de uma tabela sem apagar a tabela?", "respostas": ["DELETE", "DROP", "TRUNCATE", "REMOVE"], "resposta_correta": "TRUNCATE"},
        {"pergunta": "Qual comando é usado para criar um banco de dados no SQL?", "respostas": ["CREATE DATABASE", "CREATE TABLE", "NEW DATABASE", "MAKE DATABASE"], "resposta_correta": "CREATE DATABASE"},
        {"pergunta": "Qual é a cláusula SQL usada para filtrar registros?", "respostas": ["WHERE", "FILTER", "HAVING", "GROUP BY"], "resposta_correta": "WHERE"},
        {"pergunta": "Qual tipo de dado SQL é usado para armazenar texto longo?", "respostas": ["VARCHAR", "TEXT", "STRING", "LONGTEXT"], "resposta_correta": "TEXT"},
        {"pergunta": "Qual comando é usado para modificar a estrutura de uma tabela?", "respostas": ["UPDATE", "ALTER TABLE", "MODIFY", "RESTRUCTURE"], "resposta_correta": "ALTER TABLE"},
        {"pergunta": "O que é uma chave primária em um banco de dados relacional?", "respostas": ["Um campo que armazena valores duplicados", "Um campo que identifica exclusivamente cada registro", "Uma tabela que contém registros únicos", "Um índice especial para acelerar consultas"], "resposta_correta": "Um campo que identifica exclusivamente cada registro"},
        {"pergunta": "Qual comando SQL é usado para juntar dados de várias tabelas?", "respostas": ["JOIN", "UNION", "COMBINE", "MERGE"], "resposta_correta": "JOIN"}
        
        
],
    "TypeScript": [
        {"pergunta": "O que é TypeScript?", "respostas": ["Uma linguagem de programação interpretada", "Um superconjunto de JavaScript com tipagem estática", "Um framework para JavaScript", "Um banco de dados relacional"], "resposta_correta": "Um superconjunto de JavaScript com tipagem estática"},
        {"pergunta": "Qual a extensão padrão dos arquivos TypeScript?", "respostas": [".ts", ".js", ".tsx", ".jsx"], "resposta_correta": ".ts"},
        {"pergunta": "Qual comando é usado para compilar arquivos TypeScript para JavaScript?", "respostas": ["tsc", "npm build", "node build", "compile-ts"], "resposta_correta": "tsc"},
        {"pergunta": "Qual dessas características é exclusiva do TypeScript?", "respostas": ["Manipulação de DOM", "Inferência de tipos", "Suporte a ES6", "Execução no navegador"], "resposta_correta": "Inferência de tipos"},
        {"pergunta": "Quem desenvolveu o TypeScript?", "respostas": ["Google", "Microsoft", "Facebook", "Apple"], "resposta_correta": "Microsoft"},
        {"pergunta": "Qual comando inicializa um projeto TypeScript?", "respostas": ["tsc --init", "npm init ts", "ts-init", "typescript init"], "resposta_correta": "tsc --init"},
        {"pergunta": "O que o arquivo tsconfig.json faz?", "respostas": ["Configura a compilação do TypeScript", "Instala pacotes TypeScript", "Cria componentes React", "Define o ambiente de execução"], "resposta_correta": "Configura a compilação do TypeScript"},
        {"pergunta": "Qual desses tipos não existe no TypeScript?", "respostas": ["number", "boolean", "string", "decimal"], "resposta_correta": "decimal"},
        {"pergunta": "Qual comando instala o TypeScript globalmente?", "respostas": ["npm install -g typescript", "npm install typescript", "yarn add typescript", "npm typescript install"], "resposta_correta": "npm install -g typescript"},
        {"pergunta": "Qual funcionalidade do TypeScript ajuda a detectar erros antes da execução?", "respostas": ["Tipagem estática", "Polimorfismo", "Renderização no servidor", "Closures"], "resposta_correta": "Tipagem estática"}
        

],
    "Segurança da Informação": [
        {"pergunta": "O que significa a sigla CIA em segurança da informação?", "respostas": ["Confidentiality, Integrity, Availability", "Control, Integrity, Authentication", "Confidentiality, Integrity, Authorization", "Confidentiality, Identification, Authorization"], "resposta_correta": "Confidentiality, Integrity, Availability"},
        {"pergunta": "O que é um ataque de phishing?", "respostas": ["Um ataque de força bruta", "Uma tentativa de obter informações sensíveis se passando por uma entidade confiável", "Um ataque de negação de serviço (DDoS)", "Uma exploração de vulnerabilidade em software"], "resposta_correta": "Uma tentativa de obter informações sensíveis se passando por uma entidade confiável"},
        {"pergunta": "Qual é o objetivo de um firewall?", "respostas": ["Armazenar dados com segurança", "Proteger uma rede ao controlar o tráfego de entrada e saída", "Gerar senhas seguras automaticamente", "Proteger contra ataques de phishing"], "resposta_correta": "Proteger uma rede ao controlar o tráfego de entrada e saída"},
        {"pergunta": "O que é uma senha forte?", "respostas": ["Apenas números", "Uma sequência de palavras do dicionário", "Uma combinação de letras, números e caracteres especiais", "Uma senha curta e fácil de lembrar"], "resposta_correta": "Uma combinação de letras, números e caracteres especiais"},
        {"pergunta": "O que é um certificado digital?", "respostas": ["Um documento físico que comprova identidade", "Um protocolo de segurança para redes sem fio", "Um arquivo eletrônico que autentica a identidade de uma entidade", "Uma tecnologia para criptografar e-mails"], "resposta_correta": "Um arquivo eletrônico que autentica a identidade de uma entidade"},
        {"pergunta": "O que é criptografia?", "respostas": ["O processo de armazenamento de dados em nuvem", "A técnica de proteger dados por meio de codificação", "Uma forma de ataque cibernético", "A criação de backups seguros"], "resposta_correta": "A técnica de proteger dados por meio de codificação"},
        {"pergunta": "Qual dessas é uma boa prática de segurança da informação?", "respostas": ["Usar a mesma senha para todas as contas", "Compartilhar senhas com colegas", "Habilitar autenticação de dois fatores", "Desativar antivírus para melhorar desempenho"], "resposta_correta": "Habilitar autenticação de dois fatores"},
        {"pergunta": "O que é ransomware?", "respostas": ["Um tipo de malware que exige resgate para restaurar o acesso a dados", "Um antivírus desenvolvido para grandes empresas", "Um método de autenticação seguro", "Um protocolo de criptografia"], "resposta_correta": "Um tipo de malware que exige resgate para restaurar o acesso a dados"},
        {"pergunta": "O que significa VPN?", "respostas": ["Virtual Private Network", "Verified Personal Network", "Virtual Public Network", "Verified Private Network"], "resposta_correta": "Virtual Private Network"},
        {"pergunta": "Qual das opções é considerada uma vulnerabilidade de segurança?", "respostas": ["Uso de firewalls", "Senhas fracas", "Atualização de softwares", "Criptografia de dados"], "resposta_correta": "Senhas fracas"}
        

]}
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
	
