import subprocess
import time
import sys
import shlex
import os

print("Starting Branch Script")
file = open("branch.temp","r")
branch_name = file.read() #loads the branch name from the temporary file
file.close()
try:
    checkout = str(subprocess.check_output('git checkout '+branch_name,shell=True)) #attempts to checkout to the selected branch
    print("Successful checkout to '"+branch_name+"', rebooting bot")
    successfile = open("branch_success.temp","w+") #to be processed by the bot at boot if present.
    successfile.close()
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    print("Closing Branch Script")
    time.sleep(3)
    exit()
except:
    errorfile = open("branch_error.temp","w+") #to be processed by the bot at boot if present.
    errorfile.close()
    print("Failed checkout to '"+branch_name+"', rebooting bot")
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py','bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE) #same command pulled from update.py
    print("Closing Branch Script")
    time.sleep(3)
    exit()
