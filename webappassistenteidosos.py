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
            "pergunta": "O que significa POO?",
            "respostas": [
                "Programação Organizada em Objetos",
                "Programação Orientada a Objetos",
                "Projeto Orientado em Objetos",
                "Prototipagem de Objetos Orientados"
            ],
            "resposta_correta": "Programação Orientada a Objetos"
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
            "pergunta": "Qual é o valor de 'x' após executar: `x = 5; x += 2`?",
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
            "respostas": [
                "Um loop que nunca termina",
                "Um loop que termina após um número fixo de iterações",
                "Um loop usado apenas em funções",
                "Um tipo de estrutura condicional"
            ],
            "resposta_correta": "Um loop que nunca termina"
        },
        {
            "pergunta": "Em qual tipo de estrutura podemos armazenar pares de chave e valor?",
            "respostas": ["Lista", "Dicionário", "Tupla", "Conjunto"],
            "resposta_correta": "Dicionário"
        },
        {
            "pergunta": "Qual é a principal função do comando 'if'?",
            "respostas": [
                "Executar repetidamente um código",
                "Executar um código condicionalmente",
                "Definir uma variável",
                "Criar um loop"
            ],
            "resposta_correta": "Executar um código condicionalmente"
        },
        {
            "pergunta": "O que é um algoritmo?",
            "respostas": [
                "Um tipo de dado",
                "Uma sequência de instruções para resolver um problema",
                "Um comando para exibir na tela",
                "Uma estrutura de repetição"
            ],
            "resposta_correta": "Uma sequência de instruções para resolver um problema"
        }
    ],
    "Frontend": [
        {
            "pergunta": "Qual tag é usada para criar um parágrafo no HTML?",
            "respostas": ["<div>", "<p>", "<h1>", "<span>"],
            "resposta_correta": "<p>"
        },
        {
            "pergunta": "Qual propriedade CSS altera a cor do texto?",
            "respostas": ["text-color", "color", "font-color", "background-color"],
            "resposta_correta": "color"
        },
        {
            "pergunta": "O que significa HTML?",
            "respostas": [
                "Hyperlinks and Text Markup Language",
                "HyperText Markup Language",
                "HighText Markup Language",
                "HyperText Machine Language"
            ],
            "resposta_correta": "HyperText Markup Language"
        },
        {
            "pergunta": "Qual propriedade CSS é usada para centralizar texto?",
            "respostas": ["text-align", "center", "justify", "align"],
            "resposta_correta": "text-align"
        },
        {
            "pergunta": "Qual tag HTML é usada para criar links?",
            "respostas": ["<link>", "<a>", "<href>", "<url>"],
            "resposta_correta": "<a>"
        },
        {
            "pergunta": "Qual tecnologia é usada para criar comportamento dinâmico em páginas da web?",
            "respostas": ["HTML", "CSS", "JavaScript", "SQL"],
            "resposta_correta": "JavaScript"
        },
        {
            "pergunta": "Qual unidade CSS é relativa ao tamanho da fonte do elemento pai?",
            "respostas": ["px", "em", "%", "vh"],
            "resposta_correta": "em"
        },
        {
            "pergunta": "O que faz o atributo 'alt' na tag <img>?",
            "respostas": [
                "Define o texto alternativo para a imagem",
                "Altera a largura da imagem",
                "Remove a borda da imagem",
                "Define o alinhamento da imagem"
            ],
            "resposta_correta": "Define o texto alternativo para a imagem"
        },
        {
            "pergunta": "Qual é o propósito do modelo de caixa (box model) no CSS?",
            "respostas": [
                "Definir margens, bordas, preenchimentos e o conteúdo de um elemento",
                "Gerenciar apenas o conteúdo do elemento",
                "Criar animações no elemento",
                "Alterar apenas as cores do elemento"
            ],
            "resposta_correta": "Definir margens, bordas, preenchimentos e o conteúdo de um elemento"
        },
        {
            "pergunta": "Qual tag HTML é usada para criar tabelas?",
            "respostas": ["<table>", "<td>", "<tr>", "<tbody>"],
            "resposta_correta": "<table>"
        }
    ],
    "Banco de Dados": [
        {
            "pergunta": "Qual comando SQL é usado para selecionar dados de uma tabela?",
            "respostas": ["INSERT", "SELECT", "UPDATE", "DELETE"],
            "resposta_correta": "SELECT"
        },
        {
            "pergunta": "O que significa a sigla SQL?",
            "respostas": [
                "Simple Query Language",
                "Structured Query Language",
                "Secure Query Language",
                "Server Query Language"
            ],
            "resposta_correta": "Structured Query Language"
        },
        {
            "pergunta": "Qual comando SQL é usado para adicionar um registro em uma tabela?",
            "respostas": ["ADD", "INSERT INTO", "APPEND", "CREATE"],
            "resposta_correta": "INSERT INTO"
        },
        {
            "pergunta": "Qual palavra-chave SQL é usada para evitar registros duplicados?",
            "respostas": ["DISTINCT", "UNIQUE", "FILTER", "LIMIT"],
            "resposta_correta": "DISTINCT"
        },
        {
            "pergunta": "Qual comando SQL exclui uma tabela?",
            "respostas": ["DROP", "DELETE", "REMOVE", "TRUNCATE"],
            "resposta_correta": "DROP"
        },
        {
            "pergunta": "O que é uma chave primária (PRIMARY KEY)?",
            "respostas": [
                "Uma coluna usada para referenciar outra tabela",
                "Uma coluna ou conjunto de colunas que identificam unicamente uma linha",
                "Uma restrição para valores duplicados",
                "Uma palavra-chave para selecionar dados"
            ],
            "resposta_correta": "Uma coluna ou conjunto de colunas que identificam unicamente uma linha"
        },
        {
            "pergunta": "Qual comando SQL atualiza dados em uma tabela?",
            "respostas": ["MODIFY", "UPDATE", "SET", "ALTER"],
            "resposta_correta": "UPDATE"
        },
        {
            "pergunta": "O que é normalização em Banco de Dados?",
            "respostas": [
                "O processo de organizar dados para minimizar redundâncias",
                "A criação de tabelas temporárias",
                "A replicação de dados entre tabelas",
                "O uso de chaves estrangeiras"
            ],
            "resposta_correta": "O processo de organizar dados para minimizar redundâncias"
        },
        {
            "pergunta": "O que faz o comando SQL 'JOIN'?",
            "respostas": [
                "Exclui registros duplicados",
                "Combina registros de várias tabelas com base em uma condição",
                "Cria um índice na tabela",
                "Divide os registros de uma tabela"
            ],
            "resposta_correta": "Combina registros de várias tabelas com base em uma condição"
        },
        {
            "pergunta": "Qual é a diferença entre 'INNER JOIN' e 'OUTER JOIN'?",
            "respostas": [
                "INNER JOIN retorna apenas os registros correspondentes; OUTER JOIN retorna todos os registros de ambas as tabelas",
                "INNER JOIN retorna duplicatas; OUTER JOIN não",
                "INNER JOIN é mais rápido que OUTER JOIN",
                "Não há diferença"
            ],
            "resposta_c
