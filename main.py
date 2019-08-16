# roulette-bot
import discord
import random
from discord.ext import commands
import asyncio
import time

from discord.ext.commands import Bot

TOKEN = ''

client = discord.Client()
client = commands.Bot(command_prefix='t!')
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


# ---------------------------------------------------------------
# Original Commands
# --------------------------------------------------------------

# Test Ping Command. Simplest Command in the bot
@client.command()
async def ping():
    await client.say('Pong!')


# Command to Kick Yourself from discord
@client.command(pass_context=True)
async def suicide(ctx, msg="real"):
    author = ctx.message.author
    await client.say('You are about to commit Sudoku. There is no turning back')
    if msg.lower() == "real":
        await client.say('You will be kicked from the server. It is suggested to invite yourself back now')
    await client.say('You have 30 seconds to say goodbye.')
    seconds = 30
    counter = 0
    while counter < seconds:
        if counter is 26:
            await client.say('5')
            time.sleep(1)
        if counter is 27:
            await client.say('4')
            time.sleep(1)
        if counter is 28:
            await client.say('3')
            time.sleep(1)
        if counter is 29:
            await client.say('2')
            time.sleep(1)
        if counter is 30:
            await client.say('1')
            time.sleep(1)
        counter += 1

    if msg.lower() == "fake":
        await client.say("https://res.cloudinary.com/teepublic/image/private/s--xsKE16tF--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1531445013/production/designs/2885063_0.jpg")
    elif msg.lower() == "Real":
        await client.kick(author)
    else:
        await client.say("https://res.cloudinary.com/teepublic/image/private/s--xsKE16tF--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1531445013/production/designs/2885063_0.jpg")

#Command to play Russian Roulette
@client.command(pass_context = True)
async def roulette(ctx, msg="Easy"):
    author = ctx.message.author
    await client.say('You are about the to play Russian Roulette(%s)' % msg)
    await client.say('*If you are on Medium or Higher, You can be kicked or banned!*')
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

    if msg.lower() != "easy":
        await client.say('*You are advised to send yourself an invite now*')
    userinput = await client.wait_for_message()
    userinput = ""
    counter = 0
    stringmessage = ""
    stringmessage = str(msg)
    while userinput.lower() != "n":
        if gun[counter] == 1:
            if stringmessage.lower() == "medium":
                await client.kick(author)
            elif stringmessage.lower() == "hard":
                await client.ban(author)
            elif stringmessage.lower() == "legendary":
                await client.ban(author, 7)
            else:
                await client.say(
                    "https://res.cloudinary.com/teepublic/image/private/s--xsKE16tF--/t_Preview/b_rgb:191919,c_limit,f_jpg,h_630,q_90,w_630/v1531445013/production/designs/2885063_0.jpg")
                break
        else:
            await client.say("You Survived This Round! Type N to Stop.")
            await client.say("Type anything else to continue. *Chamber will not be respun*")
            msg = await client.wait_for_message()
            counter += 1

# ---------------------------------------------------------------
# Help Function
# --------------------------------------------------------------
@client.command(pass_context=True)
async def help(ctx, msg="help"):
    author = ctx.message.author
    if msg == "help":
        embed = discord.Embed(
            colour=discord.Colour.orange()
        )
        embed.set_author(name='Help')
        embed.add_field(name='z!roulette', value='Play Russian Roulette (No Kick Version)',inline=False)
        embed.add_field(name='z!roulette (difficulty)', value='Play Russian Roulette (Kick Version)', inline=False)
        embed.add_field(name='Dificulties', value='------------------------------', inline=False)
        embed.add_field(name='Easy', value='Default, if z!roulette is entered. Returns Picture upon loss', inline=False)
        embed.add_field(name='Medium', value='Kicks you from Server upon loss (You Can instantly Rejoin)', inline=False)
        embed.add_field(name='Hard', value='Bans you for 1 day upon loss', inline=False)
        embed.add_field(name='Legendary', value='Lifetime Ban upon loss(Must be reinstated by admin)', inline=False)
        embed.add_field(name='Other Commands', value='------------------------------', inline=False)
        embed.add_field(name='z!suicide', value='Give you 30 seconds before killing you (Kick Version)',
                        inline=False)
        embed.add_field(name='z!suicide fake', value='Give you 30 seconds before killing you (No Kick Version)', inline=False)
        await client.say(embed=embed)
        # await client.send_message(author, embed=embed)


client.run(TOKEN)
