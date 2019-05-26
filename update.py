import subprocess
import os
import time
import sys
import shlex

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
    process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    #process = subprocess.Popen(['x-terminal-emulator','-e','python3.7 bot.py'],shell=True, stdout=subprocess.PIPE)
    print(process.returncode)
print("Closing Update Script")
time.sleep(3)
exit()
