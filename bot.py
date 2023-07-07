import discord
import requests
from discord import app_commands
from discord.ext import commands
from key import token

TOKEN = token.get('TOKEN') # importa o token do bot presente no arquivo "key"

intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix = "!", intents = intents)

# Função de inicialização
@bot.event
async def on_ready():
    print(f'{bot.user} ficou online')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

# Função de mensagem de boas vindas no servidor
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1110730791056576624) # definindo o canal em que a mensagem sera enviada pelo ID do canal
    await channel.send(f"Bem-vindo {member.mention}! Posso gerar imagens de bichinhos para você, Aproveite!! <3") # mensagem de boas vindas

# Comando de enviar fotos de gatos no chat
@bot.tree.command(name = "cat")
async def cat(interaction: discord.Interaction):
        response = requests.get("https://api.thecatapi.com/v1/images/search") # requisição web para uma API de gatos
        if response: # Verifica se a resposta contém dados
            json_data = response.json() # Converte a resposta da requisição em um objeto JSON
            cat = json_data[0] # Acessa o primeiro objeto da lista de dados
            image = cat.get('url') # Obtém o valor do campo 'url' do objeto 'cat'
            await interaction.response.send_message(image, ephemeral = False) # Envia a URL da imagem do gato no canal de mensagem do Discord
        else:
            await interaction.response.send_message("Não encontrei nenhum gatinho </3)", ephemeral = False) # Envia uma mensagem informando que não foi possível obter a URL 

# Comando de enviar fotos de cachorros no chat
@bot.tree.command(name = "dog")
async def dog(interaction: discord.Interaction):
        response = requests.get("https://dog.ceo/api/breeds/image/random") # requisição web para uma API de cachorros
        if response:
            image = response.json()['message'] # Converte a resposta da requisição em um objeto JSON e obtém o valor do campo 'message', que contém a URL da imagem
            await interaction.response.send_message(image, ephemeral = False) # Envia a URL da imagem do cachorro no canal de mensagem do Discord
        else:
            await interaction.response.send_message("Não encontrei nenhum cachorrinho </3") # Envia uma mensagem informando que nao foi possivel obter a URL

# Comando de enviar fotos de raposa no chat
@bot.tree.command(name = "fox")
async def fox(interaction: discord.Interaction):
    response = requests.get("https://randomfox.ca/floof")
    if response:
        json_data = response.json() # Converte a resposta da requisição em um objeto JSON
        image = json_data.get('image') # Obtém o valor do campo 'image' do objeto 'json'
        await interaction.response.send_message(image, ephemeral = False) # Envia a URL da imagem da raposa no canal de mensagem do Discord
    else:
        await interaction.response.send_message("Não encontrei nenhuma raposa </3") # Envia uma mensagem informando que nao foi possivel obter a URL

# Comando de enviar fotos de pato no chat
@bot.tree.command(name = "duck")
async def duck(interaction: discord.Interaction):
        response = requests.get("https://random-d.uk/api/random") # requisição web para uma API de patos
        if response: # Verifica se a resposta contém dados
            json_data = response.json() # Converte a resposta da requisição em um objeto JSON
            image = json_data['url'] # Obtém a URL da foto do pato a partir da resposta da API
            await interaction.response.send_message(image, ephemeral = False) # Envia a URL da imagem do pato no canal de mensagem do Discord
        else:
            await interaction.response.send_message("Não encontrei nenhum patinho </3)", ephemeral = False) # Envia uma mensagem informando que não foi possível obter a URL 

# Comando que informa a utilidade do bot
@bot.tree.command(name = "about")
async def about(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá, {interaction.user.name} Consigo gerar imagens de bichinhos para você!! Aproveite", ephemeral = False) # Envia a mensagem no chat

bot.run(TOKEN) # inicializa o bot