import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(671251879530987520)
    await channel.send(f'{member}光臨了比薩店')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(671251879530987520)
    await channel.send(f'{member}離開了比薩店')

bot.run("NjcxMjIzODQyNzk4MTc0MjA4.Xi6M3Q._-AvNILZeGztWU3lRlYcmASt2cE")