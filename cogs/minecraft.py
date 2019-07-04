from discord.ext import tasks, commands
import discord
import core.vars
from cogs.math import nether,overworld
from urllib.request import urlopen
from math import floor

class Minecraft(commands.Cog):
    debug = False

    def __init__(self,bot):
        print("Minecraft: Initialized")
        self.bot = bot

    @commands.command(aliases=['search'])
    async def wiki(self,ctx,*args):
        """Search the Minecraft Wiki."""
        with urlopen("https://minecraft.gamepedia.com/Special:Search/{}".format('_'.join(args))) as page:
            await ctx.send(str(page.geturl()))

    @commands.command()
    async def locations(self,ctx):
        """ Show the link for the Valdrea Address Book """
        await ctx.send("You can add or remove locations to the Address Book here:\n<https://docs.google.com/spreadsheets/d/1AsiOVZLNIWb_XxsvvRnU3tG81JqfcNPpS2NML-zh2Uw/edit?usp=sharing>")

    @commands.command(aliases=['portal'])
    async def nether(self,ctx,xcoord,zcoord):
        """ Converts given Overworld coordinates to Nether coordinates """
        coords = nether(xcoord,zcoord)
        await ctx.send("Nether Coords: \nX: {x:d}\nZ: {z:d}".format(x=coords['x'],z=coords['z']))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Overworld coords to Nether coords")

    @commands.command()
    async def overworld(self,ctx,xcoord,zcoord):
        """ Converts given Nether coordinates to Overworld coordinates
        +/-8 block range"""
        coords = overworld(xcoord,zcoord)
        await ctx.send("Overworld Coords:\nX: {x:d} to {x2:d}\nZ: {z:d} to {z2:d}".format(x=coords['x'],x2=coords['x2'],z=coords['z'],z2=coords['z2']))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Nether coords to Overworld coords")

def setup(bot):
    bot.add_cog(Minecraft(bot))
