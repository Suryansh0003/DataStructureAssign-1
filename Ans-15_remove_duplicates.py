def duplicate_remove(d):
    set1 = set()
    list1 = []

    for item in d:
        if item not in set1:
            set1.add(item)
            list1.append(item)
    return list1


duplicate_list = [2, 4, 2, 6, 2, 6, 4, 7, 4]


print("Original list : {}".format(duplicate_list))
resutl = duplicate_remove(duplicate_list)
print("After remove duplicates : {}".format(resutl))
