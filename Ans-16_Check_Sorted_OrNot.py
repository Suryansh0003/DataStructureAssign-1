def sortedL(list):
    if list == sorted(list):
        return "the list is sorted in acceding order "
    elif list == sorted(list, reverse=True):
        return "the list is sorted in decending order "
    else:
        return "The list is not sorted"


MyList = [6, 5, 4, 3, 1]
lst2 = [4, 7, 9, 12]
lst3 = [4, 3, 6, 2, 8]


print(sortedL(MyList))
print(sortedL(lst2))
print(sortedL(lst3))
