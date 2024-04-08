def find_all_occurrences(Main_String,Sub_String):
    occurence=[]
    
    start=0
    while True:
        start=Main_String.find(Sub_String,start)
        if start==-1:
            return occurence
        
        occurence.append(start)
        start+=len(Sub_String)
        
        
        
Main_String="appleAPple".lower()
Sub_String="pp"
occurence=find_all_occurrences(Main_String,Sub_String)
print(occurence)