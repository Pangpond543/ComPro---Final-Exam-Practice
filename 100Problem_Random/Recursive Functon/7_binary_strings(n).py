def binary_strings(n):
    if n == 1:
        return ["0", "1"]
    
    result = []
    for sub in binary_strings(n-1):
        result.append("0" + sub)
        result.append("1" + sub)
        
    return result    

print(binary_strings(2))   # ["00", "01", "10", "11"]