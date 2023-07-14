from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.get("/callAI")
def callAI():
    args = request.args
    question = str(args.get('q'))
    return callAIService(question)

def callAIService(question):
    print("Calling AI program with question: " + question)
    url = 'https://us-central1-aiplatform.googleapis.com/v1/projects/hack-team-tradeai/locations/us-central1/publishers/google/models/codechat-bison@001:predict'

    restBody = {
        'instances': [
            {
                'messages': [
                    {
                        'author': 'user',
                        'content': question
                    }
                ]
            }
        ],
        'parameters': {
            'temperature': 0.2,
            'maxOutputTokens': 1024
        }
    }

    response = requests.post(url, json=restBody, headers={
        'Authorization': 'Bearer ya29.a0AbVbY6MHAdSNtwwoJFhqP0vqnJ26bHyJN3OuU99pZ1U5usgXmyO-TJ7MK1RP3y9qHWHPsZO5nsRzodhUFt1eqIMrLw6gfe6jFAn5BRJMqRbv7EQhMyMW4-I2A-HpJfLO5M4UjrGg8xZmExzb9bRMGngk3TTqhDSokI5isC-ZRUBQ6v-oyn7Uitf8wufWsHdEt4QINro9UeL5nSpZh2Z_MKa8pbltFZl3x5YEzrjary5mrvMX2mfUSD7lsssSEOKK4Qar5mOzlQnLVoQm1MYrOjOcRFW_ExSGVS4K6VacNXQBSvoNTOGu4Yip877lwWLJnrRc5-8zk2QUHIb8Z2B8AvyT7MFyjKO7pOxhaT8brZPZBitpRULQpOzHak7Qjwg93ByRYbgumvc173YlodwPRaLVaCgYKAbYSARMSFQFWKvPlRsF2Wz_42Oa_h5Ye249ryg0415',
        'Content-Type': 'application/json'})

    data = response.json()
    response = data['predictions'][0]['candidates'][0]['content']
    print("Answer from AI: " + response)

    return response
