from discord.ext import tasks, commands
import discord
import core.vars
import os
import shutil
import asyncio
from cogs.log import log

#TODO:
# Add a way to upload/request files to and from the bot.

class Data(commands.Cog):
    debug = False
    logging = False
    dir = os.getcwd()
    types = ["global","server"]
    typestring = ", ".join(types)

    def __init__(self,bot):
        print("Data: Initialized")
        self.bot = bot
#---------------------------------functions------------------------------------#
    async def makefile(self,structurepath,data = None):
        if(os.path.exists(str(self.dir)+structurepath) != True):
            file = open(str(self.dir)+str(structurepath),"w+")
            file.write(str(data))
            file.close()
            if(self.logging==True):
                await log(self,"Data: Created file: "+structurepath)
        else:
            if(self.logging==True):
                await log(self,"Data: File "+structurepath+" was already found.")

    async def makedir(self,structurepath):
        dir = str(self.dir)
        folders = structurepath.split("\\")
        for folder in folders:
            dir = dir+"\\"+folder
            if(os.path.exists(dir) != True):
                os.makedirs(dir)
            else:
                await log(self,"Data: Directory "+structurepath+" was already found.")

    async def deldir(self,structurepath):
        dir = str(self.dir)
        shutil.rmtree(dir+structurepath) #deletes entire directory tree
        if(self.logging==True):
            await log(self, "Data: Directory "+structurepath+" was deleted.")

    async def delfile(self,structurepath):
        dir = str(self.dir)
        os.remove(dir+structurepath)
        if(self.logging==True):
            await log(self, "Data: File "+structurepath+" was deleted.")

    async def dirlist(self,serverid):
        structure = {
        "global": [
            "dir-/Data/Global/Config",
            "file-/Data/Global/Config/settings.ini-data-TEST",
            "file-/Data/Global/Config/lapislords.ini"
            ],
        "server": [
            "dir-/Data/Server/"+serverid+"/Config"
            ]
        }
        return structure
#----------------------------------commands------------------------------------#
    @commands.group()
    @commands.is_owner()
    async def data(self, ctx):
        if(ctx.invoked_subcommand is None):
                await ctx.send("Invalid data command passed.")

    @data.command() #owner only
    async def create(self,ctx,type):
        datastructure = await self.dirlist(str(ctx.message.guild.id))
        actionlist = datastructure.get(type)
        for action in actionlist:
            splitstring = action.split("-")
            if(splitstring[0] == "dir"):
                await self.makedir(splitstring[1])
            if(splitstring[0] == "file"):
                if(len(splitstring)>2):
                    await self.makefile(splitstring[1],splitstring[3]) #tells it to write data if any is found.
                if(len(splitstring)==2):
                    await self.makefile(splitstring[1])
        await ctx.send("Created "+type+" data successfully.")

    @data.command(aliases=['show','list']) #owner only
    async def tree(self,ctx):
        dir = str(self.dir)
        message = ""
        for dirpath,dirnames,files in os.walk(dir+"\\Data"):
            message = message+dirpath.replace(dir,"")+"\n"
            for file in files:
                message = message+"└── "+file+"\n"
        if(len(message)==0):
            message="No data found."
        await ctx.send(message)

    @data.command() #owner only
    async def delete(self,ctx,path):
        dir = str(self.dir)
        if(path == None):
            await ctx.send("Incorrect Syntax: Include datapath")
        if(os.path.exists(dir+path) == True):
            if("Data" not in path): #keeps sensitive files safe
                await ctx.send("You cannot delete this directory.")
            elif("." in path):
                await self.delfile(path)
                await ctx.send("File "+path+" deleted successfully.")
            else:
                await self.deldir(path)
                await ctx.send("Directory "+path+" and all subdirectories deleted successfully.")
        else:
            await ctx.send("Directory not found.")

    @data.command() #owner only
    async def request(self,ctx,path):
        dir=str(self.dir)
        if(path == None):
            await ctx.send("Incorrect Syntax: Include datapath")
        if(os.path.exists(dir+path) == True):
            if("Data" not in path): #keeps sensitive files safe
                await ctx.send("You cannot request this directory.")
            elif("." in path):
                await ctx.send(file=discord.File(dir+path))
            else:
                shutil.make_archive("request","zip",dir+path)
                await ctx.send(file=discord.File(dir+"\\request.zip"))
                await self.delfile("\\request.zip")
        else:
            await ctx.send("Directory not found.")

def setup(bot):
    bot.add_cog(Data(bot))
