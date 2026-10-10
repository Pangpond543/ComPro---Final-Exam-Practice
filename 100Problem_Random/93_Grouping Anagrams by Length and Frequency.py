def group_anagrams(words: list) -> dict:
    dict_sorted = {}
    for w in words:
        sort_ = "".join(sorted(w))
        if sort_ not in dict_sorted:
            dict_sorted[sort_] = []
        dict_sorted[sort_].append(w)
        
    result = {}
    for k, v in dict_sorted.items():
        len_ = len(k)
        if len_ not in result:
            result[len_] = []
        result[len_].append(v)

    return result
    
words = ["bat", "tab", "cat", "act", "tac", "rat", "tar", "art", "star", "rats"]

print(group_anagrams(words))
# { 
#     3: [["bat", "tab"], ["cat", "act", "tac"], ["rat", "tar", "art"]], 
#     4: [["star", "rats"]] 
# }