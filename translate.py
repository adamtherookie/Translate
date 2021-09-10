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
async def detect(ctx, arg1):
    url = 'https://libretranslate.de/detect'
    payload = {'q': f"{arg1}"}
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    await ctx.send('"' + arg1 + '"' + ' is most likely in ' + response.json()[0].get('language') + ' (confidence: ' + str(response.json()[0].get('confidence')) + ')')

bot.run('TOKEN HERE')
