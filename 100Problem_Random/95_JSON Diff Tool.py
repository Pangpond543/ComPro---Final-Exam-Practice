def json_diff(dict1: dict, dict2: dict) -> dict:
    result = {"added": {}, "removed": {}, "modified": {}}
    for k, v in dict1.items():
        if dict1[k] != dict2[k]:
            
            

dict1 = {
        "name": "Alice",
        "age": 30,
        "address": {
        "city": "Wonderland",
        "zip": "12345"
        }
}

dict2 = {
        "name": "Alice",
        "age": 31,
        "address": {
        "city": "Wonderland",
        "zip": "54321"
        },
        "email": "alice@example.com"
}

print(json_diff(dict1,dict2))
