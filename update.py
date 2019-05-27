import subprocess
import time
import sys
import shlex
import os

print("Starting Update Script")
try:
    subprocess.run('git pull',shell=True)
    print("Fetched code, making success note")
    successfile = open("update_success.temp","w+") #to be processed by the bot at boot if present.
    successfile.close()
    print("Rebooting bot")
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py','bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    print("Closing Update Script")
    time.sleep(3)
    os._exit(0) #forces an exit, avoids triggering the except block
except:
    errorfile = open("update_error.temp","w+") #to be processed by the bot at boot if present.
    errorfile.close()
    print("Update failed, rebooting bot")
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py','bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    print("Closing Update Script")
    time.sleep(3)
    exit()
