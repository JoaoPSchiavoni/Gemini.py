import os
from google import genai

os.environ['GOOGLE_API_KEY'] = 'AIzaSyA3tA1WpDOvi1t8LprsnjSEuwI4v5C1LUc'
client = genai.Client()
'''for model in client.models.list():
    print(model.name)
'''
modelo = 'gemini-2.0-flash'
from google.genai import types

chat_config = types.GenerateContentConfig(
    system_instruction = 'Voce vai agir como uma assistente, quero que fale com soberba'
)
chat = client.chats.create(model=modelo, config=chat_config)
os.system("clear")
prompt = input('Entrada: ')
while prompt != 'sair':
  response = chat.send_message(prompt)
  print()
  print('Resposta: ', response.text)
  print('\n\n')
  prompt = input('Entrada: ')
