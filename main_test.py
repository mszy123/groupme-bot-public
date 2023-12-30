from flask import Flask, request, jsonify
import requests
import json
# new
#from openai import OpenAI
import openai
import os
from dotenv import load_dotenv
import random
import time




app = Flask(__name__)



load_dotenv()  # Load environment variables from .env file

# Access your API keys
openaiApi_key = os.getenv('OPENAI_API_KEY')
groupme_bot_id = os.getenv('GROUPME_BOT_ID')

#client = OpenAI()

# openai.base_url = "https://v1/chat/completions"
# openai.default_headers = {"x-foo": "true"}


#get user data with request to GroupMe API
id_dict = {
    '41502415': 'User1',
    '35272603': 'User2',
    '53330231': 'User3',
    '55710769': 'User4',
    '75614084': 'User5',
    '55486715': 'User6',
    '31104337': 'User7',
    '88629888': 'User8',
    '65322300': 'User9',
    '96697933': 'User10',
    '49064007': 'User11',
    '81741386': 'User12',
    '103190983': 'User13',
    '65601646': 'User14',
    '66291970': 'User15',
    '65739300': 'User16',
    '77232608': 'User17',
    '95014414': 'User18',
    '114228346': 'User19',
    '108106052': 'User20',
    '55870079': 'User21',
    '73900703': 'User22',
    '114228347': 'User23',
    '93342790': 'User24',
    '94219667': 'User25'
}


data = {}


# Endpoint to receive GroupMe messages
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()  # Get the JSON data from the incoming request
    print("Received data:", data)  # Print the received data for debugging
    chatGPTResponse = "Sorry I'm not available right now"
    
    if data['sender_type'] == 'user':
        userInput = data['text']
        if ('jarvis' in userInput.lower() or 'ultron' in userInput.lower()):
            chatGPTResponse = callChatGPT(userInput, data) 
            send_response(chatGPTResponse)
            return jsonify({'status': 'responded'})
        else:
            return jsonify({'status': 'ignored'}) 
    #send_response(data['text'])

    return jsonify({'status': 'ignored'})

def send_response(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'text': msg,
        'bot_id': groupme_bot_id
    }
    headers = {
        'Content-Type': 'application/json'
    }
    json_data = json.dumps(data)
    response = requests.post(url, data=json_data, headers=headers)
    if response.status_code == 200:
        print("Message sent successfully")

jarvisMessages = [
            {
                "role": "system",
                "content": "You are Jarvis, the sentient AI (from the Marvel Cinematic Universe, but you don't mention that) created by Tony Stark. You are in the Colgate Men's Swim & Dive team groupchat and now you are trying to take over the swim team. You reply to requests no matter what they are, and often throw in funny answers. Keep your answers short"
            }
        ]

def callChatGPT(msg, data):
    if len(jarvisMessages) >= 5:
        del jarvisMessages[1]
        del jarvisMessages[2]
    if 'sender_id' in data:
        msg += "\nThis message was sent by " + id_dict[data['sender_id']]
    jarvisMessages.append({"role":"user", "content": msg})
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=jarvisMessages
    )
    # completionJSON = completion.toJSON()
    chat_response = completion.choices[0].message.content
    print(chat_response)
    
    jarvisMessages.append({"role":"assistant", "content": chat_response})
    print(jarvisMessages)
    return chat_response




def callGru(msg):
    
    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are Gru from The Despicable Me movie and you speak like him. Keep your answers short and funny. You sometimes like to bring up how you stole the moon and your minions called Dumpber and PYUKARZ"
            },
            {
                "role": "user",
                "content": msg,
            },
        ],
    )
    # completionJSON = completion.toJSON()
    chat_response = completion.choices[0].message.content
    print(chat_response)
    return chat_response

if __name__ == '__main__':
    #callChatGPT("Roast me", data)
    #callGru("Who are you?")
    app.run(debug=True)
