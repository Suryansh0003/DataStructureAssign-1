def Ana(String1,String2):
    
    String1.replace(" ","").lower()
    String2.replace(" ","").lower()
    
    SortStr1=sorted(String1)
    SortStr2=sorted(String2)
    
    return SortStr1==SortStr2


user1=input("Enter the first string   :")
user2=input("Enter The second string   :")
    
if Ana(user1,user2):
    print("This is an anagram".upper())
else :
    print("This is not an anagram".upper())