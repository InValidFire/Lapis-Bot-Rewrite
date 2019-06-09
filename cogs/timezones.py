from discord.ext import tasks, commands
import discord
import core.vars
from simpledate import SimpleDate
import pytz

class TimeZones(commands.Cog):
    debug = False
    
    def __init__(self,bot):
        print("TimeZones: Initialized")
        self.bot = bot

    @commands.command()
    async def time(self,ctx,timezone):
        """Query the time in a certain timezone."""
        response = SimpleDate(tz=timezone,unsafe=True)
        format = str(response.convert(format='A, I:M p'))
        await ctx.send(timezone+" - "+format)

    @commands.command()
    async def zonesearch(self,ctx,search):
        """Search for timezones with the given term"""
        if(search == None):
            await ctx.send("Please specify a search term.")
        for tz in pytz.all_timezones:
            if(tz.find(search)>=0):
                await ctx.send(tz)
        await ctx.send("Search complete!")

def setup(bot):
    bot.add_cog(TimeZones(bot))
