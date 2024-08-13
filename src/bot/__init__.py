# src/bot/__init__.py

import os
from discord.ext import commands
import discord
from dotenv import load_dotenv

# Загрузка переменных окружения из .env файла
load_dotenv()

# Создайте объект Intents и укажите, какие события вы хотите отслеживать
intents = discord.Intents.default()
intents.messages = True  # Установите необходимые флаги, если нужно
intents.guilds = True
intents.reactions = True
intents.message_content = True  # Включаем доступ к содержимому сообщений

# Передайте объект Intents при создании бота
bot = commands.Bot(command_prefix='!', intents=intents)

# Загрузка токена из переменных окружения
TOKEN = os.getenv('DISCORD_TOKEN')

# Функция для загрузки когов
def load_cogs():
     bot.load_extension('src.bot.commands')
     bot.load_extension('src.bot.config_commands')

# Запуск бота
def run_bot():
    load_cogs()
    bot.run(TOKEN)
