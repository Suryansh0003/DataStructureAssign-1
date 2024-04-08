def Unique_char(string):
    mySet = set()

    for char in string:
        if char in mySet:
            return False

        mySet.add(char)
    return True


string1 = "suryansh"
string2 = "abcd"

print(Unique_char(string1))
print(Unique_char(string2))
