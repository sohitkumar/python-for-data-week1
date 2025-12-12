def unique_elements(input_list):
    # approach1
    # d = {x: input_list.count(x) for x in input_list}
    # return list(d.keys())

    # approach2
    # return list(dict.fromkeys(input_list))

    # approach3
    result = []
    for x in input_list:
        if x not in result:
            result.append(x)
    return result

l = ["a", "b", "a", "c", "b"]
print(unique_elements(l))