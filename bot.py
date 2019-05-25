import discord
from discord.ext import commands, tasks
import logging
import os
import core.setup
import core.saveload
import core.vars

logging.basicConfig(level=logging.ERROR)

bot = commands.Bot(command_prefix='+', description='Various things Valdrea needs')
cogs = ['cogs.timer', 'cogs.events', 'cogs.math', 'cogs.update']
gsl = core.saveload.Global() #Global saving/loading class
gset = core.setup.Global() #Global setup class
dir = os.getcwd()

try:
    gsl.load()
    gsl.eventload()
except IOError:
    gset.setup()
    gsl.load()
    gsl.eventload()

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)
#move timer to its own classes in 'core' folder to be called before bot makes connection.
#seems we don't get feedback from async/discord stuff... :c

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    channel = bot.get_channel(547799429072027649)
    update = False
    if(os.path.exists("update_success.temp")):
        await channel.send("Update Complete!")
        os.remove("update_success.temp")
        update = True
    if(os.path.exists("update_error.temp")):
        await channel.send("Uh oh, something went wrong.\nIf you're on another branch, check if you have any uncommitted changes.")
        os.remove("update_error.temp")
        update = True
    if(core.vars.debug == False and update == False):
        await channel.send("It's Lapis.")

bot.run(os.environ['DISCORDBOTTOKEN'], reconnect=True)
#unless otherwise stated, code written by Fire#4224
