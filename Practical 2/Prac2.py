a=4
b=3
initialstate=[0,0]
finalstate=[2,0]
rev=finalstate[::-1]
print(rev)
while(initialstate!=finalstate):
    if(initialstate[1]<b):
        initialstate[1]+=b
        print("1",initialstate)
    if(initialstate[0]+initialstate[1]<=a and initialstate[1]>0):
        initialstate[0]=initialstate[0]+initialstate[1]
        initialstate[1]=0
        print("2",initialstate)
    if(initialstate[0]+initialstate[1]>=a and initialstate[1]>0):
        initialstate[1]=initialstate[1]-(a-initialstate[0])
        initialstate[0]=a
        print("3",initialstate)
    if(initialstate[1]>0):
        initialstate[0]=0
        print("4",initialstate)
    if(initialstate==[0,2]):
        initialstate=[2,0]
        print("5",initialstate)