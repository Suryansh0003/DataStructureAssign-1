def InputIntersection(tuple1, tuple2):
    tup1 = set(tuple1)
    tup2 = set(tuple2)

    comman = tup1.intersection(tup2)
    comman_tup = tuple(comman)

    return comman_tup


input1 = input("Enter the tuple here seperated by comma (,)")
userInput1 = tuple(map(int, input1.split(",")))

input2 = input("Enter the second tuple here sepreted by comma ','")
userInput2 = tuple(map(int, input2.split(",")))

print("comman in both tuples : ", InputIntersection(userInput1, userInput2))
