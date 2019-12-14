from discord.ext import tasks, commands
import core.vars
import cogs

#TODO:
# Server specific stuff needs to happen
# Save and load the debug/logging variables from a file

async def log(self,message,channel=566836559039430668):
    channel = self.bot.get_channel(channel)
    await channel.send(message)

class Log(commands.Cog):
    def __init__(self,bot):
        print("Log: Initialized")
        self.bot = bot

    @commands.command() #possibly creating new variable instead of pointing to the one requested. :/ Need to figure this out.
    async def debug(self,ctx,cogname):
        """ Toggle Debug mode for given cog. """
        cogname = cogname.lower()
        cog = getattr(cogs,cogname)
        cogname = cogname.capitalize()
        cog = getattr(cog,cogname)
        if cog.debug == False:
            setattr(cog,'debug',True)
        else:
            setattr(cog,'debug',False)
        await log(self,"Debug for "+cogname+" set to "+str(cog.debug))

    @commands.command()
    async def logging(self,ctx,cogname):
        """ Toggle logging for given cog. """
        cogname = cogname.lower()
        cog = getattr(cogs,cogname)
        cogname = cogname.capitalize()
        cog = getattr(cog,cogname)
        if cog.logging == False:
            setattr(cog,'logging',True)
        else:
            setattr(cog,'logging',False)
        await log(self,"Logging for "+cogname+" set to "+str(cog.logging))

def setup(bot):
    bot.add_cog(Log(bot))
