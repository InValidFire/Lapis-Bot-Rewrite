import discord
from discord.ext import tasks, commands
import core.vars

class Math(commands.Cog):
    debug = True

    def __init__(self, bot):
        print("Math: Initialized")
        self.bot = bot

    def cog_unload(self):
        self.temp.cancel()

    @commands.command(aliases=['deg','temp','temperature'])
    async def degree(self, ctx, temperature, scale):
        """ Convert temperatures between fahrenheit and celsius """
        if(scale == "C" or scale == "c" or scale == "celsius" or scale == "celsius"):
            celsius = float(temperature)
            fahrenheit = celsius*9/5+32
            kelvin = celsius + 273.15
            await ctx.send("{c:.2f}°C = {f:.2f}°F or {k:.2f}°K".format(c=celsius,f=fahrenheit,k=kelvin))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Celsius to Fahrenheit")
        if(scale == "F" or scale == "f" or scale == "Fahrenheit" or scale == "fahrenheit"):
            fahrenheit = float(temperature)
            celsius = (fahrenheit-32)*5/9
            kelvin = celsius + 273.15
            await ctx.send("{f:.2f}°F = {c:.2f}°C or {k:.2f}°K".format(f=fahrenheit,c=celsius,k=kelvin))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Fahrenheit to Celsius")
        if(scale == "K" or scale == "k" or scale == "Kelvin" or scale == "kelvin"):
            kelvin = float(temperature)
            celsius = kelvin - 273.15
            fahrenheit = celsius*9/5+32
            await ctx.send("{k:.2f}°K = {c:.2f}°C or {f:.2f}°F".format(k=kelvin,c=celsius,f=fahrenheit))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Kelvin to Celsius")

    @commands.command()
    async def add(self,ctx,num1,num2):
        """ Adds two numbers together """
        await ctx.send(str(float(num1)+float(num2)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Added {} and {}".format(num1,num2))

    async def sub(self,ctx,num1,num2):
        """ Subtracts two numbers """
        await ctx.send(str(float(num1)-float(num2)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Subtracted {} and {}".format(num1,num2))

    @commands.command()
    async def nether(self,ctx,xcoord,zcoord):
        """ Converts given Overworld coordinates to Nether coordinates """
        xcoord = float(xcoord)
        zcoord = float(zcoord)
        await ctx.send("Nether Coords:\nX: {x:.2f}\nZ: {z:.2f}".format(x=xcoord/8,z=zcoord/8))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Overworld coords to Nether coords")
def setup(bot):
    bot.add_cog(Math(bot))
