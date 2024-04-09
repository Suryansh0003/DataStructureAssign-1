def count_element(list):

    Counts = {}

    for i in list:
        if i in Counts:
            Counts[i] += 1
        else:
            Counts[i]=1
    return Counts


list=[1,2,3,45,45,3,2,5,7,2]

print(count_element(list))