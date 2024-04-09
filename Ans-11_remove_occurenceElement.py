def Remove_Occ(String_tobe_remove, Input_list):
    while String_tobe_remove in Input_list:
        Input_list.remove(String_tobe_remove)
    return Input_list


elements = [2, 4, 8, 16, 2, 32]
remo = 2
result = Remove_Occ(remo,elements)
print("List after removing {} : {}".format(remo, result))
