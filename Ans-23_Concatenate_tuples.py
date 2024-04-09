def tuple_concetante(t1,t2):
    tup1=set(t1)
    tup2=set(t2)

    c= tup1 | tup2
    # ---we also use union()---
    
    return c



input1=input("Enter the tuple with saperated comma ',' : ")
tupple1=set((map(int ,input1.split(','))))

input2=input("Enter the second tuple with saperated comma ',' : ")
tupple2=set((map(int ,input2.split(','))))

print(tuple_concetante(tupple1,tupple2))