import discord 
from discord.ext import commands

bot=commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    print(f'{member}光臨了比薩店')

@bot.event
async def on_member_remove(member):
    print(f'{member}離開了比薩店')

bot.run('NjcxMjIzODQyNzk4MTc0MjA4.Xi5-pQ.avHGUO05axvxf1iC2moo5DNE8UA')