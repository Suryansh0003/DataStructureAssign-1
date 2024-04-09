def MyTup(tup, StartInd, EndInd):

    extractElement = tup[StartInd : EndInd + 1]
    return tuple(extractElement)

OriginalTup=[2,4,8,6,12,24]


strtInd=2
endInd=5

result=MyTup(OriginalTup,strtInd,endInd)
print(result)