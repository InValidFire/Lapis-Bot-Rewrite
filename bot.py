import discord
from discord.ext import commands, tasks
import logging
import os
import core.vars

logging.basicConfig(level=logging.ERROR)

bot = commands.Bot(command_prefix='+', description='Various things Valdrea needs')
cogs = ['cogs.timer', 'cogs.events', 'cogs.math', 'cogs.system','cogs.data','cogs.timezones','cogs.minecraft']
dir = os.getcwd()

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)

@bot.event
async def on_ready():
    print("Logged in as {0.user}".format(bot))
    channel = bot.get_channel(core.vars.channel_testing)
    update = False #startup message control variables
    branch = False
    restart = False
    if(os.path.exists("branch_success.temp")):
        file = open("branch.temp","r")
        branch_name = file.read()
        file.close()
        await channel.send("Branch switch to '"+branch_name+"' complete!")
        os.remove("branch.temp")
        os.remove("branch_success.temp")
        branch = True
    if(os.path.exists("branch_error.temp")):
        file = open("branch.temp","r")
        branch_name = file.read()
        file.close()
        await channel.send("Branch switch to '"+branch_name+"' failed.\nDouble check the branch name and uncommitted changes.")
        os.remove("branch.temp")
        os.remove("branch_error.temp")
        branch = True
    if(os.path.exists("update_success.temp")):
        await channel.send("Update Complete!")
        os.remove("update_success.temp")
        update = True
    if(os.path.exists("update_error.temp")):
        await channel.send("Uh oh, something went wrong.\nCheck if you have any uncommitted changes.")
        os.remove("update_error.temp")
        update = True
    if(os.path.exists("restart.temp")):
        await channel.send("We're back!")
        os.remove("restart.temp")
        restart = True
    if(os.path.exists("restartpi.temp")):
        await channel.send("We're back!")
        os.remove("restartpi.temp")
        restart = True
    if(core.vars.debug == False and update == False and branch == False and restart == False):
        await channel.send("It's Lapis.")

bot.run(os.environ['DISCORDBOTTOKEN'], reconnect=True)
#unless otherwise stated, code written by Fire#4224
