import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
# Загрузка переменных окружения из .env файла
load_dotenv()

# Создайте объект Intents и укажите, какие события вы хотите отслеживать
intents = discord.Intents.default()
intents.messages = True  # Установите необходимые флаги, если нужно
intents.guilds = True
intents.reactions = True

# Передайте объект Intents при создании бота
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    bot.run(os.getenv("DISCORD_TOKEN"))  # Токен должен быть в переменной окружения
