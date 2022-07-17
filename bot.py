import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = "c:", intents = intents)

@bot.event
async def on_ready():
    print(f"Online as {bot.user}")

@bot.event
async def on_member_join(member):
    print(member, "joined!")
    channel = bot.get_channel(993165929330507910)
    await channel.send(f"Hello there, @{member}.")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(993165929330507910)
    await channel.send(f"Bye there, @{member}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await message.channel.send("Hello there!")

tokenFile = open("/home/brine/Codes/Python/token.txt", 'r')
TOKEN = tokenFile.readline()
bot.run(TOKEN)
