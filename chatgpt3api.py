import requests
import json
from matrix import *

API_KEY = "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"
API_URL = "https://api.openai.com/v1/chat/completions"

def get_chatbot_response(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "messages":[{'role': 'user', 'content': prompt}],
        "model": "gpt-3.5-turbo",        
        
    }

    response = requests.post(API_URL, headers=headers, data=json.dumps(data))
    response_json = json.loads(response.content)

    return response_json['choices'][0]['message']['content']
                

prompt = f"give me an instruction by following text: {result}"

response = get_chatbot_response(prompt)
print("Chatbot:", response)
