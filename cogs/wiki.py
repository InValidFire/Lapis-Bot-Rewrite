from discord.ext import tasks, commands
import discord
import core.vars
from urllib.request import urlopen

class Wiki(commands.Cog):
    debug = False

    def __init__(self,bot):
        print("Wiki: Initialized")
        self.bot = bot

    @commands.command(aliases=['search'])
    async def wiki(self,ctx,*args):
        """Search the Minecraft Wiki."""
        with urlopen("https://minecraft.gamepedia.com/Special:Search/{}".format('_'.join(args))) as page:
            await ctx.send(str(page.geturl()))

def setup(bot):
    bot.add_cog(Wiki(bot))
