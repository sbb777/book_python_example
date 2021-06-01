import psutil   # 실행중인 프로세스 및 시스템 활용 라이브러리
 
for proc in psutil.process_iter():
    try:
        # 프로세스 이름, PID값 가져오기
        processName = proc.name()
        processID = proc.pid
        #print(processName , ' - ', processID)
 
        if processName == "base.exe" or processName ==  "wg.exe" or processName == "ag.exe" or processName == "syrduino.exe":
            parent_pid = processID  #PID
            parent = psutil.Process(parent_pid) # PID 찾기
            for child in parent.children(recursive=True):  #자식-부모 종료
                child.kill()
            parent.kill()
 
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):   #예외처리
        pass


