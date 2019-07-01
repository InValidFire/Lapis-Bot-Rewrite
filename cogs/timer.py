from discord.ext import tasks, commands
import time
import core.vars

#Technically I don't need this file anymore now that I've figured out how cogs work.
#However I like the idea of having all the time calculations done in one location.
#This file may change or disappear later
class Timer(commands.Cog):
    debug = False

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
        if(self.debug == True and core.vars.debug == True):
            print("Timer: currentdaytime - "+core.vars.currentdaytime)
            print("       currenttime - "+core.vars.currenttime)
            print("       currentdate - "+core.vars.currentdate)
def setup(bot):
    bot.add_cog(Timer(bot))
