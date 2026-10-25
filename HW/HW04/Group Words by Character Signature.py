def group_by_signature(words: list) -> list: 
    
    data = {}
    
    for i in words:
        sorted_ = "".join(sorted(i))
        if sorted_ not in data:
            data[sorted_] = [i]
        else:
            data[sorted_].append(i)
            
    return list(data.values())

words = ["abc", "bca", "cab", "bac", "xyz", "yxz", "zxy", "dog"] 
print(group_by_signature(words)) 
# Output: [["abc", "bca", "cab", "bac"], ["xyz", "yxz", "zxy"], ["dog"]]

words = ["apple", "pale", "leap", "plea", "papel", "hello"] 
print(group_by_signature(words)) 
# Output: [["apple", "papel"], ["pale", "leap", "plea"], ["hello"]]