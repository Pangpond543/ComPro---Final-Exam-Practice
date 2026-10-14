def subsets(s):
    if s == "":
        return [s]
    
    current = s[0]
    after = s[1:]
    
    result = []
    for i in subsets(after):
        result.append(i)
        result.append(current + i)
    return result

print(subsets("abc"))   # ["", "a", "b", "ab"]  (ลำดับไม่ซีเรียส)