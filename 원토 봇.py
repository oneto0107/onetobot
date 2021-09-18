import discord
import asyncio

client = discord.Client()

token = "ODc0OTI4MjU3NjA5MzgzOTQ2.YROGbw.RpxxcJPxVHjZazzDbOEJKyZoXpI"

@client.event
async def on_ready():

        print(client.user.name)
        print('성공적으로 봇이 실행됨 :D')
        game = discord.Game('원토 유튜브 정리')
        await client.change_presence(status=discord.Status.online, activity=game)


client.run(token)
