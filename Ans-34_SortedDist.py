def Dist_Sorter(Input_dist, reverse=False):
    mydist = dict(sorted(Input_dist.items(), key=lambda x: x[1], reverse=reverse))

    return mydist


inputDist = {"Apple": 3, "orange": 5, "grapes": 2, "papaya": 1}
sortDist_acending = Dist_Sorter(inputDist)
sortdist_decending = Dist_Sorter(inputDist, reverse=True)

print(sortDist_acending)
print(sortdist_decending)
