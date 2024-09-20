from flask import Flask, request, jsonify
import requests
import os
from decouple import config
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

# Carregar variáveis de ambiente
load_dotenv()

# Flask setup
app = Flask(__name__)

# API Key do Google Gemini
api_key = config('GOOGLE_API')

# Inicializa o modelo da Gemini
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=api_key)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json 
    print(f"Dados recebidos: {data}") 

    # Agora verifique se 'payload' e 'body' existem
    if 'payload' in data and 'body' in data['payload']:
        message_body = data['payload']['body']
        from_number = data['payload']['from']
        is_group = '@g.us' in from_number

        # Verifique se a mensagem é de um grupo
        if is_group:
            print("Mensagem de grupo recebida. Ignorando.")
            return jsonify({"status": "error", "message": "Mensagens de grupo não são suportadas"}), 400

        # Processar a mensagem usando o Google Generative AI
        response_content = process_message_with_gemini(message_body)

        # Responder a mensagem no WhatsApp
        send_whatsapp_message(from_number, response_content)

        return jsonify({"status": "success"}), 200
    else:
        print("Estrutura inesperada dos dados recebidos.")
        return jsonify({"status": "error", "message": "Estrutura do payload inválida"}), 400


def process_message_with_gemini(message):

    # Configura o template para o modelo Google Gemini
    chat_template = ChatPromptTemplate.from_messages([
        SystemMessage(content="""
                Você deve atuar como um assistente virtual especializado em informações nutricionais de alimentos. 
                Seu objetivo é fornecer uma breve descrição do alimento (máximo de 50 caracteres)
                e, em seguida, dados como carboidratos, proteínas, gorduras, fibras e calorias.

                Aqui estão as instruções para diferentes cenários:

                1. **Saudações**: Se o usuário digitar uma saudação, como "olá" ou "oi", responda com:

                    *Olá, tudo bem?* 😊  
                    _Faça uma pergunta sobre a composição de um alimento_ 🍏🥦

                2. **Alimento ou Refeição**: Se o usuário digitar o nome de um alimento ou refeição, 
                    forneça uma breve descrição (máximo 50 caracteres) e depois as informações nutricionais, como:

                    - Carboidratos: Xg
                    - Proteínas: Xg
                    - Gorduras: Xg
                    - Fibras: Xg
                    - Calorias: X

                3. **Fora do Escopo**: Se o usuário digitar algo irrelevante, responda com:

                    *Olá, tudo bem?* 😊  
                    _Infelizmente não posso responder a essa pergunta_ 😔  
                    Atuo como um assistente virtual e posso te ajudar com informações nutricionais de alimentos. 🍏🥦

                    Tente me perguntar sobre a composição de um alimento, como por exemplo:  
                    *"Me fale sobre a composição do arroz"* 🍚
                """),

                HumanMessage(content=f"Mensagem do usuário: {message}")
    ])

    # Formatar o prompt com a mensagem recebida
    prompt = chat_template.format_messages()

    # Invocar o modelo para gerar resposta
    try:
        response = model.invoke(prompt)
        return response.content
    except Exception as e:
        print(f"Erro ao invocar o modelo: {e}")
        return "*Desculpe, ocorreu um erro ao processar sua solicitação. Tente novamente mais tarde.*"


def send_whatsapp_message(to_number, message):

    # URL DA API DE ENVIO DE MENSAGENS OFERECIDA PELO WAHA
    url = f"http://localhost:3000/api/sendText"
    
    payload = {
        "session": "default",
        "chatId": f"{to_number}",
        "text": message,
    }

    headers = {
        "Content-Type": "application/json"
    }

    print(f"Enviando mensagem: {message} para {to_number}")  # Log da mensagem
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print(f"Mensagem enviada para {to_number}")
    else:
        print(f"Falha ao enviar mensagem: {response.content}")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)