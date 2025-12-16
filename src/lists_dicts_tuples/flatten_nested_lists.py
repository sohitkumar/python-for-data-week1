def flattened_list(nested_list):
    final_list = []
    for item in nested_list:
        if isinstance(item, list):
            final_list.extend(flattened_list(item))
        else:
            final_list.append(item)
    return final_list

nested_list = [[1,2],[3,[4, [5]]]]
print(flattened_list(nested_list))