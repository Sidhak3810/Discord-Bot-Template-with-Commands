#Imports
import discord
from discord.ext import commands
import os
import json
import requests
#Definations
token = os.environ['TOKEN']
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a'] +"   " + "Quotes given by https://zenquotes.io"
  return(quote)
  
#Client
client = commands.Bot(command_prefix="!")
#StartUp
@client.event
async def on_ready():
  print("I am ready!")
#Commands
@client.command()
async def ping(ctx):
  latency = round(client.latency * 1000)
  await ctx.reply(f"Pong! My ping from the server to Discord is `{latency}`ms")
@client.command()
async def inspire(ctx):
  quote = get_quote()
  await ctx.reply(quote)
#Run
client.run(token)