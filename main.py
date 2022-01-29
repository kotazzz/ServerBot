import os
import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.command(name='test')
async def _test(ctx):
    await ctx.send('Hi!')

@bot.event
async def on_ready():
    print('Online!')

bot.load_extension('jishaku')
token = os.environ['SERVER_BOT_TOKEN']
bot.run(token)