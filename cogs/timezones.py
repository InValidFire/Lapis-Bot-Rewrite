from discord.ext import tasks, commands
import discord
import core.vars
from simpledate import SimpleDate
import pytz
from cogs.log import log

#TODO:
# make entire time system based on UTC, likely using this module. To replace cogs.timer

class Timezones(commands.Cog):
    debug = False
    logging = False
    bottime = None

    def __init__(self,bot):
        print("TimeZones: Initialized")
        self.bot = bot
        self.timer.start()

    @commands.command()
    async def time(self,ctx,timezone):
        """Query the time in a certain timezone."""
        for tz in pytz.all_timezones: #makes it case-insensitive
            if(timezone.lower() == tz.lower()):
                timezone = tz
        response = SimpleDate(tz=timezone,unsafe=True)
        format = str(response.convert(format='B d, Y - I:M p'))
        await ctx.send(format)

    @commands.command()
    async def zonesearch(self,ctx,search):
        """Search for timezones with the given term"""
        if(search == None):
            await ctx.send("Please specify a search term.")
        search = search.lower()
        for tz in pytz.all_timezones:
            ttz = tz.lower()
            if(ttz.find(search)>=0):
                await ctx.send(tz)
        await ctx.send("Search complete!")

    @tasks.loop(seconds=1)
    async def timer(self):
        lasttime = self.bottime
        self.bottime = SimpleDate(tz='UTC')
        self.bottime = str(self.bottime.convert(format='B d, Y - I:M p'))
        if(self.logging == True and lasttime != self.bottime):
            await log(self,"Bottime updated: "+self.bottime)

    @commands.command()
    async def bottime(self,ctx):
        await ctx.send(self.bottime)

def setup(bot):
    bot.add_cog(Timezones(bot))
