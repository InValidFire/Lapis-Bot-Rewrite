import discord
from discord.ext import tasks, commands
import core.vars
import math

def nether(x,z):
    x=math.floor(int(x)/8)
    z=math.floor(int(z)/8)
    d = dict()
    d['x'] = x
    d['z'] = z
    return d

def overworld(x,z):
    x=math.floor(int(x)*8)
    z=math.floor(int(z)*8)
    x2=math.floor(x+7)
    z2=math.floor(z+7)
    d = dict()
    d['x'] = x
    d['z'] = z
    d['x2'] = x2
    d['z2'] = z2
    return d

class Math(commands.Cog):
    debug = True
    decimal = 0 #controls our moving decimal system

    def __init__(self, bot):
        print("Math: Initialized")
        self.bot = bot
        self.decimal = 2

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

def setup(bot):
    bot.add_cog(Math(bot))
