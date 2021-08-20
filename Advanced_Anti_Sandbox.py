from time import sleep
import time
import win32api
import sys
import psutil
alertstate = 0
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processName = processName.lower()
        if("wireshark" in processName or "processhacker" in processName or "fiddler" in processName or "procexp" in processName or "procmon" in processName or "sysmon" in processName):
            print("One or more debuggers/network analyze tools detected!")
            alertstate = 1
    except:
        pass
secs = 20
if len(sys.argv) == 2:
	secs = float(sys.argv[1])

x, y = win32api.GetCursorPos()
print("x: " + str(x) + ", y: " + str(y))

sleep(secs)

x2, y2 = win32api.GetCursorPos()
print("x: " + str(x2) + ", y: " + str(y2))

if x - x2 == 0 and y - y2 == 0:
	print("No mouse movement detected!");alertstate = 1
else:
	pass
if time.tzname[0] == "Coordinated Universal Time" or time.tzname[1] == "Coordinated Universal Time":
	print("UTC time zone detected!");alertstate = 1
else:
	pass
if(alertstate == 0):
    print("Enter your code here")
else:
    print("Sandbox environment detected! Process exiting...")
    exit()