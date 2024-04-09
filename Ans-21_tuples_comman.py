
def comman_in_two_tuples(tup1,tup2):
    set1=set(tup1)
    set2=set(tup2)

    comman=set1.intersection(set2)
    comman_tuple=tuple(comman)

    return comman_tuple

tuple1=(1,3,5,6,7)
tuple2=(5,6,7,2,85)

result=comman_in_two_tuples(tuple1,tuple2)
print("comman in two tuples : ",result)