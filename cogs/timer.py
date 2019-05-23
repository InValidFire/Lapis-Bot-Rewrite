from discord.ext import tasks, commands
import time
import core.vars

class Timer(commands.Cog):
    debug = False

    def __init__(self, bot):
        print("Timer: Initialized")
        self.bot = bot
        self.timer.start()

    def cog_unload(self):
        self.timer.cancel()

    @tasks.loop(seconds=3)
    async def timer(self):
        currentdays=time.strftime("%A")
        currenthour=time.strftime("%H")
        currentmins=time.strftime("%M")
        core.vars.currentdate = currentdays+", "+currenthour+":"+currentmins
        core.vars.currenttime = currenthour+":"+currentmins
        if(self.debug == True or core.vars.debug == True):
            print("Timer: Currentdate - "+core.vars.currentdate)
            print("Timer: Currenttime - "+core.vars.currenttime)
def setup(bot):
    bot.add_cog(Timer(bot))
