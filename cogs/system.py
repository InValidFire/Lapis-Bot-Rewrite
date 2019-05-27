from discord.ext import tasks, commands
import discord
import subprocess
import os
import sys
import shlex
import core.vars

class System(commands.Cog):
    debug = False

    def __init__(self,bot):
        print("System: Initialized")
        self.bot = bot

    def lordcheck(self,id):
        if(core.vars.debug==True and self.debug==True):
            print("System: Permission check started")
        file = open("Data/Global/Config/lapislord.cfg","r")
        for line in file:
            if(str(id) in line):
                if(core.vars.debug==True and self.debug==True):
                    print("System: Permission check passed")
                return True
        if(core.vars.debug==True and self.debug==True):
            print("System: Permission check failed")
            return False

    @commands.command()
    async def update(self,ctx):
        """ Updates the bot's code to math the Github's master branch [Lapis Lord only] """

        #look into the specifics of ctx works in the discord.py documentation later, appears to get the context of the command, but what does that include
        dir = os.getcwd()
        #if(str(ctx.user.id) in file:
        if(self.lordcheck(ctx.author.id)==True): #Runs the lordcheck() function to see if the user has Lapis Lord permissions.
            if(sys.platform == 'win32'): #handles updates on windows systems
                subprocess.run(['start','py',dir+'\\update.py'],shell=True)
                await ctx.send("Windows: Rebooting for an update!")
                exit()
            if(sys.platform == 'linux'): #handles updates on linux systems
                subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 update.py"""), stdout=subprocess.PIPE)
                await ctx.send("Linux: Rebooting for an update!")
                exit()
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def branch(self,ctx,mode,branch_name=None):
        """ Modify the branch the bot operates on

            Modes:
            - swap: changes branch to 'branch_name'
            - status: show the output of 'git status' """

        if(ctx.author.id == core.vars.owner_id): #owner only command to change branches
            if(mode in ['swap','switch','change']):
                if(sys.platform == 'win32'):
                    file = open("branch.temp","w+")
                    file.write(branch_name)
                    file.close()
                    subprocess.run(['start','py','branch.py'],shell=True)
                    await ctx.send("Windows: Rebooting for a branch change to '"+branch_name+"'!")
                    exit()
                if(sys.platform == 'linux'):
                    file = open("branch.temp","w+")
                    file.write(branch_name)
                    file.close()
                    subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 branch.py"""), stdout=subprocess.PIPE)
                    await ctx.send("Linux: Rebooting for a branch change to '"+branch_name+"'!")
                    exit()
            if(mode in ['status']):
                if(sys.platform == 'win32'):
                    process = subprocess.check_output(['git','status'],universal_newlines=True)
                    await ctx.send(process)
                if(sys.platform == 'linux'):
                    process = subprocess.check_output(shlex.split("""git status"""))
                    await ctx.send(process.output)
        else:
            await ctx.send("This is an owner only command.")

    @commands.command()
    async def id(self,ctx,user: discord.User=None):
        """Gets ID of mentioned user"""
        if(self.lordcheck(ctx.author.id)==True):
            if(user != None):
                await ctx.send("Mentioned ID: "+str(user.id))
            if(user == None):
                await ctx.send("Author ID: "+str(ctx.author.id))
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def getname(self,ctx,id):
        """Gets name of given ID"""
        if(self.lordcheck(ctx.author.id)==True):
            user = self.bot.get_user(int(id))
            await ctx.send(user.name)

    @commands.command()
    async def lapislord(self,ctx,mode,user: discord.User=None): # Owner only command that allows me to trust users with certain commands
        """ Manage Lapis Lords [Owner Only]"""
        if(ctx.author.id == core.vars.owner_id):
            if(mode == "add"):
                with open("Data/Global/Config/lapislord.cfg","a+") as file:
                    file.write(str(user.id)+"\n")
                    file.close()
                await ctx.send("Added "+str(user.name)+" to the Lapis Lord roster.")
            if(mode == "list"):
                try:
                    with open("Data/Global/Config/lapislord.cfg","r") as file:
                        idlist = [] #holds the ids for processing
                        message = ""
                        for line in file:
                            idlist.append(line.rstrip("\n")) #stores each line of the lapislord.cfg as new item in the idlist
                        print(idlist)
                        for id in idlist: #creates the message using the idlist
                            user = self.bot.get_user(int(id))
                            message = message + user.name+" - "+id+"\n"
                        await ctx.send(message)
                except IOError:
                    file = open("Data/Global/Config/lapislord.cfg","w+") #Before push: have this be made in core.setup
                    await ctx.send("Couldn't find lapislord.cfg: Made new file.")
            if(mode == "remove"):
                file = open("Data/Global/Config/lapislord.cfg","r")
                s = "" # line processing variable
                text = "" # holds file rewrite
                for line in file:
                    s = line
                    s = s.replace(str(user.id)+"\n","") #removes all instances the user.id shows up
                    text = text + s # adds whatever's left to the rewrite
                file.close()
                file = open("Data/Global/Config/lapislord.cfg","w+") #resets the lapislord.cfg file
                file.write(text) #writes file rewrite data
                file.close() #closes the file instance
                await ctx.send("Removed "+str(user.name)+" from the Lapis Lord roster.")
            if(mode == "reset"):
                file = open("Data/Global/Config/lapislord.cfg","w+")
                await ctx.send("Reset the lapislord.cfg")
        if(ctx.message.author.id != core.vars.owner_id):
            await ctx.send("This is an owner only command.")

def setup(bot):
    bot.add_cog(System(bot))
