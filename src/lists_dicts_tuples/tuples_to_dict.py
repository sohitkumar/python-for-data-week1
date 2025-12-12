def convertTuplesToDict(input_tuples):
    d = {x:y for x,y in input_tuples}
    return d

t = [("a",1),("b",2)]
print(convertTuplesToDict(t))