import subprocess
import time
import sys
import shlex
import os

print("Starting System Restart Script")
print("Making restartpi note")
successfile = open("restartpi.temp","w+") #to be processed by the bot at boot if present.
successfile.close()
print("Rebooting Raspberry Pi")
time.sleep(2)
process = subprocess.run(shlex.split("""sudo restart"""))
sys.exit()
