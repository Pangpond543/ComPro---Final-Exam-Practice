def flatten_dict(d: dict, separator: str = '.') -> dict:
    result = {}
    for k, v in d.items():
        if type(v) == dict:
            for k1, v1 in v.items():
                if type(v1) == dict:
                    for k2, v2 in v1.items():
                        if type(v2) == dict:
                            pass
                        else:
                            result[k + separator + k1 + separator + k2] = v2
                else:
                    result[k + separator + k1] = v1
        else:
            result[k] = v
    return result
    
d = { "a": 1, "b": { "c": 2, "d": { "e": 3, "f": 4 } } }
separator = "."

print(flatten_dict(d, separator))

# { 
#  "a": 1, 
#  "b.c": 2, 
#  "b.d.e": 3, 
#  "b.d.f": 4 
# }