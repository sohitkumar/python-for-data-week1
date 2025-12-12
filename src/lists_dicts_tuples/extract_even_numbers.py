def getEvenNumbers(input_list):
    return [x for x in input_list if x % 2 == 0]

l = [1, 2, 3, 4, 5, 6]
print(getEvenNumbers(l))