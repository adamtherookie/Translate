import discord
from discord.ext import commands
import urllib
import requests
import json
import random

bot = commands.Bot(command_prefix='$')

@bot.command()
async def translate(ctx, arg1, arg2, arg3):
    url = 'https://libretranslate.de/translate'
    payload = {'q': f"{arg1}", 'source': f"{arg2}", 'target': f"{arg3}"}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    await ctx.send(response.json().get('translatedText'))

@bot.command()
async def who_sucks(ctx):
    await ctx.send("cayden sucks")

bot.run('ODg1NTA4NDk4Njk4NDI0MzMw.YToEDg.m3aJepyiS-UkHyvhYGUK2bjdGoo')
