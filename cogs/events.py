from discord.ext import tasks, commands
import time
import core.vars

class Events(commands.Cog):
    a = 0 #startup messages toggle
    b = 0 #prevents bot from spamming messages
    i = 0 #keeps count of how many times the script has run
    timecache = "blank" #stores time value when successful. Used so it knows when to reset variable 'b'
    debug = True #whether or not to get detailed debug info

    def __init__(self, bot):
        self.bot = bot
        self.run.start()

    def cog_unload(self):
        self.run.cancel()

    @tasks.loop(seconds=5.0)
    async def run(self): #checks if the time matches, and posts an event reminder if so
        if(self.debug == True or core.vars.debug == True):
            print("Events: Outside a: "+str(self.a))
            print("Events: Outside b: "+str(self.b))
        if(self.a == 0):
            if(self.debug == True or core.vars.debug == True):
                print("Events: 1a: "+str(self.a))
                print("Events: 1b: "+str(self.b))
            print("Events: I'm here!")
            self.a = 1
        if(self.a == 1):
            channel = self.bot.get_channel(533473243768684584) #creates channel object linked to announcement channel.
            currentdate = core.vars.currentdate #snatches currentdate value from timer.py
            eventdata = core.saveload.eventdata #snatches eventtimes value from saveload.py
            self.i = 1
            if(self.debug == True or core.vars.debug == True):
                print("Events: 2a: "+str(self.a))
                print("-------"+str(1)+"-------")
            for data in eventdata: #compares the current time with the event times loaded
                self.i = self.i + 1
                if(self.i > len(eventdata)):
                    self.i = 0
                temp = data.split(" - ")
                time = temp[0]
                message = temp[1]
                if(self.debug == True or core.vars.debug == True):
                    print("Events: Time: "+time)
                    print("Events: Message: "+message)
                if(self.debug == True or core.vars.debug == True):
                    print("Events: Testing "+time+" against the current time, "+currentdate)
                if(currentdate == time and self.b == 0):
                    if(self.debug == True or core.vars.debug == True):
                        print("Events: 2b: "+str(self.b))
                    await channel.send(message)
                    print("Events: Message sent!")
                    if(self.debug == True or core.vars.debug == True):
                        print("-------"+str(self.i)+"-------")
                    self.timecache = time
                    self.b = 1
                if (currentdate != self.timecache and self.b == 1):
                    self.b = 0
                if (currentdate != time and self.b == 0 and (self.debug == True or core.vars.debug == True)):
                    print("Events: 3b: "+str(self.b))
                    print("Events: Did not match")
                    print("-------"+str(self.i)+"-------")
        print("Events: Completed time check. - "+core.vars.currenttime)

    @run.before_loop
    async def before_loop(self):
        print('Events: waiting...')
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(Events(bot))
