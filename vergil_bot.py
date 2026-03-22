
import discord
import asyncio
from other import names
from other import bannedwords
from discord import app_commands
import random
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
mainChat = None 
chillsesh = None 


async def checkUserVoice(member):
    return member.voice and member.voice.self_mute


# for voice stuff
@client.event
async def on_voice_state_update(member, before, after):

    if member.id == names.julianID:
        if after.self_mute:
            await asyncio.sleep(180)
            if await checkUserVoice(member):
                await member.send(file=discord.File('other/vergil-vergil-dmc.gif'), content='You are muted')
    if member.id == names.brandonID:
        if after.self_mute:
            await asyncio.sleep(180)
            if await checkUserVoice(member):
                await member.send(file=discord.File('other/vergil-vergil-dmc.gif'), content='You are muted')
    if member.id == names.jacobID:
        if after.self_mute:
            await asyncio.sleep(180)
            if await checkUserVoice(member):
                await member.send(file=discord.File('other/vergil-vergil-dmc.gif'), content='You are muted')
    if member.id == names.devinID:
        if after.self_mute:
            await asyncio.sleep(180)
            if await checkUserVoice(member):
                await member.send(file=discord.File('other/vergil-vergil-dmc.gif'), content='You are muted')



# logon message
@client.event
async def on_ready():
    global mainChat, chillsesh
    print(f'We have logged in as {client.user}')
    mainChat = client.get_channel(147875019861524480)
    chillsesh = client.get_channel(147875019861524482)
    await tree.sync(guild=discord.Object(id=147875019861524480))
    print('Sync sucessful')


# for commands
@tree.command(
        name="summon",
        description="is he?",
        guild=discord.Object(id=147875019861524480)
)
async def summon(interaction):
    await interaction.response.send_message(file=discord.File('other/vergil-vergil-dmc.gif'), delete_after=10)


@tree.command(
        name="terry",
        description="templeOS",
        guild=discord.Object(id=147875019861524480)
)
async def terry(interaction):
    await interaction.response.send_message(file=discord.File('other/terry.webm'), delete_after=11)


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
        await message.channel.send(
                file=discord.File(
                    'other/Vergil_computer.jpg'),
                    content="Cringe"
                )


# For Voice Stuff
@tree.command(
        name="join",
        description="This joins a channel",
        guild=discord.Object(id=147875019861524480)
)
async def join(interaction):
    voice_files = ['other/vergilclips/vergilclips-01.mp3',
                   'other/vergilclips/vergilclips-02.mp3',
                   'other/vergilclips/vergilclips-03.mp3',
                   'other/vergilclips/vergilclips-04.mp3',
                   'other/vergilclips/vergilclips-05.mp3',
                   'other/vergilclips/vergilclips-06.mp3',
                   'other/vergilclips/vergilclips-07.mp3',
                   'other/vergilclips/vergilclips-08.mp3',
                   'other/vergilclips/vergilclips-09.mp3',
                   'other/vergilclips/vergilclips-10.mp3',
                   'other/vergilclips/vergilclips-11.mp3',
                   'other/vergilclips/vergilclips-12.mp3',
                   'other/vergilclips/vergilclips-13.mp3',
                   'other/vergilclips/vergilclips-14.mp3',
                   'other/vergilclips/vergilclips-15.mp3',
                   'other/vergilclips/vergilclips-16.mp3',
                   'other/vergilclips/vergilclips-17.mp3',
                   'other/vergilclips/vergilclips-18.mp3',
                   'other/vergilclips/vergilBadass.mp3']
    num = random.randint(0, 18)
    member = interaction.user
    sleeptime = 3
    if num == 18:
        sleeptime = 50
    if not member.voice or not member.voice.channel:
        await interaction.response.send_message("You aren't in a chat")
        return

    connection = await member.voice.channel.connect()
    connection.play(discord.FFmpegPCMAudio(executable='/usr/bin/ffmpeg',
                                           source=voice_files[num]))
    await asyncio.sleep(sleeptime)
    await connection.disconnect()


client.run(names.token)
