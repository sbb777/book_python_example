import os, sys, signal
import time
pid=os.getpid() # 현재 파이썬 프로그램의 pid 
print(pid)
while True:
    print('printing ...')
    time.sleep(1)
    os.kill(pid, signal.SIGTERM)
if pid.name == 'notepad' :
    print(pid.id)
