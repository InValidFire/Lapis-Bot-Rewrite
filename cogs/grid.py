import discord
from discord.ext import tasks, commands
import core.vars
import cogs.math
from cogs.log import log

class Grid(commands.Cog):
    debug = False
    logging = False

    def __init__(self,bot):
        print("Grid: Initialized")
        self.bot = bot

    def gridData(self,centerx,centerz,radius): #grabs all possible portal coordinate sets.
        xlist = []
        zlist = []
        centerx = int(centerx) #converts user input, if given, into integers
        centerz = int(centerz)
        radius = int(radius)
        #------ possible coord generation ------#
        nodedist = abs(radius)/2
        tempx = (radius*-1)+centerx
        tempz = (radius*-1)+centerz
        a = 0
        while(a<5):
            xlist.append(int(tempx))
            tempx = tempx+nodedist
            zlist.append(int(tempz))
            tempz = tempz+nodedist
            a=a+1
        nodecoords = [] #stores possible node coords
        for x in xlist: #generates all possible node coords
            loop = len(xlist) #runs through each coord, adding the nodedist until it reaches the last number in the list
            z = zlist[0] #resets the nodez for each coord
            a = 0
            while(a < loop): #generates the numbers, adding them to the list
                nodecoords.append(str(int(x))+", "+str(int(z)))
                z = z+nodedist
                a = a+1
        nodenames = ["Green - A1","Lime/Green - A2","Lime - A3","Lime/Yellow - A4","Yellow - A5","Green/Cyan - B1","Dark Gray - B2","Lime/Pink - B3","Gray - B4","Yellow/Orange - B5","Cyan - C1","Cyan/Pink - C2","Pink - C3","Pink/Orange - C4","Orange - C5","Cyan/Blue - D1","Black - D2","Pink/Purple - D3","White - D4","Orange/Red - D5","Blue - E1","Blue/Purple - E2","Purple - E3","Purple/Red - E4","Red - E5"]
        d = dict()
        d['xlist'] = xlist
        d['zlist'] = zlist
        d['nodecoords'] = nodecoords
        d['nodenames'] = nodenames
        return d

    @commands.command(aliases=['gm'])
    async def gridmap(self,ctx,centerx,centerz,radius):
        """ Maps our grid system based on the given values """
        data = self.gridData(centerx,centerz,radius)
        message = "X: "
        for x in data['xlist']:
            message = message + str(int(x)) + " "
        message = message + "\nZ: "
        for z in data['zlist']:
            message = message + str(int(z)) + " "
        message = message + "\n"
        for coord in data['nodecoords']:
            templist = coord.split(", ")
            ncoords = cogs.math.nether(templist[0],templist[1])
            message = message + data['nodenames'][data['nodecoords'].index(coord)] + ": " + coord + " [" + str(ncoords['x']) + ", " + str(ncoords['z']) + "]\n"
        if self.logging == True:
            await log(self,"Grid: Executed gridmap with coords: {x}, {z} and radius: {r}".format(x=centerx,z=centerz,r=radius))
        await ctx.send(message)

    @commands.command(aliases=['gf'])
    async def gridfind(self,ctx,xcoord,zcoord,centerx=0,centerz=0,radius=1000):
        """ Finds the closest grid portal to the given coords """
        data = self.gridData(centerx,centerz,radius)
        tempx = []
        tempz = []
        nametemp = "None"
        message = "None"
        for x in data['xlist']:
            tempx.append(int(abs(x - int(xcoord))))
        for z in data['zlist']:
            tempz.append(int(abs(z - int(zcoord))))
        for x in tempx:
            if(min(tempx)==x):
                xdest = data['xlist'][tempx.index(x)]
        for z in tempz:
            if(min(tempz)==z):
                zdest = data['zlist'][tempz.index(z)]
        coordtemp = str(xdest) + ", " + str(zdest)
        for coord in data['nodecoords']:
            if coord == coordtemp:
                nametemp = data['nodenames'][data['nodecoords'].index(coord)]
        message = "Portal Name: " + nametemp + "\nX: " + str(xdest) + "\nZ: " + str(zdest)
        if self.logging == True:
            await log(self,"Grid: Executed gridfind for coords {} and {}, finding portal '{}''".format(xcoord,xcoord,nametemp))
        await ctx.send(message)

    @commands.command(aliases=['gs'])
    async def gridsearch(self,ctx,*args):
        """ Search the grid for the desired location """
        data = self.gridData(0,0,1000) #TODO: let this be loaded from a file
        message = ""
        name = " ".join(args)
        if "Grey" in name:
            name = name.replace("Grey","Gray")
        for node in data['nodenames']:
            if name in node:
                templist = data['nodecoords'][data['nodenames'].index(node)].split(", ")
                ncoords = cogs.math.nether(templist[0],templist[1])
                message = message + node + ": " + data['nodecoords'][data['nodenames'].index(node)] + " [" + str(ncoords['x']) + ", " + str(ncoords['z']) + ']' "\n"
        if message == "":
            message = "Nothing found."
        if self.logging == True:
            await log(self,"Grid: Executed gridsearch for name {}".format(name))
        await ctx.send(message)

    @commands.command(aliases=['gv'])
    async def gridview(self,ctx):
        """ View a map of the Grid """
        nodecodes = ["A1","A2","A3","A4","A5","B1","B2","B3","B4","B5","C1","C2","C3","C4","C5","D1","D2","D3","D4","D5","E1","E2","E3","E4","E5"]
        r = -1
        message = ""
        for code in nodecodes:
            if r==5: #TODO: see if .join can improve this, forgot that method existed. :/
                r=0
            if r<5 and r!=0 and r!=-1 and code not in message:
                message = message + " - " + code
                r= r+1
            if r ==-1 and code not in message:
                message = message + "\n`" + code
                r= r+2
            if r==0 and code not in message:
                message = message + "`\n`" + code
                r= r+1
        message = message + "`"
        if self.logging == True:
            await log(self,"Grid: Executed gridview successfully.")
        await ctx.send(message)
def setup(bot):
    bot.add_cog(Grid(bot))
