def flatten(lst):
    result = []
    
    for i in lst:
        if isinstance(i, list):
            sss = flatten(i)
            for s in sss:
                result.append(s)
        else: 
            result.append(i)
    return result

print(flatten([1, [2, 3], [4, [5, 6]]]))