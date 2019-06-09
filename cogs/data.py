from discord.ext import tasks, commands
import discord
import core.vars
import os

class Data(commands.Cog):
    debug = False
    dir = os.getcwd()


    def __init__(self,bot):
        print("Setup: Initialized")
        self.bot = bot

    @commands.command()
    async def data(self, ctx, mode, type="all"):
        if(cogs.system.System.lordcheck(ctx.author.id) == True):
            if(mode == "create"):
                if(type == "all"): #makes all directories required for bot functionality
                    if(os.path.exists(str(self.dir)+"/Data") != True):
                        os.makedirs(str(self.dir)+"/Data")
                        await ctx.send("Created: /Data")
                    if(os.path.exists(str(self.dir)+"/Data/Global") != True):
                        os.makedirs(str(self.dir)+"/Data/Global")
                        await ctx.send("Created: /Data/Global")
                    if(os.path.exists(str(self.dir)+"/Data/Global/Activity") != True):
                        os.makedirs(str(self.dir)+"/Data/Global/Activity")
                        await ctx.send("Created: /Data/Global/Activity")
                    if(os.path.exists(str(self.dir)+"/Data/Global/Config") != True):
                        os.makedirs(str(self.dir)+"/Data/Global/Config")
                        await ctx.send("Created: /Data/Global/Config")
                    if(os.path.exists(str(self.dir)+"/Data/Server") != True):
                        os.makedirs(str(self.dir)+"/Data/Server")
                        await ctx.send("Created: /Data/Server")
                    if(os.path.exists(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)) != True):
                        os.makedirs(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id))
                        await ctx.send("Created /Data/Server/"+str(ctx.message.guild.id))
                    if(os.path.exists(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Activity") != True):
                        os.makedirs(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Activity")
                        await ctx.send("Created: /Data/Server/"+str(ctx.message.guild.id)+"/Activity")
                    if(os.path.exists(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Config") != True):
                        os.makedirs(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Config")
                        await ctx.send("Created: /Data/Server/"+str(ctx.message.guild.id)+"/Config")
                    if(os.path.exists(str(self.dir)+"/Data/Global/Config/lapislord.cfg") != True):
                        file = open("Data/Global/Config/lapislord.cfg","w+")
                        file.close()
                        await ctx.send("Created the global lapislord.cfg file.")
                    if(os.path.exists(str(self.dir)+"/Data/Global/Config/events.cfg") != True):
                        file = open(str(self.dir)+"/Data/Global/Config/events.cfg","w+")
                        file.close()
                        await ctx.send("Created the global events.cfg file.")
                    if(os.path.exists(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Config/channels.cfg") != True):
                        file = open(str(self.dir)+"/Data/Server/"+str(ctx.message.guild.id)+"/Config/channels.cfg","w+")
                        file.close()
                        await ctx.send("Created the server's channels.cfg file.")
                    if(os.path.exists(str(self.dir)+"/Data/Global/Config/eventid.cfg") != True):
                        file = open(str(self.dir)+"/Data/Global/Config/eventid.cfg","w+")
                        file.write(str(0))
                        file.close()
                        await ctx.send("Created the global eventid.cfg file.")
                    await ctx.send("Setup complete.")
            if(mode == "list" or mode == "show"):
                dir = str(self.dir)
                for dirpath,dirnames,files in os.walk(dir+"/Data"):
                    await ctx.send(dirpath.replace(dir,""))
                    for file in files:
                        await ctx.send("└── "+file)
            if(mode == "delete"):
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
