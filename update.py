import subprocess
import os
import time
import sys

dir = os.getcwd()
print("Starting Update Script")
checkout = str(subprocess.check_output('git checkout master',shell=True))
if("error" in checkout):
    errorfile = open(dir+"\\update_error.temp","w+")
    exit()
print("Changed to master branch")
subprocess.run('git pull',shell=True)
print("Fetched code, making success note")
successfile = open(dir+"\\update_success.temp","w+")
print("Rebooting bot")
time.sleep(2)
if(sys.platform == 'win32'): #restarts bot on windows systems
    subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
if(sys.platform == 'linux'): #restarts bot on linux systems
    subprocess.run(["x-terminal-emulator","-e","bash","-c","'python3.7","bot.py;","bash'"],shell=True)
print("Closing Update Script")
time.sleep(3)
exit()
