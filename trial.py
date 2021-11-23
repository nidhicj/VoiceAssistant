import time
import main
import pywhatkit as kit

print('set a timer for 12 minutes and 30 seconds')
command = take_command()
print(command)
meta = [int(s) for s in command.split() if s.isdigit()]
if 'minutes' in command:
    talk('Setting a timer for ' +str(meta[0])+ 'and ' +str(meta[1])+ 'seconds' )

kit.shutdown(1)