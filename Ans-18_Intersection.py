def intersection(s1, s2):
    return list(set(s1) & set(s2))


s1 = [4, 7, 6, 2, 7, 2, 5]
s2 = [5, 6, 7, 4, 7, 6]
print("The inter seciton of two list : {}}".format(intersection(s1, s2)))
