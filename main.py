import discord
from key import token #importa do meu diretorio o arquivo que contem o token do meu bot

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = token.get('TOKEN') #aloca o token do meu bot na constante TOKEN

@client.event
async def on_ready():
    print(f'{client.user} ficou online') #mensagem de quando o bot ficar online

@client.event
async def on_message(message):

    if message.author == client.user: #verificação para o bot responder somente mesnagens de usuários
        return

    if message.content.lower() == "oi":
        await message.channel.send(f'Oi {message.author}, tudo bem?')

client.run(TOKEN) # inicia o Bot

