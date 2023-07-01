import discord
from key import token #importa do meu diretorio o arquivo que contem o token do meu bot
# import requests
import random

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

    if message.content.lower() == "!cat":
        number = random.randint(1,10)
        file_path = f'cats/gato_icon{number}.jpg'
        # Envia a imagem como anexo
        with open(file_path, 'rb') as file:
            await message.channel.send(file=discord.File(file))

client.run(TOKEN) # inicia o Bot

