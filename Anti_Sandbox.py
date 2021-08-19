import psutil
alertstate = 0
for proc in psutil.process_iter():
    try:
        processName = proc.name()
        processName = processName.lower()
        if("wireshark" in processName or "processhacker" in processName or "fiddler" in processName or "procexp" in processName or "procmon" in processName or "sysmon" in processName):
            alertstate = 1
            print("Sandbox environment detected! Process exiting...")
            exit()
    except:
        pass
if(alertstate == 0):
    print("Enter your code here")