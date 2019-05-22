'''
Author: Osman Çakmak
Skype: oxcakmak
Email: oxcakmak@hotmail.com
Website: http://oxcakmak.com/
Country: Turkey [TR]
'''
# pip install psutil
import psutil

#Iterate over all running process
for proc in psutil.process_iter():
    try:
        #Get process name & pid form process object.
        processName = proc.name()
        processID = proc.pid
        print(processName , ' ::: ', processID)
    except (psutil.NoSuchProcess, \
        psutil.AccessDenied, psutil.ZombieProcess):
        pass
