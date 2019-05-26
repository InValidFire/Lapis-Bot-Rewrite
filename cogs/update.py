from discord.ext import tasks, commands
import discord
import subprocess
import os
import sys

class Update(commands.Cog):
    debug = True

    def __init__(self,bot):
        print("Update: Initialized")
        self.bot = bot

    @commands.command()
    async def update(self,ctx):
        """ Updates the bot's code from the master branch """

        role = discord.utils.get(ctx.guild.roles, name="Lapis Lord")
        #look into the specifics of ctx works in the discord.py documentation later, appears to get the context of the command, but what does that include
        dir = os.getcwd()
        if(role in ctx.author.roles):
            if(sys.platform == 'win32'): #handles updates on windows systems
                subprocess.run(['start','py',dir+'\\update.py'],shell=True)
                await ctx.send("W: Rebooting for an update!")
                exit()
            if(sys.platform == 'linux'): #handles updates on linux systems
                process = subprocess.Popen(['x-terminal-emulator','-e','"python3.7 bot.py"'],shell=True, stdout=subprocess.PIPE)
                print(process.returncode)
                await ctx.send("L: Rebooting for an update!")
                exit()
        await ctx.send("You do not have permission to use this command.")
def setup(bot):
    bot.add_cog(Update(bot))
