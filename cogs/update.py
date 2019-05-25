from discord.ext import tasks, commands
import discord
import subprocess

class Update(commands.Cog):
    debug = True

    def __init__(self,bot):
        print("Update: Initialized")
        self.bot = bot

    @commands.command()
    async def update(self,ctx):
        """ Updates the bot's code from the master branch """

#        subprocess.run('update.py')
#        subprocess.run('update.bat')
        role = discord.utils.get(ctx.guild.roles, name="Lapis Lord")
        if(role in ctx.author.roles):
            subprocess.run(['start','py','C:\\Users\\Valid\\OneDrive\\Desktop\\Lapis-Bot-Rewrite\\update.py'],shell=True)
            await ctx.send("Rebooting for update!")
            exit()
        await ctx.send("You do not have permission to use this command.")
def setup(bot):
    bot.add_cog(Update(bot))
