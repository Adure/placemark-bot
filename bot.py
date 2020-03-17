import discord
from discord.ext import commands
from auth import token

bot = commands.Bot(command_prefix='!')

#Implement algo to determine if an account is an egirl or not
@bot.command()
async def egirl(ctx, name):
    pass
	
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
    print(message)

bot.run(token)
