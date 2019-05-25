import subprocess
import os
import time

print("Starting Update Script")
subprocess.run('git checkout master',shell=True) #need to find a way to stop the script if git doesn't properly change branches, look into subprocess more.
print("Changed to master branch")
subprocess.run('git fetch',shell=True)
print("Fetched code, now waiting 30 seconds before bot reboot")
time.sleep(30)
print("Rebooting bot")
dir = os.getcwd()
if(sys.platform == 'win32'): #restarts bot on windows systems
    subprocess.run(['start','py',dir+'\\update.py'],shell=True)
if(sys.platform == 'linux'): #restarts bot on linux systems
    subprocess.run(['x-terminal-emulator','-e','python3.7',dir+'\\update.py'],shell=True)
print("Closing Update Script")
time.sleep(3)
exit()
