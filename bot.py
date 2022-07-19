import discord
import json
from discord.ext import commands

with open("./settings.json", 'r') as file:
    settings = json.load(file)


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

# @bot.event
# async def on_message(message):
#     if message.author == bot.user:
#         return

#     await message.channel.send("Hello there!")

@bot.command()
async def ping(context):
    await context.send(f"{round(bot.latency * 1000)} ms.")

@bot.command()
async def picture(context):
    await context.send(file = discord.File("./BCalendar/output/temp.png"))

bot.run(settings["TOKEN"])
