from discord.ext import tasks, commands
import discord
import core.vars
import os
from cogs.log import log

#TODO:
# Add a way to upload/request files to and from the bot.

class Data(commands.Cog):
    debug = False
    logging = False
    dir = os.getcwd()
    types = ["all","global","server"]
    typestring = ", ".join(types)
    def __init__(self,bot):
        print("Setup: Initialized")
        self.bot = bot

    async def makefile(self,structurepath,data = None):
        if(os.path.exists(str(self.dir)+structurepath) != True):
            file = open(str(self.dir)+str(structurepath),"w+")
            file.write(str(data))
            file.close()
            if(self.logging==True):
                await log(self,"Data: Created file: "+structurepath)
        else:
            if(self.logging==True):
                await log(self,"Data: File: "+structurepath+" was already found.")

    async def makedir(self,structurepath):
        if(os.path.exists(str(self.dir)+str(structurepath)) != True):
            os.makedirs(str(self.dir)+str(structurepath))
            if(self.logging==True):
                await log(self,"Data: Created directory: "+structurepath)
        else:
            if(self.logging==True):
                await log(self,"Data: Directory "+structurepath+" was already found.")

    async def serverset(self,serverid):
        structure = {
        "global": ["dir-/Data","dir-/Data/Global","dir-/Data/Global/Config","file-/Data/Global/Config/settings.ini-data-TEST","file-/Data/Global/Config/lapislords.ini"],
        "server": ["dir-/Data","dir-/Data/Server/"+serverid,"dir-/Data/Server/"+serverid+"/Config"]
        }
        return structure

    @commands.group()
    async def data(self, ctx):
        if(ctx.invoked_subcommand is None):
                await ctx.send("Invalid data command passed.")

    @data.command()
    async def create(self,ctx,type):
        datastructure = await self.serverset(str(ctx.message.guild.id))
        actionlist = datastructure.get(type)
        print(actionlist)
        for action in actionlist:
            splitstring = action.split("-")
            print(splitstring[0]+"-"+splitstring[1])
            if(splitstring[0] == "dir"):
                await self.makedir(splitstring[1])
            if(splitstring[0] == "file"):
                if(len(splitstring)>2):
                    await self.makefile(splitstring[1],splitstring[3]) #tells it to write data if any is found.
                if(len(splitstring)==2):
                    await self.makefile(splitstring[1])
            print("Successfully made "+splitstring[0]+"-"+splitstring[1])

    @data.command(aliases=['show'])
    async def list(self,ctx):
        dir = str(self.dir)
        for dirpath,dirnames,files in os.walk(dir+"\\Data"):
            await ctx.send(dirpath.replace(dir,""))
            for file in files:
                await ctx.send("└── "+file)

    @data.command()
    async def delete(self,ctx,type="None"):
        if(type == "None"):
            await ctx.send("Select a type: "+self.typestring)
        if(type == "all"):
            dir = str(self.dir)
            for dirpath,dirnames,files in os.walk(dir+"/Data",topdown=False):
                for file in files:
                    os.remove(os.path.join(dirpath,file))
                for dirs in dirnames:
                    os.rmdir(os.path.join(dirpath,dirs))
            os.rmdir(dir+"/Data")
            await ctx.send("Deleted the /Data directory")

def setup(bot):
    bot.add_cog(Data(bot))
