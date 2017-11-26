import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot_prefix= "."
client = commands.Bot(command_prefix=bot_prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))

@client.command(pass_context=True)
async def ping(ctx):
    await client.say("Pong!")

@client.command(pass_context=True)
async def laba(ctx):
    await client.say("Trista")

@client.command(pass_context=True)
async def cristina(ctx):
    await client.say("Met crede ca-s muista")

@client.command(pass_context=True)
async def matt(ctx):
    await client.say("Met este nablet")

@client.command(pass_context=True)
async def beata(ctx):
    await client.say("Is beata omule :heart:")

@client.command(pass_context=True)
async def sex(ctx):
    await client.say(" :middle_finger: ")

@client.command(pass_context=True)
async def indian(ctx):
    await client.say(" SEND NUDES :heart_eyes_cat:  ")

@client.command(pass_context=True)
async def pula(ctx):
    await client.say("Am pula cat un T-Rex")

@client.command(pass_context=True)
async def nervoasa(ctx):
    await client.say(" CALM YOUR TITIES FA :angry:   ")

@client.command(pass_context=True)
async def suc(ctx):
    await client.say("la miss si mister")

@client.command(pass_context=True)
async def tocuri(ctx):
    await client.say("1.62 hm suna bine")

@client.command(pass_context=True)
async def vise(ctx):
    await client.say("1.62 hm suna bine")

@client.command(pass_context=True)
async def popcorn(ctx):
    await client.say("https://imgur.com/a/E15e2")

@client.command(pass_context=True)
async def engleza(ctx):
    await client.say("https://imgur.com/a/9zfDr")

@client.command(pass_context=True)
async def nuba(ctx):
    await client.say("https://prnt.sc/goqfbo")
	
@client.command(pass_context=True)
async def bubz(ctx):
    await client.say("https://cdn.discordapp.com/attachments/262946424034033674/371006437922439180/unknown.png")
	
@client.command(pass_context=True)
async def bubz2(ctx):
    await client.say("https://imgur.com/a/8AEYi")
	
@client.command(pass_context=True)
async def marelecanion(ctx):
    await client.say("https://imgur.com/a/p8QZi")
	
@client.command(pass_context=True)
async def dildo(ctx):
    await client.say("https://imgur.com/a/stEqL")

@client.command(pass_context=True)
async def nudes(ctx):
    await client.say("https://imgur.com/a/ef1CA")    
    
client.run("MzU5NzI5MjY2OTIyODgxMDM3.DKLciw.O_nhcQ0gdEQ_S8eiB_eh6KArygU")
