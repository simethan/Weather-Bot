
    """IMPORT STUFF HERE"""
import discord
import cmath
from discord.ext import commands
from discord import Permissions
from discord.utils import get
import asyncio
import json
import locale
import time
import requests
from datetime import date
from requests import get
from json import loads, dump
import datetime
from json.decoder import JSONDecodeError
import sched, time
locale.setlocale(locale.LC_ALL, 'en_US')

token = "UR-BOT-TOKEN-HERE"
client = commands.Bot(command_prefix = '/')
client.remove_command("help")
game = discord.Game("with the weather?!")

    """LOGGING STUFF HERE"""
    
@client.event  
async def on_ready():  
    print(f'We have logged in as {client.user}')  
    print()
    print("Discord.py Version " + discord.__version__)
    print()
    await client.change_presence(activity = game)  
        
@client.event
async def on_message(message):
    print()
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    await client.process_commands(message)
    
    """COMMAND STUFF HERE"""
    
@client.command()
async def weather(ctx,*,phrase=None):

    today = str(date.today())
    URL = requests.get(f"https://api.data.gov.sg/v1/environment/24-hour-weather-forecast?date={today}")
    URLJSON = URL.json()
    t = datetime.datetime.now()
    tt = t.strftime("%H:%M:%S")
    
    forecast = URLJSON["items"][0]["general"]["forecast"]
    high_hum = URLJSON["items"][0]["general"]["relative_humidity"]["high"]
    low_hum = URLJSON["items"][0]["general"]["relative_humidity"]["low"]
    high_temp = URLJSON["items"][0]["general"]["temperature"]["high"]
    low_temp = URLJSON["items"][0]["general"]["temperature"]["low"]
    avatar = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url
    
    weatherembed = discord.Embed(title ="24 Hour Weather Forecast",description =f"Forecast: {forecast}", color=0xFFF8E7 )
    weatherembed.add_field(name="Highest/Lowest Temperature",value=f"{high_temp}°C / {low_temp}°C", inline = False)
    weatherembed.add_field(name="Highest/Lowest Humidty",value=f"{high_hum}% / {low_hum}%", inline = False)
    weatherembed.set_footer(icon_url = avatar, text=f" Requested By: {ctx.message.author} | Today At: {tt}")
    
    await ctx.send(embed=weatherembed)
    await ctx.message.delete()
    
@client.command()
async def w(ctx,*,prhase=None):

    today = str(date.today())
    URL = requests.get(f"https://api.data.gov.sg/v1/environment/4-day-weather-forecast?date={today}")
    URL3JSON = URL.json()
    t = datetime.datetime.now()
    tt = t.strftime("%H:%M:%S") 


    for days in range(len(URL3JSON["items"][0]["forecasts"])):
    
        date2 = URL3JSON["items"][days]["forecasts"][days]["date"]
        forecast = URL3JSON["items"][days]["forecasts"][days]["forecast"]
        high_hum = URL3JSON["items"][days]["forecasts"][days]["relative_humidity"]["high"]
        low_hum = URL3JSON["items"][days]["forecasts"][days]["relative_humidity"]["low"]
        high_temp = URL3JSON["items"][days]["forecasts"][days]["temperature"]["high"]
        low_temp = URL3JSON["items"][days]["forecasts"][days]["temperature"]["low"]
        avatar = ctx.message.author.avatar_url or ctx.message.author.default_avatar_url
        weatherembed = discord.Embed(title =f"On {date2}",description=f"Forecast: {forecast}", color=0xFFF8E7 )
        weatherembed.add_field(name="Highest/Lowest Temperature",value=f"{high_temp}°C / {low_temp}°C", inline = False)
        weatherembed.add_field(name="Highest/Lowest Humidty",value=f"{high_hum}% / {low_hum}%", inline = False)
        weatherembed.set_footer(icon_url = avatar, text=f" Requested By: {ctx.message.author} | Today At: {tt}")
        
        await ctx.send(embed=weatherembed)

    await ctx.message.delete()
    
    """RUN THE BOT LOL"""
    
    client.run(token)
