#Disabled - Going to phase out completely with timezones.py
from discord.ext import tasks, commands
import time
import core.vars
from cogs.log import log

#Technically I don't need this file anymore now that I've figured out how cogs work.
#However I like the idea of having all the time calculations done in one location.
#This file may change or disappear later
class Timer(commands.Cog):
    debug = False
    logging = False

    def __init__(self, bot):
        print("Timer: Initialized")
        self.bot = bot
        self.timer.start()

    @tasks.loop(seconds=1)
    async def timer(self):
        currentdaynum = time.strftime("%d")
        currentmonthnum = time.strftime("%m")
        currentyearnum = time.strftime("%y")
        currentday=time.strftime("%A")
        currenthour=time.strftime("%H")
        currentmins=time.strftime("%M")
        core.vars.currentdaytime = currentday+"-"+currenthour+":"+currentmins
        core.vars.currenttime = currenthour+":"+currentmins
        core.vars.currentdate = currentmonthnum+"/"+currentdaynum+"/"+currentyearnum
        if(self.debug == True and self.logging == True):
            message = ""
            message = message + "Timer: currentdaytime - "+core.vars.currentdaytime
            message = message + "\n       currenttime - "+core.vars.currenttime
            message = message + "\n       currentdate - "+core.vars.currentdate
            await log(self,message)
def setup(bot):
    bot.add_cog(Timer(bot))
