def sum_to_n(n):
    if n > 1:
        result = n - 1
    else: 
        return n
    
    result = sum_to_n(result) + n
    return result

print(sum_to_n(4))   # 10  (1+2+3+4)
print(sum_to_n(1))   # 1