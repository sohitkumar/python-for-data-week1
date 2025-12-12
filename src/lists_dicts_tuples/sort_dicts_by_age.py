def sortDictByAge(input_list):
    l1 = sorted(input_list, key= lambda input_list: input_list['age'])
    return l1

l = [{"name":"Bob","age":30},{"name":"Alice","age":30},{"name":"Raj","age":25}]
print(sortDictByAge(l))