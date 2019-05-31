from discord.ext import tasks, commands
import time
import core.vars

# TODO:
# Add date specific Events
#    - These don't reoccur.
# Give each event an id
#    - Start a variable at 0, add one for each new event and never go backwards.
#    - Global variable, individual servers don't start at 0, all servers share it.
# Make events server-specific
#    - Requires rework of setup()
#    - Might as well just remove saveload() needs a complete rewrite, and changing setup() would break it.
# Add commands for adding/removing events based on the Event ID

class Events(commands.Cog):
    i = 0 #gives each event a number, helping us identify it in the console (only shows up if debug is true)
    b = 0 #prevents bot from spamming messages, helps bot know when it's sent the announcement message
    timecache = "blank" #stores time value when successful. This way it knows when it's already sent the message.
    debug = False #whether or not to get detailed debug info

    def __init__(self, bot):
        print("Events: Initialized")
        self.bot = bot
        self.run.start()

    def cog_unload(self):
        self.run.cancel()

    @tasks.loop(seconds=5.0)
    async def run(self): #checks if the time matches, and posts an event reminder if so
        if(self.debug == True and core.vars.debug == True):
            print("Events: 1b: "+str(self.b))
        channel = self.bot.get_channel(core.vars.channel_announcements) #creates channel object linked to announcement channel.
        currentdate = core.vars.currentdate #currentdate = DAY, TIME
        eventdata = core.saveload.eventdata #list of events loaded from events.cfg in saveload.py
        self.i = 1
        if(self.debug == True and core.vars.debug == True):
            print("-------"+str(1)+"-------")
        for data in eventdata: #compares the current time with the event times loaded
            self.i = self.i + 1
            if(self.i > len(eventdata)): #keeps 'i' from exceeding the amount of events
                self.i = 0
            temp = data.split(" - ") #splits each line in events.cfg in half and puts the result in a list
            time = temp[0]
            message = temp[1]
            if(self.debug == True and core.vars.debug == True):
                print("Events: Time: "+time)
                print("Events: Message: "+message)
                print("Events: Testing "+time+" against the current time, "+currentdate)
            if(currentdate == time and self.b == 0): #if the time matches the currentdate, send the message if it hasn't already
                if(self.debug == True and core.vars.debug == True):
                    print("Events: 2b: "+str(self.b))
                await channel.send(message)
                print("Events: Message sent!")
                if(self.debug == True or core.vars.debug == True):
                    print("-------"+str(self.i)+"-------")
                self.timecache = time #stores the successful time to the cache
                self.b = 1
            if (currentdate != self.timecache and self.b == 1):
                self.b = 0
            if (currentdate != time and self.b == 0 and (self.debug == True and core.vars.debug == True)):
                print("Events: 3b: "+str(self.b))
                print("Events: Did not match")
                print("-------"+str(self.i)+"-------")
        print("Events: Completed time check. - "+core.vars.currenttime)

    @run.before_loop
    async def before_loop(self): #waits on bot to connect before starting the events code
        print('Events: waiting...')
        await self.bot.wait_until_ready()

def setup(bot): #required bit of code so discord.py knows where the cog (this thing) is
    bot.add_cog(Events(bot))
