import threading

def uf():
    print("hello world")
    return
treads=[]
for i in range(5):
    t=threading.Thread(target=uf)
    treads.append(t)
    t.start() 