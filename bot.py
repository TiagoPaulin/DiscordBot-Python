import discord
import requests
from discord import app_commands
from discord.ext import commands
from key import token

TOKEN = token.get('TOKEN')

bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print("O botbichinhos esta online")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.tree.command(name = "cat")
async def cat(interaction: discord.Interaction):
        response = requests.get("https://api.thecatapi.com/v1/images/search") # requisição web para uma API de gatos
        json_data = response.json() # Converte a resposta da requisição em um objeto JSON
        if json_data: # Verifica se a resposta contém dados
            cat = json_data[0] # Acessa o primeiro objeto da lista de dados
            url = cat.get('url') # Obtém o valor do campo 'url' do objeto 'cat'
            await interaction.response.send_message(url, ephemeral = False) # Envia a URL da imagem do gato no canal de mensagem do Discord
        else:
            await interaction.response.send_message("Não encontrei nenhum gatinho </3)") # Envia uma mensagem informando que não foi possível obter a URL da imagem do gato

@bot.tree.command(name = "dog")
async def dog(interaction: discord.Interaction):
        response = requests.get("https://api.thecatapi.com/v1/images/search") # requisição web para uma API de gatos
        json_data = response.json() # Converte a resposta da requisição em um objeto JSON
        if json_data: # Verifica se a resposta contém dados
            cat = json_data[0] # Acessa o primeiro objeto da lista de dados
            url = cat.get('url') # Obtém o valor do campo 'url' do objeto 'cat'
            await interaction.response.send_message(url, ephemeral = False) # Envia a URL da imagem do gato no canal de mensagem do Discord
        else:
            await interaction.response.send_message("Não encontrei nenhum gatinho </3)") # Envia uma mensagem informando que não foi possível obter a URL da imagem do gato

bot.run(TOKEN)