import random

def suffle_program(list):
    n=len(list)
    for i in range(n-1,0,-1):
        j=random.randint(0,i)
        list[i],list[j]=list[j],list[i]
    return list

list=[1,2,3,4,5,6,7,8]
result=suffle_program(list)
print("suffle list is : ",result)