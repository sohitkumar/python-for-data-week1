def groupByKey(input_list, key):
    d = {}
    for i in input_list:
        group_key = i[key]
        if group_key not in d:
            d[group_key] = []
        d[group_key].append(i)
    return d

l = [{"name":"Ann","dept":"HR"},{"name":"Bob","dept":"IT"},{"name":"Cara","dept":"HR"}]
print(groupByKey(l, "dept"))