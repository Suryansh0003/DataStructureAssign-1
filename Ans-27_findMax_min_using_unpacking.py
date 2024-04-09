def num(number):

    MinValue=min(*number)
    MaxValue=max(*number)

    return MinValue,MaxValue

number=(4,5,6,7,9)
MinV,Maxv=num(number)
print("max - ",Maxv)
print("min - ",MinV)




