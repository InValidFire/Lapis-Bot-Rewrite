import subprocess
import os
import time
import sys

dir = os.getcwd()
print("Starting Update Script")
checkout = subprocess.check_output('git checkout master',shell=True) #need to find a way to stop the script if git doesn't properly change branches, look into subprocess more.
if("error" in checkout):
    errorfile = open(dir+"\update_error","w+")
print("Changed to master branch")
subprocess.run('git fetch',shell=True)
print("Fetched code, making success note")
successfile = open(dir+"\update_success","w+")
print("Rebooting bot")
if(sys.platform == 'win32'): #restarts bot on windows systems
    subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
if(sys.platform == 'linux'): #restarts bot on linux systems
    subprocess.run(['x-terminal-emulator','-e','python3.7',dir+'\\bot.py'],shell=True)
print("Closing Update Script")
time.sleep(3)
exit()
