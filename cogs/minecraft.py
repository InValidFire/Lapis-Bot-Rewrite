from discord.ext import tasks, commands
import discord
import core.vars
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
        xcoord = float(xcoord)
        zcoord = float(zcoord)
        await ctx.send("Nether Coords:\nX: {x:.0f}\nZ: {z:.0f}".format(x=floor(xcoord/8),z=floor(zcoord/8)))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Overworld coords to Nether coords")

    @commands.command()
    async def overworld(self,ctx,xcoord,zcoord):
        """ Converts given Nether coordinates to Overworld coordinates
        +/-8 block range"""
        xcoord = float(xcoord)
        zcoord = float(zcoord)
        await ctx.send("Overworld Coords:\nX: {x:.0f} to {s:.0f}\nZ: {z:.0f} to {a:.0f}".format(x=floor(xcoord*8),s=floor((xcoord+1)*8-1),z=floor(zcoord*8),a=floor((zcoord+1)*8-1)))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Nether coords to Overworld coords")

def setup(bot):
    bot.add_cog(Minecraft(bot))
