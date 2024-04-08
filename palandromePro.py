def p_drome(s):
    s=s.replace(" ","").lower()
    return s==s[::-1]



#taking user input ..
print("you have 5 chances only")
count=1
while count<=5:
    user=input("Enter the palandrome here : ")
    print("Chance -",count)

    if p_drome(user):
        print("this is an palandrome ")

    else:
        print("This is not an palandrome")
        
    count+=1
   
  