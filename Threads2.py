import threading
def uf(num1,num2):
    print("numbers: {} {}".format(num1,num2))
    print("result= {}".format(int(num1)+int(num2)))
    return
t=threading.Thread(target=uf,args=(2,3))
t.start()