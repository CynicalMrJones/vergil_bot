
import discord
import asyncio
from other import names
from other import bannedwords
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
mainChat = client.get_channel(147875019861524480)
chillsesh = client.get_channel(147875019861524482)


async def checkUserVoice(userID):
    return userID.voice.self_mute


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

    if not before.channel and after.channel and member.id == names.reggieID and before.self_mute:
        await mainChat.send(content="REGGIE, HOW DO YOU JOIN MUTED EVERY TIME")


# logon message
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
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
                file=discord.File('other/Vergil_computer.jpg'),
                content="Cringe"
                )


@tree.command(
        name="join",
        description="This joins a channel",
        guild=discord.Object(id=147875019861524480)
)
async def join(interaction):
    member = interaction.user
    test = await member.voice.channel.connect()
    test.play(discord.FFmpegPCMAudio(executable='/usr/bin/ffmpeg', source='other/vergil_voice.mp3'))
    await asyncio.sleep(7)
    await test.disconnect()


client.run(names.token)
