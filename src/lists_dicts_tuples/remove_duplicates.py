def remove_duplicates(input_list):
    l1 = list(set(input_list))
    return l1

l = [1, 2, 2, 3, 1, 4]
print(remove_duplicates(l))