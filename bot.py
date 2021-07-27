import discord
from discord.ext import commands
from discord import colour
from discord.embeds import Embed
import datetime
import random
import asyncio
import os
client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    print("봇 켜짐")
    print(client.user)
    print("======")
    game = discord.Game("무야호잇!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "야":
        await message.channel.send("왜")
    if message.content == "ㅎㅇ":
        await message.channel.send("ㅂㅇ")
    
    if message.content == "!도움":
        embed = discord.Embed(colour=discord.Colour.blue(), title = "둘리봇이라고 합니다", description="잘 부탁드려요")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        
        embed.add_field(name="!내정보", value="서버 가입일을 알려줍니다", inline=False)
        embed.add_field(name="!청소 <수>", value="수 만큼의 메시지를 삭제합니다", inline=False)
        embed.add_field(name="!타이머 <n초>", value="n초만큼 타이머를 작동합니다", inline=False)
        embed.add_field(name="!채널 <보낼 채널 ID> <보낼 내용>", value="보낼 채널에 메시지가 보내집니다", inline=False)
        await message.channel.send(embed=embed)

    if message.content.startswith(f"!채널"):
        ch = client.get_channel(int(message.content[4:22]))
        await ch.send(message.content[23:])

    if message.content == "!내정보":
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000)/ 1000)
        embed = discord.Embed(colour=discord.Colour.blue(), title = f"{user.display_name}님의 정보")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="가입일", value=f"{user.display_name}의 가입일 : {date.year}/{date.month}/{date.day}", inline=False)
        await message.channel.send(embed=embed)
    
    if message.content.startswith("!타이머"):
        time = int(message.content[5:])
        print("타이머 시작")
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="타이머를 {0}초간 작동할게요".format(time), value="이따 봐요!")
        await message.channel.send(embed=embed)
        await asyncio.sleep(time)
        embed = discord.Embed(colour=discord.Colour.blue(), title = "타이머",)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/866815123586547712/866815175931985930/00a2b4db95d21fa6.PNG")
        embed.add_field(name="{0}초가 지났어요!".format(time), value="다음에 또 이용해주세요")
        await message.channel.send(embed=embed)

    if message.content.startswith("!청소"):
        number = int(message.content.split(" ")[1])
        await message.delete()
        await message.channel.purge(limit=number)
        await message.channel.send(f"{number}개의 메시지 삭제")




client.run(os.environ['token'])
