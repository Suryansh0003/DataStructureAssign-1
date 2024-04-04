def Vowels_counter(string):
    vowels={'a','e','i','o','u'}
    string=string.lower()
    
    StrCount=0
    
    for char in string:
        if char in vowels:
            StrCount+=1
            
    return StrCount
            

while True:
    input_str=input("Enter the string here ")
    print("the vowels count in this string is : ",Vowels_counter(input_str))
    
    command=input("do you want to contnue yes/no").lower()
    if command!="yes":
        break
        
        
        
        
        
    
    
        
        