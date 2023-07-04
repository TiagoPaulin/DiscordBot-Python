import discord
from key import token #importa do meu diretorio o arquivo que contem o token do meu bot
import requests
from discord import app_commands
from discord.ext import commands 

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
# bot = commands.Bot(command_prefix='/', intents=intents)

TOKEN = token.get('TOKEN') #aloca o token do meu bot na constante TOKEN

@client.event
async def on_ready():
    print(f'{client.user} ficou online') #mensagem de quando o bot ficar online

# @client.tree.command(name="hello")
# async def hello(interaction: discord.Interaction):
#     await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)


@client.event
async def on_message(message):

    if message.author == client.user: #verificação para o bot responder somente mensagens de usuários
        return

# comando para mandar uma imagem de cachorro aleatoria no chat (Via requisição web)
    if message.content.lower() == "!dog":
        response = requests.get("https://dog.ceo/api/breeds/image/random") # Faz uma requisição GET para a API Dog CEO para obter uma imagem aleatória de cachorro
        image = response.json()['message'] # Converte a resposta da requisição em um objeto JSON e obtém o valor do campo 'message', que contém a URL da imagem
        await message.channel.send(image) # Envia a URL da imagem do cachorro no canal de mensagem do Discord

# comando para mandar uma imagem de gatinho aleatoria no chat (Via requisição web)
    if message.content.lower() == "!cat":
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        json_data = response.json() # Converte a resposta da requisição em um objeto JSON
        if json_data: # Verifica se a resposta contém dados
            cat = json_data[0] # Acessa o primeiro objeto da lista de dados
            url = cat.get('url') # Obtém o valor do campo 'url' do objeto 'cat'
            await message.channel.send(url) # Envia a URL da imagem do gato no canal de mensagem do Discord
        else:
            await message.channel.send("Não encontrei nenhum gatinho </3)") # Envia uma mensagem informando que não foi possível obter a URL da imagem do gato

# menu de comandos 
    if message.content.lower() == "!help":
        await message.channel.send(f"Olá, {message.author.name} estes são meus comandos\n1- !cat para você ver um gatinho\n2- !dog para você ver um cachorrinho")

client.run(TOKEN) # inicia o Bot

