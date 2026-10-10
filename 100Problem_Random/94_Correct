def flatten_dict(d: dict, separator: str = '.') -> dict:
    result = {}

    for k, v in d.items():
        if type(v) == dict:
            nested = flatten_dict(v, separator)

            for k1, v1 in nested.items():
                result[k + separator + k1] = v1
        else:
            result[k] = v

    return result

d = { "a": 1, "b": { "c": 2, "d": { "e": 3, "f": 4 } } }
separator = "."

print(flatten_dict(d, separator))