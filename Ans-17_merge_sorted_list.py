def Merge_lis(list1, list2):
    i = 0
    j = 0

    mergedList = []
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            mergedList.append(list1[i])
            i += 1
 
        else:
            mergedList.append(list2[j])
            j+=1

    while i < len(list1):
        mergedList.append(list1[i])
        i += 1

    while j < len(list2):
        mergedList.append(list2[j])
        j += 1
    return mergedList

list1 = [1,2,3,4]
list2 = [5,7,8,6]

margedL = Merge_lis(list1, list2)
print(margedL)

