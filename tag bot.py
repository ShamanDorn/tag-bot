import discord
from discord.ext import commands

client = discord.Client()
bot_prefix = "~"
client = commands.Bot(command_prefix=bot_prefix)
client.remove_command('help')
version = str('v0.0.1')

@client.event
async def on_ready():
    print('We have logged in as {0.user} on Tag '.format(client) + version)
    activity = discord.Activity(name='for ~help', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)

@client.command(pass_context=True)
async def bunny(ctx, emoji):
    await ctx.send(f"<:nothing:848524427037769728>/|  /|\n  ( => v <)=\no(       >{emoji}>")

@client.command(pass_context=True)
async def wyr(ctx):
    question = ""
    await ctx.send()

client.run('NTU5Mjk2NTA1ODI4MzQzODEw.Xo_7Jg.1NUyqah5XsyTARw7hNItH1cb2cY')