import subprocess
import time
import sys
import shlex
import os

print("Starting Restart Script")
try:
    print("Making restart note")
    successfile = open("restart.temp","w+") #to be processed by the bot at boot if present.
    successfile.close()
    print("Rebooting bot")
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py','bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.run(shlex.split("""python3.7 bot.py &"""))
    print("Closing Restart Script")
