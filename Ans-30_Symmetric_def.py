def syDef(t1, t2):

    set1 = set(t1)
    set2 = set(t2)
    return set1.symmetric_difference(set2)


tup1 = (2, 4, 8, 16)
tup2 = (2, 4, 32, 56)

result=syDef(tup1,tup2)
print(result)