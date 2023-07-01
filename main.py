import discord
from key import token #importa do meu diretorio o arquivo que contem o token do meu bot
# from key import cat
import requests
import random
import json

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = token.get('TOKEN') #aloca o token do meu bot na constante TOKEN

@client.event
async def on_ready():
    print(f'{client.user} ficou online') #mensagem de quando o bot ficar online








@client.event
async def on_message(message):

    if message.author == client.user: #verificação para o bot responder somente mensagens de usuários
        return

#comando para mandar uma imagem de cachorro aleatoria no chat (Via requisição web)
    if message.content.lower() == "!dog":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image = response.json()['message']
        await message.channel.send(image)

#comando para mandar uma imagem de gatinho aleatoria no chat (Via requisição web)
    if message.content.lower() == "!cat":
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        # Faz uma requisição GET para a API TheCatAPI para obter uma imagem de gato
        json_data = response.json() # Converte a resposta da requisição em um objeto JSON
        if json_data: # Verifica se a resposta contém dados
            cat = json_data[0] # Acessa o primeiro objeto da lista de dados
            url = cat.get('url') # Obtém o valor do campo 'url' do objeto 'cat'
            await message.channel.send(url) # Envia a URL da imagem do gato no canal de mensagem do Discord
        else:
            await message.channel.send("Não foi possível obter a URL da imagem do gato.") # Envia uma mensagem informando que não foi possível obter a URL da imagem do gato

client.run(TOKEN) # inicia o Bot

