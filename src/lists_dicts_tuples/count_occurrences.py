def getOccurences(input_list):
    d = {x:input_list.count(x) for x in input_list}
    return d

l = ["a", "b", "a", "c", "b", "a"]
print(getOccurences(l))