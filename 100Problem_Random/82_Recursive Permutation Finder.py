def find_permutations(s: str) -> list:
    if len(s) == 1:
        return s
    
    result = []
    for i in range(len(s)):
        current = s[i]
        before_after = s[:i] + s[i + 1: ]
        
        sss = find_permutations(before_after)
        
        for i in sss:
            result.append(current + i)
        
    return result
     
print(find_permutations("ABC"))