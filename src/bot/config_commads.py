# src/bot/config_commands.py

import discord
from discord.ext import commands
from src.storage.file_manager import save_config

class ConfigCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='cfg')
    async def cfg(self, ctx, action: str, game: str = None):
        if action == 'add':
            if len(ctx.message.attachments) == 0:
                await ctx.send('Please attach a configuration file.')
                return

            attachment = ctx.message.attachments[0]
            file_content = await attachment.read()

            user_id = ctx.author.id
            username = ctx.author.name
            save_config(user_id, username, game, file_content)

            await ctx.send(f'Configuration for {game} has been added for user {username}.')
        else:
            await ctx.send('Unknown action. Use `add` to add a new configuration.')

def setup(bot):
    bot.add_cog(ConfigCommands(bot))
