def second_larges(num):

    if len(num)<2:
        return "List must have atlist 2 nubmers "
    

    Largest=Second_lar=float('-inf')

    for a in num:
        if a>Largest:
            Second_lar=Largest
            Largest=a

        elif a>Second_lar and a!=Largest:
            Second_lar=a
    return Second_lar

list=[1,2,3,4]
print("Original list :",list)
print("second largest num : ",second_larges(list))