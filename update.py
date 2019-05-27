import subprocess
import time
import sys
import shlex

print("Starting Update Script")
try:
    checkout = str(subprocess.check_output('git checkout master',shell=True))
    print("Changed to master branch")
    subprocess.run('git pull',shell=True)
    print("Fetched code, making success note")
    successfile = open("update_success.temp","w+") #to be processed by the bot at boot if present.
    successfule.close()
    print("Rebooting bot")
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    print("Closing Update Script")
    time.sleep(3)
    exit()
except CalledProcessError:
    errorfile = open("update_error.temp","w+") #to be processed by the bot at boot if present.
    errorfile.close()
    print("Failed checkout, rebooting bot")
    time.sleep(2)
    if(sys.platform == 'win32'): #restarts bot on windows systems
        subprocess.run(['start','py',dir+'\\bot.py'],shell=True)
    if(sys.platform == 'linux'): #restarts bot on linux systems
        process = subprocess.Popen(shlex.split("""x-terminal-emulator -e python3.7 bot.py"""), stdout=subprocess.PIPE)
    print("Closing Update Script")
    time.sleep(3)
    exit()
