import threading
import time
def ug():
    print(threading.current_thread().getName(),'Starting')
    time.sleep(2)
    print(threading.current_thread().getName(),'Exiting')
    time.sleep(2)
for i in range(5):
    w = threading.Thread(target=ug)
    w.start()