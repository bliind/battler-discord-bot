import os
import json
import random
import datetime
import discord
from discord import app_commands
from discord.ext import commands, tasks
from util import *

cfg = {}
def load_cfg():
    global cfg
    env = os.getenv('BOT_ENV')
    file = 'battler_cfg.json' if env == 'prod' else 'cattler_cfg.test.json'
    try:
        with open(file, encoding='utf8') as stream:
            cfg = json.load(stream)
        cfg = dotdict(cfg)
    except:
        return False
    return True

load_cfg()

class Battler(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.config = config
        self.server = discord.Object(id=config.server)

    # add commands to the tree on load
    async def cog_load(self):
        self.bot.tree.add_command(self.reload_cfg, guild=self.server)
        self.bot.tree.add_command(self.debug_cfg, guild=self.server)

    # remove commands from the tree on load
    async def cog_unload(self):
        self.bot.tree.remove_command('reload_cfg', guild=self.server)
        self.bot.tree.remove_command('debug_cfg', guild=self.server)

    # attempts to reload the Battler config
    @app_commands.command(name='reload_cfg', description='Reload the Battler config')
    async def reload_cfg(self, interaction: discord.Interaction):
        if load_cfg():
            await interaction.response.send_message('Reloaded Battler config', ephemeral=True)
        else:
            await interaction.response.send_message('Error reloading Battler config', ephemeral=True)

    # debug, spit out config
    @app_commands.command(name='debug_cfg', description='debug cfg')
    async def debug_cfg(self, interaction: discord.Interaction, var: str):
        await interaction.response.send_message(cfg.config[var], ephemeral=True)
