def Invert_dict(Input_dict):
    inverted_dict={}

    for key,value in Input_dict.items():
        if value not in inverted_dict:
            inverted_dict[value]=[key]
        else: 
            inverted_dict[value].append(key)
    return inverted_dict


Mydict={'a':1,'b':2,'c':1,'d':2}

print(Invert_dict(Mydict))

