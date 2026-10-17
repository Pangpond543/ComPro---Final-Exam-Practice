def json_diff(dict1: dict, dict2: dict) -> dict:
    result = {"added": {}, "removed": {}, "modified": {}}
    
    for k, v in dict2.items():
        if k not in dict1:
            result["added"][k] = v
    
    for k, v in dict1.items():
        if k not in dict2:
            result["removed"][k] = v
            continue
        
        if type(v) == dict and type(dict2[k]) == dict:
            re = json_diff(v, dict2[k])
            for cat in ["added", "removed", "modified"]:
                if re[cat]:
                    result[cat][k] = re[cat]
                
            continue
            
        if v != dict2[k]:
            result["modified"][k] = {"from": v, "to": dict2[k]}
        
    return result

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
