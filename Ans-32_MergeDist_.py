def merge_dist(dist1, dist2):
    d1 = {}

    for key, value in dist1.items():
        if key in d1:
            d1[key] += value

        else:
            d1[key] = value

    for key, value in dist2.items():
        if key in d1:
            d1[key] += value
        else:
            d1[key] = value

    return d1


dic1 = {"a": 10, "b": 20, "c": 30}
dic2 = {"b": 30, "c": 40, "d": 50}

result = merge_dist(dic1, dic2)
print("Merge dist : ", result)
