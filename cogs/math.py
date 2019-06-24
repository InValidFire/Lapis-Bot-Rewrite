import discord
from discord.ext import tasks, commands
import core.vars
import math

class Math(commands.Cog):
    debug = True
    decimal = 0 #controls our moving decimal system

    def __init__(self, bot):
        print("Math: Initialized")
        self.bot = bot
        self.decimal = 2 

    def cog_unload(self):
        self.temp.cancel()

    @commands.command()
    async def decimal(self, ctx, number):
        """ Change the decimal place the math functions round to """
        self.decimal = int(number)
        await ctx.send("Decimal rounding is set to {zero:.{deci}f}".format(zero=0,deci=self.decimal)) #formatting the formatting string hehe.

    @commands.command(aliases=['deg','temp','temperature'])
    async def degree(self, ctx, temperature, scale):
        """ Convert temperatures between fahrenheit, celsius and kelvin """
        if(scale == "C" or scale == "c" or scale == "celsius" or scale == "celsius"):
            celsius = float(temperature)
            fahrenheit = celsius*9/5+32
            kelvin = celsius + 273.15
            await ctx.send("{c:.2f}°C = {f:.2f}°F or {k:.2f}K".format(c=celsius,f=fahrenheit,k=kelvin))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Celsius to Fahrenheit")
        if(scale == "F" or scale == "f" or scale == "Fahrenheit" or scale == "fahrenheit"):
            fahrenheit = float(temperature)
            celsius = (fahrenheit-32)*5/9
            kelvin = celsius + 273.15
            await ctx.send("{f:.2f}°F = {c:.2f}°C or {k:.2f}K".format(f=fahrenheit,c=celsius,k=kelvin))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Fahrenheit to Celsius")
        if(scale == "K" or scale == "k" or scale == "Kelvin" or scale == "kelvin"):
            kelvin = float(temperature)
            celsius = kelvin - 273.15
            fahrenheit = celsius*9/5+32
            await ctx.send("{k:.2f}K = {c:.2f}°C or {f:.2f}°F".format(k=kelvin,c=celsius,f=fahrenheit))
            if(self.debug == True and core.vars.debug == True):
                print("Math: Converted Kelvin to Celsius")

    @commands.command(aliases=['add'])
    async def addition(self,ctx,num1,num2):
        """ Adds two numbers """
        await ctx.send(str(round(float(num1)+float(num2),self.decimal)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Added {} and {}".format(num1,num2))

    @commands.command(aliases=['sub'])
    async def subtract(self,ctx,num1,num2):
        """ Subtracts two numbers """
        await ctx.send(str(round(float(num1)-float(num2),self.decimal)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Subtracted {} and {}".format(num1,num2))

    @commands.command(aliases=['times'])
    async def multiply(self,ctx,num1,num2):
        """ Multiplies two numbers """
        await ctx.send(str(round(float(num1)*float(num2),self.decimal)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Multiplied {} and {}".format(num1,num2))

    @commands.command(aliases=['div'])
    async def divide(self,ctx,num1,num2):
        """ Divides two numbers """
        await ctx.send(str(round(float(num1)/float(num2),self.decimal)))
        if(self.debug == True and core.vars.debug == True):
            print("Math: Divided {} and {}".format(num1,num2))

    @commands.command(aliases=['portal'])
    async def nether(self,ctx,xcoord,zcoord):
        """ Converts given Overworld coordinates to Nether coordinates """
        xcoord = float(xcoord)
        zcoord = float(zcoord)
        await ctx.send("Nether Coords:\nX: {x:.0f}\nZ: {z:.0f}".format(x=math.floor(xcoord/8),z=math.floor(zcoord/8)))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Overworld coords to Nether coords")

    @commands.command()
    async def overworld(self,ctx,xcoord,zcoord):
        """ Converts given Nether coordinates to Overworld coordinates
        +/-8 block range"""
        xcoord = float(xcoord)
        zcoord = float(zcoord)
        await ctx.send("Overworld Coords:\nX: {x:.0f} to {s:.0f}\nZ: {z:.0f} to {a:.0f}".format(x=math.floor(xcoord*8),s=math.floor((xcoord+1)*8-1),z=math.floor(zcoord*8),a=math.floor((zcoord+1)*8-1)))
        if(self.debug == True and core.vars.debug == True):
            print("Converted Nether coords to Overworld coords")

def setup(bot):
    bot.add_cog(Math(bot))
