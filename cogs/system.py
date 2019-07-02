from discord.ext import tasks, commands
import discord
import subprocess
import sys
import shlex
import core.vars

#TODO:
# Add +shutdown command, should be simple.
# Add a +time command, shows the time variables.

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

        #if(str(ctx.user.id) in file:
        if(self.lordcheck(ctx.author.id)==True): #Runs the lordcheck() function to see if the user has Lapis Lord permissions.
            if(sys.platform == 'win32'): #handles updates on windows systems
                await ctx.send("Windows: Rebooting for an update!")
                subprocess.run(['start','py','update.py'],shell=True)
                await ctx.bot.close()
            if(sys.platform == 'linux'): #handles updates on linux systems
                await ctx.send("Linux: Rebooting for an update!")
                subprocess.run(shlex.split("""python3.7 update.py &"""))
                await ctx.bot.close()
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def restart(self,ctx):
        if(self.lordcheck(ctx.author.id)==True):
            if(sys.platform == 'win32'):
                await ctx.send("Windows: Restarting bot!")
                subprocess.run(['start','py','restart.py'],shell=True)
                await ctx.bot.close()
            if(sys.platform == 'linux'):
                await ctx.send("Linux: Restarting bot!")
                subprocess.run(shlex.split("""python3.7 restart.py"""))
                await ctx.bot.close()
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def shutdown(self,ctx):
        """Closes the bot"""
        if(ctx.author.id == core.vars.owner_id):
            await ctx.send("Shutting down the bot.")
            await ctx.bot.close()
        else:
            await ctx.send("Really? Thought you could just off me like that... rude.")

    @commands.command()
    async def restartpi(self,ctx):
        if(self.lordcheck(ctx.author.id)==True):
            if(sys.platform == 'linux'):
                await ctx.send("Linux: Restarting Raspberry Pi!")
                subprocess.run(shlex.split("""python3.7 restartpi.py"""))
                await ctx.bot.close()
            else:
                await ctx.send("This is a Linux only command.")
        else:
            await ctx.send("You do not have permission to use this command.")

    @commands.command()
    async def branch(self,ctx,mode,branch_name=None):
        """ Modify the branch the bot operates on

            Modes:
            - swap: changes branch to 'branch_name'
            - status: show the output of 'git status'
            - version: shows the latest commit message """

        if(self.lordcheck(ctx.author.id)==True):
            if(mode in ['swap','switch','change']):
                if(ctx.author.id == core.vars.owner_id):
                    if(sys.platform == 'win32'):
                        file = open("branch.temp","w+")
                        file.write(branch_name)
                        file.close()
                        await ctx.send("Windows: Rebooting for a branch change to '"+branch_name+"'!")
                        subprocess.run(['start','py','branch.py'],shell=True)
                        await ctx.bot.close()
                    if(sys.platform == 'linux'):
                        file = open("branch.temp","w+")
                        file.write(branch_name)
                        file.close()
                        await ctx.send("Linux: Rebooting for a branch change to '"+branch_name+"'!")
                        subprocess.run(shlex.split("""python3.7 branch.py &"""))
                        await ctx.bot.close()
            if(mode in ['status']):
                if(sys.platform == 'win32'):
                    process = subprocess.check_output(['git','status'],universal_newlines=True)
                    await ctx.send(process)
                if(sys.platform == 'linux'):
                    process = subprocess.check_output(shlex.split("""git status"""),universal_newlines=True)
                    await ctx.send(process)
            if(mode in ['version']):
                if(sys.platform == 'win32'):
                    process = subprocess.check_output(['git','log','-1'],universal_newlines=True)
                    await ctx.send(process)
                if(sys.platform == 'linux'):
                    process = subprocess.check_output(shlex.split("""git log -1"""), universal_newlines=True)
                    await ctx.send(process)
        else:
            await ctx.send("This is an owner only command.")

    @commands.command()
    async def sid(self,ctx):
        """Gets the server id"""
        if(self.lordcheck(ctx.author.id)==True):
            await ctx.send("Server ID: "+str(ctx.message.guild.id))

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
        """ Manage Lapis Lords [Owner Only]

        Modes:
        - list: lists all Lapis Lords
        - add: adds a user to the Lapis Lord roster
        - remove: removes a user from the Lapis Lord roster
        - reset: resets the Lapis Lord Roster
        """
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
                    text = text + s # adds whatever's left to the rewrite variable
                file.close()
                file = open("Data/Global/Config/lapislord.cfg","w+") #resets the lapislord.cfg file
                file.write(text) #writes file rewrite variable
                file.close() #closes the file instance
                await ctx.send("Removed "+str(user.name)+" from the Lapis Lord roster.")
            if(mode == "reset"):
                file = open("Data/Global/Config/lapislord.cfg","w+")
                await ctx.send("Reset the lapislord.cfg")
        if(ctx.message.author.id != core.vars.owner_id):
            await ctx.send("This is an owner only command.")

    @commands.command()
    async def github(self,ctx):
        """Gets link to the bot repository"""
        await ctx.send("Here's a link to my code:\n<https://github.com/InValidFire/Lapis-Bot-Rewrite>")

    @commands.command(aliases=['issues','bugs','report'])
    async def suggest(self,ctx):
        """ Go to the suggestions page for Lapis. """
        ownerid = self.bot.get_user(196335906871967744) #bot creator's ID, do not change unless you're forking the code.
        await ctx.send("If you want to make a suggestion that " + ownerid.mention + " won't forget, do so here:\n<https://github.com/InValidFire/Lapis-Bot-Rewrite/issues>\nMake sure to label the post appropriately. =D")

    @commands.command(aliases=['info'])
    async def readme(self,ctx):
        """ Shows Lapis's readme file """
        await ctx.send("You'll find info about the bot here:\n<https://github.com/InValidFire/Lapis-Bot-Rewrite/blob/master/README.md>")

def setup(bot):
    bot.add_cog(System(bot))
