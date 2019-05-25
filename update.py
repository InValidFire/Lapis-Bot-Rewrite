import subprocess
import os
import time

print("Starting Update Script")
subprocess.run('git checkout master',shell=True)
print("Changed to master branch")
subprocess.run('git fetch',shell=True)
print("Fetched code, now waiting 30 seconds before bot reboot")
time.sleep(30)
print("Rebooting bot")
dir = os.getcwd()
subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
print("Closing Update Script")
exit()
