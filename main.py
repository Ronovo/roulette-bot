# Roulette Bot
import discord
import requests
import json
import random
from discord.ext import commands
import asyncio
from itertools import cycle
import time

from discord.ext.commands import Bot

TOKEN = ''

client = discord.Client()
client: Bot = commands.Bot(command_prefix='z!')
client.remove_command('help')

gun = [0, 0, 0, 0, 0, 0]

# ---------------------------------------------------------------
# Bot Start
# --------------------------------------------------------------
# Logs Ready and sets Status at start
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name='Hi you, I\'m Dad'))


# ---------------------------------------------------------------
# Original Commands
# --------------------------------------------------------------

# Test Ping Command. Simplest Command in the bot
@client.command()
async def ping():
    await client.say('Pong!')


# Suicide
@client.command(pass_context = True)
async def suicide(ctx):
    author = ctx.message.author
    await client.say('You are about to commit Sudoku. There is no turning back')
    await client.say('You have 5 seconds to say goodbye.')
    seconds = 5
    minutes = 0.5
    counter = 0
    while counter < seconds:
        if counter is 0:
            await client.say('5')
            time.sleep(1)
        if counter is 1:
            await client.say('4')
            time.sleep(1)
        if counter is 2:
            await client.say('3')
            time.sleep(1)
        if counter is 3:
            await client.say('2')
            time.sleep(1)
        if counter is 4:
            await client.say('1')
            time.sleep(1)
        counter += 1
    await client.say("https://res.cloudinary.com/teepublic/image/private/s--xsKE16tF--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1531445013/production/designs/2885063_0.jpg")

@client.command(pass_context = True)
async def suicideKick(ctx):
    author = ctx.message.author
    await client.say('You are about to commit Sudoku. There is no turning back')
    await client.say('You have 30 seconds to say goodbye.')
    seconds = 30
    minutes = 0.5
    await asyncio.sleep(seconds)
    counter = 0
    while counter < seconds:
        if counter is 25:
            await client.say('5')
        if counter is 26:
            await client.say('4')
        if counter is 27:
            await client.say('3')
        if counter is 28:
            await client.say('2')
        if counter is 29:
            await client.say('1')
        counter += 1
    await client.kick(author)

@client.command(pass_context = True)
async def kick(ctx, userName: discord.User):
    await client.kick(userName)

@client.command(pass_context = True)
async def rouletteEasy(ctx):
    await client.say('You are about the to play Russian Roulette(Easy)')
    await client.say('*This is a No Stakes Version*')
    gun = [0, 0, 0, 0, 0, 0]
    used = []
    time.sleep(1)
    await client.say('*Gun is initialized*')
    gun[0] = 1
    time.sleep(1)
    await client.say('*Gun is Loaded*')
    gun[0] = 0
    x = random.randint(0, 5)
    gun[x] = 1
    time.sleep(1)
    await client.say('*Chamber is spun*')
    await client.say('*Type anything to start*')
    msg = await client.wait_for_message()
    msg = ""
    counter = 0
    while msg != "N" or msg != "n":
        if gun[counter] == 1:
            await client.say("https://res.cloudinary.com/teepublic/image/private/s--xsKE16tF--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1531445013/production/designs/2885063_0.jpg")
            break
        else:
            await client.say("You Survived This Round! Type N to Stop.")
            await client.say("Type anything else to continue. *Chamber will not be respun*")
            msg = await client.wait_for_message()
            counter += 1

@client.command(pass_context = True)
async def rouletteHard(ctx):
    author = ctx.message.author
    await client.say('You are about the to play Russian Roulette(Hard)')
    await client.say('*If You Lose, You Will Be Kicked From The Server*')
    await client.say('*It is suggested you send yourself an invite before you start*')
    time.sleep(1)
    gun = [0, 0, 0, 0, 0, 0]
    time.sleep(1)
    await client.say('*Gun is initialized*')
    gun[0] = 1
    time.sleep(1)
    await client.say('*Gun is Loaded*')
    gun[0] = 0
    x = random.randint(0, 5)
    gun[x] = 1
    time.sleep(1)
    await client.say('*Chamber is spun*')
    await client.say('*Type anything to start*')
    msg = await client.wait_for_message()
    msg = ""
    counter = 0
    while msg != "N" or msg != "n":
        if gun[counter] == 1:
            await client.kick(author)
            break
        else:
            await client.say("You Survived This Round! Type N to Stop.")
            await client.say("Type anything else to continue. *Chamber will not be respun*")
            msg = await client.wait_for_message()
            counter += 1



client.run(TOKEN)
