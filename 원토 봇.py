import discord
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():

        print(client.user.name)
        print('성공적으로 봇이 실행됨 :D')
        game = discord.Game('원토 유튜브 정리')
        await client.change_presence(status=discord.Status.online, activity=game)
        
        


access_token = os.environ['BOT_TOKEN']
client.run(access_token)
