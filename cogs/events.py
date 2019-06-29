from discord.ext import tasks, commands
import time
import os
import core.vars
import cogs.system

# TODO:
# Add date specific Events
#    - These don't reoccur.
# Fix redundancy in closing and reopening the file just to write data.
#    - Need to figure out how to move the file cursor to the end of the file in r+ mode
# Make eventadd syntax a bit friendlier.
#    - Not sure how as of the moment, will research possible methods

class Events(commands.Cog):
    i = 0 #gives each event a number, helping us identify it in the console (only shows up if debug is true)
    b = 0 #prevents bot from spamming messages, helps bot know when it's sent the announcement message
    timecache = "blank" #stores time value when successful. This way it knows when it's already sent the message.
    debug = True #whether or not to get detailed debug info
    eventdata = []
    id = None

    def __init__(self, bot):
        print("Events: Initialized")
        self.bot = bot
        self.run.start()
        self.eventsload()

    def eventsload(self):
        try:
            file = open(os.getcwd()+"/Data/Global/Config/eventid.cfg","r+") #opens eventid.cfg
            self.id = file.read() #loads latest event id
            file.close()
            file = open(os.getcwd()+"/Data/Global/Config/events.cfg","r+") #opens events.cfg
            self.eventdata = []
            for line in file:
                self.eventdata.append(line.rstrip("\n")) #adds each line to the eventdata list
            file.close()
            print("Events: Loaded eventdata")
            print(self.eventdata)
        except:
            print("Events: Failed to load eventdata")

    @tasks.loop(seconds=5.0)
    async def run(self): #checks if the time matches, and posts an event reminder if so
        if(self.debug == True and core.vars.debug == True):
            print("Events: 1b: "+str(self.b))
        channel = self.bot.get_channel(core.vars.channel_announcements) #creates channel object linked to announcement channel.
        currentdaytime = core.vars.currentdaytime #currentdaytime = DAY, TIME
        eventdata = self.eventdata #list of events loaded from events.cfg in saveload.py
        self.i = 1
        if(self.debug == True and core.vars.debug == True):
            print("-------"+str(1)+"-------")
        for data in eventdata: #compares the current time with the event times loaded
            self.i = self.i + 1
            if(self.i > len(eventdata)): #keeps 'i' from exceeding the amount of events
                self.i = 0
            temp = data.split(" - ") #splits each line in events.cfg in half and puts the result in a list
            id = temp[0]
            time = temp[1]
            type = temp[2]
            message = temp[3]
            if(self.debug == True and core.vars.debug == True):
                print("Events: ID: "+id)
                print("Events: Time: "+time)
                print("Events: Type: "+type)
                print("Events: Message: "+message)
                print("Events: Testing "+time+" against the current time, "+currentdaytime)
            if(currentdaytime == time and self.b == 0): #if the time matches the currentdaytime, send the message if it hasn't already
                if(self.debug == True and core.vars.debug == True):
                    print("Events: 2b: "+str(self.b))
                await channel.send(message)
                print("Events: Message sent!")
                if(self.debug == True or core.vars.debug == True):
                    print("-------"+str(self.i)+"-------")
                self.timecache = time #stores the successful time to the cache
                self.b = 1
            if (currentdaytime != self.timecache and self.b == 1):
                self.b = 0
            if (currentdaytime != time and self.b == 0 and (self.debug == True and core.vars.debug == True)):
                print("Events: 3b: "+str(self.b))
                print("Events: Did not match")
                print("-------"+str(self.i)+"-------")
        print("Events: Completed time check. - "+currentdaytime)

    @commands.command()
    async def eventadd(self,ctx,message,timedate=None,type="weekly"):
        """Adds an event to the events.cfg file. [LL Only]

        timedate:
            The format for this depends on the type of event you're adding:
            weekly: Day-Hours:Minutes

        types: weekly - recurs on a weekly basis"""
        if(cogs.system.System.lordcheck(self,ctx.author.id)==True): #LL permission test
            if(timedate == None):
                timedate = core.vars.currentdaytime
            if(type == "weekly"):
                file = open(os.getcwd()+"/Data/Global/Config/eventid.cfg","r") #loads latest event id
                self.id = int(file.read())
                file.close()
                file = open(os.getcwd()+"/Data/Global/Config/eventid.cfg","w+") #increases event id by 1
                self.id = str(self.id+1)
                file.write(self.id)
                file.close()
                file = open(os.getcwd()+"/Data/Global/Config/events.cfg","r+") #loads events.cfg
                text = ""
                for line in file:
                    text = text + line
                file.close()
                file = open(os.getcwd()+"/Data/Global/Config/events.cfg","w+") #fix this redundancy, I did this because opening a file in r+ without moving the cursor overwrites
                text = text + (self.id+" - "+timedate+" - "+type+" - "+message+"\n") #need to figure out how to move that thing.
                file.write(text)
                file.close()
                await ctx.send("Added weekly event at id: "+str(self.id))
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def eventlist(self,ctx):
        """Lists all events currently loaded. [LL Only]"""
        if(cogs.system.System.lordcheck(self,ctx.author.id) == True):
            message = ""
            for event in self.eventdata: #loads each event into a message and sends it
                message = message + (event+"\n")
            await ctx.send(message)
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def eventremove(self,ctx,id):
        """Removes an event and reloads the events [LL Only]"""
        if(cogs.system.System.lordcheck(self,ctx.author.id) == True): #loads events if the ID doesn't match into a newfile
            file = open(os.getcwd()+"/Data/Global/Config/events.cfg","r+")
            newfile = ""
            for line in file:
                if(line.startswith(id) == False):
                    newfile = newfile + line
            file.close()
            file = open(os.getcwd()+"/Data/Global/Config/events.cfg","w+") #saves that new file
            file.write(newfile)
            file.close()
            self.eventsload()
            await ctx.send("Removed event id: "+id)
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def eventreload(self,ctx):
        """Reloads the events [LL Only]"""
        if(cogs.system.System.lordcheck(self,ctx.author.id) == True):
            self.eventsload() #see this thang
            await ctx.send("Reloaded events!")
        else:
            await ctx.send("You do not have permission to use this command.")

    @run.before_loop
    async def before_loop(self): #waits on bot to connect before starting the events code
        print('Events: waiting...')
        await self.bot.wait_until_ready()

def setup(bot): #required bit of code so discord.py knows where the cog (this thing) is
    bot.add_cog(Events(bot))
