def compress_string(s):
    result = []
    current = s[0]
    count = 0
    for chr_ in s:
        if chr_ == current:
            count += 1
        else:
            result.append((current, count))
            current = chr_
            count = 1
            
    result.append((current, count))
            
    return result
    
    
print(compress_string("wwwoodw"))
# Output: [('w', 3), ('o', 2), ('d', 1), ('w', 1)]

print(compress_string("aabbaauuuuiiiiuuuuaa"))
# Output: [('a', 2), ('b', 2), ('a', 2)]

print(compress_string("abc"))
# Output: [('a', 1), ('b', 1), ('c', 1)]