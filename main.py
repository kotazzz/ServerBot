import os
import disnake
from disnake.ext import commands
from data_api import ConfigFile, DataABC, ConfigData

bot = commands.Bot(command_prefix='!')
bot.cfg = ConfigFile() 

@bot.command(name='start')
async def _test(ctx):
    await ctx.send('Hi!')

@bot.event
async def on_ready():
    print('Online!')
    
os.environ["JISHAKU_NO_UNDERSCORE"] = "true"
token = os.environ['SERVER_BOT_TOKEN']
bot.load_extension('jishaku')
bot.run(token)