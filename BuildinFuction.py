def main():
    templist=[1,2,3,4,5,6,7]
    templist1=[]
    for item in templist:
        templist1.append(item*2)
    print(templist1)
    templist2=list(map(lambda x:x*2, templist))
    print(templist2)
    templist3=list(filter(lambda x:x % 2==0,templist))
    print(templist3)

if __name__=="__main__":main()