import time
import discord

client = discord.Client()
with open("token.txt") as f:
    token = f.read()

@client.event
async def on_connect():
    print("Connected")

@client.event
async def on_ready():
    print("ready")

@client.event
async def on_message(message):
    msg = message.content.split(" ")
    if (msg[0] == "!presence"):
        try:
            game = discord.Game(msg[1])
            await client.change_presence(activity=game)
            await message.channel.send(f"Success! {msg[1]}")
        except:
            await message.channel.send("Invalid command \:(")

client.run(token)
