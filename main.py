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

    # if message.content.lower() == "!gatinho": 
    #     await message.channel.send(f'Oi {message.author}, ainda sem gatinhos')

# comando para mandar uma imagem de gatinho aleatoria no chat (somente imagens salvas em "cats")
    if message.content.lower() == "!cat":
        number = random.randint(1,10)
        file_path = f'cats/gato_icon{number}.jpg'
        # Envia a imagem como anexo
        with open(file_path, 'rb') as file:
            await message.channel.send(file=discord.File(file))

#comando para mandar uma imagem de cachorro aleatoria no chat (Faz uso de uma API)
    if message.content.lower() == "!dog":
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        image = response.json()['message']
        await message.channel.send(image)

    if message.content.lower() == "!teste":
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        json_data = response.json()
        
        if json_data:  # Verifica se a resposta contém dados
            cat = json_data[0]
            url = cat.get('url')
            await message.channel.send(url)
        else:
            await message.channel.send("Não foi possível obter a URL da imagem do gato.")
client.run(TOKEN) # inicia o Bot

