list=[1,2,3,4,5]

left=0
right=len(list)-1

while left<right:
    temp=list[left]
    list[left]=list[right]
    list[right]=temp

    left+=1
    right-=1
print(list)

