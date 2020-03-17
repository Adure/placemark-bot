import discord
from discord.ext import commands
from auth import token, riot_dev_token
import aiohttp

bot = commands.Bot(command_prefix='!')

RIOT_API = "https://oc1.api.riotgames.com"

#Implement algo to determine if an account is an egirl or not
@bot.command()
async def egirl(ctx, name):
    async with aiohttp.ClientSession() as session:
        #Riot API application for auth pending
        async with session.get(f"{RIOT_API}/lol/summoner/v4/summoners/by-name/{name}", headers={"X-Riot-Token": riot_dev_token}) as resp:
            playerId = await resp.json()
        async with session.get(f"{RIOT_API}/lol/champion-mastery/v4/champion-masteries/by-summoner/{playerId['id']}", headers={"X-Riot-Token": riot_dev_token}) as resp:
            data = await resp.json()

    print(data)
	
#Implement algo to determine if an account is a onetrick or not
@bot.command()
async def onetrick(ctx, name):
    pass

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
	
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.content)

bot.run(token)
