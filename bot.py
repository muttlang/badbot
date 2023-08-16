import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_KEY = os.getenv('TOKEN_KEY')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print("Logged in")

@bot.command() 
async def test(ctx, arg):
    await ctx.send(arg)

@bot.command()
async def mute(ctx, arg):
    await ctx.send(arg + " has been muted!")


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("Hello"):
        await message.channel.send("Hi")

    await bot.process_commands(message)
bot.run(TOKEN_KEY)