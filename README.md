# Integração de Chatbot usando Langchain e WhatsApp via WAHA

<img src="markdown/ProjetoLangChain.png">

## 🚀 Visão Geral

Este projeto consiste em um chatbot integrado ao WhatsApp, desenvolvido com Flask, que utiliza a biblioteca Langchain e a API do WAHA. O objetivo do chatbot é fornecer informações nutricionais detalhadas sobre alimentos, como carboidratos, proteínas, gorduras e calorias, aproveitando a Google Generative AI.

## 🎯 Objetivo do Projeto

A ideia surgiu a partir de um estudo de caso apresentado pela PyCodeBr sobre LLMs e AI.
Então tive a ideia de desenvolver um chatBot pudesse responder a perguntas sobre a composição nutricional de alimentos de maneira acessível e rápida. A implementação foi realizada utilizando a API do WAHA para permitir interações via WhatsApp.

## 💡 Funcionalidades

- **Respostas Automáticas**: O chatbot responde automaticamente a consultas sobre alimentos.
- **Informações Nutricionais**: Fornece dados sobre carboidratos, proteínas, gorduras, fibras e calorias.
- **Tratamento de Saudações**: Responde a saudações de maneira amigável, incentivando perguntas sobre alimentos.
- **Tratamento de Erros**: Responde a perguntas fora do escopo com uma mensagem adequada.

## 📦 Instalação


1. Instalação do WAHA

    Você Precisa ter uma instancia do WAHA rodando localmente na sua maquina na porta 3000 para o funcionamento do projeto e consumo de todos os endpoints.

    ```bash
    docker run -it -p 3000:3000/tcp devlikeapro/waha
    ```


2. Clone o repositório:

   ```bash
   git clone https://github.com/iiiiiuri/LLM-Nutricional.git
   cd <nome do diretório>
   ```


3. Instale as dependências necessárias:

   ```bash
    pip install -r requirements.txt
   ```


4. Crie um arquivo .env na raiz do projeto e adicione sua chave de API do Google, gerada em https://ai.google.dev/ .


    ```bash
    GOOGLE_API= Sua_Chave_Aqui
    ```


🛠️ Como Usar

 1. Inicie o servidor Flask:

    ```bash
    python app.py
    ```


2. O servidor irá escutar na porta 5000 e responder a mensagens enviadas para o webhook configurado.

3. Envie uma mensagem para o número do WhatsApp associado à API do WAHA para interagir com o chatbot.

⚙️ Estrutura do Código

O código principal do projeto é estruturado da seguinte forma:

    Flask: Utilizado para criar o servidor e gerenciar as rotas.

    Langchain: Usado para gerar respostas baseadas em prompts.

    Google Generative AI: Integração com o modelo Gemini para gerar informações nutricionais.



Sinta-se à vontade para personalizar qualquer parte do texto ou adicionar mais detalhes conforme necessário!! :D

<img src="markdown/logoIuri.svg" width="200">