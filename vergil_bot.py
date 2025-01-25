# This example requires the 'message_content' intent.

import discord
import asyncio
import names
import bannedwords 

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


async def checkuser(userID):
    return userID.voice.self_mute


# for voice stuff
@client.event
async def on_voice_state_update(member, before, after):
    if member.id == names.julianID:
        if after.self_mute:
            print('Julian is muted')
            await asyncio.sleep(180)
            if await checkuser(member):
                await member.send('You are muted')
    if member.id == names.brandonID:
        if after.self_mute:
            print('Brandon is muted')
            await asyncio.sleep(180)
            if await checkuser(member):
                await member.send('You are muted')
    if member.id == names.jacobID:
        if after.self_mute:
            print('Jacob is muted')
            await asyncio.sleep(180)
            if await checkuser(member):
                await member.send('You are muted')
    if member.id == names.devinID:
        if after.self_mute:
            print('Devin is muted')
            await asyncio.sleep(180)
            if await checkuser(member):
                await member.send('You are muted')

    if not before.channel and after.channel and member.id == names.reggieID and before.self_mute:
        print('REGGIE HOW DO YOU JOIN MUTED EVERYTIME')


# logon message
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


async def checkDictCringe(str):
    dic = bannedwords.bannedwords
    for word in dic:
        if word in str.lower():
            return True
    return False


# This is for messages
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif await checkDictCringe(message.content):
        await message.channel.send("Cringe")


client.run(names.token)
