#Imports
import discord
from discord.ext import commands
import os
#Variables
token = os.environ['TOKEN']
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
#Run
client.run(token)