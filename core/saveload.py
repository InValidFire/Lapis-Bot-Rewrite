import os
import json
import time
## TODO: Turn this into a cog. See if I can run code as a one-off time with asyncio
# This will give us the ability to add a command that reloads the events without a bot reboot.
eventdata = "blank"
class Global:
    sysdate = "blank"
    a1 = 0
    a2 = 0
    a3 = 0
    a4 = 0
    a5 = 0
    a6 = 0
    a7 = 0
    a8 = 0
    a9 = 0
    a10 = 0
    a11 = 0
    a12 = 0
    a13 = 0
    a14 = 0
    a15 = 0
    a16 = 0
    a17 = 0
    a18 = 0
    a19 = 0
    a20 = 0
    a21 = 0
    a22 = 0
    a23 = 0
    a24 = 0
    a25 = 0
    a26 = 0
    a27 = 0
    a28 = 0
    a29 = 0
    a30 = 0
    a31 = 0
    a32 = 0
    a33 = 0
    a34 = 0
    a35 = 0
    a36 = 0
    a37 = 0
    a38 = 0
    a39 = 0
    a40 = 0
    a41 = 0
    a42 = 0
    a43 = 0
    a44 = 0
    a45 = 0
    a46 = 0
    a47 = 0
    a48 = 0
    def load(self):
        dir = os.getcwd()
        with open(dir+"/Data/Global/Temp/timevars.json") as file:
            self.data = json.load(file)
            for item in self.data['times']:
                try:
                    self.sysdate = item['sysdate']
                    print("Saveload: Date loaded successfully: "+self.sysdate)
                except:
                    print("Saveload: Failed to load date")
        if self.sysdate == time.strftime("%m-%d-%Y"):
            for item in self.data['times']:
                self.total=int(item['total'])
                self.a1=int(item['00:00'])
                self.a2=int(item['00:30'])
                self.a3=int(item['01:00'])
                self.a4=int(item['01:30'])
                self.a5=int(item['02:00'])
                self.a6=int(item['02:30'])
                self.a7=int(item['03:00'])
                self.a8=int(item['03:30'])
                self.a9=int(item['04:00'])
                self.a10=int(item['04:30'])
                self.a11=int(item['05:00'])
                self.a12=int(item['05:30'])
                self.a13=int(item['06:00'])
                self.a14=int(item['06:30'])
                self.a15=int(item['07:00'])
                self.a16=int(item['07:30'])
                self.a17=int(item['08:00'])
                self.a18=int(item['08:30'])
                self.a19=int(item['09:00'])
                self.a20=int(item['09:30'])
                self.a21=int(item['10:00'])
                self.a22=int(item['10:30'])
                self.a23=int(item['11:00'])
                self.a24=int(item['11:30'])
                self.a25=int(item['12:00'])
                self.a26=int(item['12:30'])
                self.a27=int(item['13:00'])
                self.a28=int(item['13:30'])
                self.a29=int(item['14:00'])
                self.a30=int(item['14:30'])
                self.a31=int(item['15:00'])
                self.a32=int(item['15:30'])
                self.a33=int(item['16:00'])
                self.a34=int(item['16:30'])
                self.a35=int(item['17:00'])
                self.a36=int(item['17:30'])
                self.a37=int(item['18:00'])
                self.a38=int(item['18:30'])
                self.a39=int(item['19:00'])
                self.a40=int(item['19:30'])
                self.a41=int(item['20:00'])
                self.a42=int(item['20:30'])
                self.a43=int(item['21:00'])
                self.a44=int(item['21:30'])
                self.a45=int(item['22:00'])
                self.a46=int(item['22:30'])
                self.a47=int(item['23:00'])
                self.a48=int(item['23:30'])
                print("Saveload: Dates matched, loaded data")
        if self.sysdate != time.strftime("%m-%d-%Y"):
            #print(self.sysdate)
            self.sysdate = time.strftime("%m-%d-%Y")
            print("Saveload: Dates did not match, did not load data")
    def eventload(self):
        global eventdata
        try:
            with open("events.cfg") as f: #loads data from events.cfg using the list 'time'
                eventdata = []
                for line in f:
                    eventdata.append(line.rstrip("\n")) #rstrip removes the newline characters before adding each line of the events.cfg to the list
        except IOError:
            f = open("events.cfg","w+")
            eventdata = [] #avoids exception involving line 21
            print("Saveload: Created 'events.cfg' file")
        print("Saveload: Loaded 'events.cfg'")
