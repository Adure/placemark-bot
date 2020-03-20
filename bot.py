import discord
from discord.ext import commands
from auth import token, app_token
from champions import get_champs_dict
import aiohttp
champs = get_champs_dict()

bot = commands.Bot(command_prefix='!')

RIOT_API = "https://oc1.api.riotgames.com"

async def summoner_name_to_id(name, session):
    async with session.get(f"{RIOT_API}/lol/summoner/v4/summoners/by-name/{name}", headers={"X-Riot-Token": app_token}) as resp:
        playerId = await resp.json()
        return playerId['id']

#Implement algo to determine if an account is an egirl or not
@bot.command()
async def egirl(ctx, name):
    async with aiohttp.ClientSession() as session:
        playerId = await summoner_name_to_id(name, session)
        async with session.get(f"{RIOT_API}/lol/champion-mastery/v4/champion-masteries/by-summoner/{playerId}", headers={"X-Riot-Token": app_token}) as resp:
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
    print(message.content)
    await bot.process_commands(message)

bot.run(token)
