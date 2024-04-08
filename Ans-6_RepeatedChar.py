def Repeated_char(string):  
    current_char=string[0]
    current_count=1
    finalStr=""

    for i in range(1,len(string)):
        if string[i]==current_char:
            current_count+=1
        else:
            finalStr+=current_char+'-'+str(current_count)+"\n"
            current_count=1
            current_char=string[i]
    finalStr+=current_char+'-'+str(current_count)+"\n"
    return finalStr

string="abccdeffgHhi"
finalstr=Repeated_char(string)
print(finalstr)
print()


