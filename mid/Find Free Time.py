def find_free_time(busy, start, end):
    start_ = start
    result = []
    for s, e in busy:
        if start_ < s:
            result.append((start_, s))
        start_ = max(e, start_)
        
    if start_ < end:
        result.append((start_, end))
    return result



# ตัวอย่างที่ 1 
print(find_free_time([(2, 4), (6, 8)], 1, 10)) 
# Output: [(1, 2), (4, 6), (8, 10)] 

# # ตัวอย่างที่ 2 
print(find_free_time([(1, 3), (3, 5)], 0, 6)) 
# Output: [(0, 1), (5, 6)]

print(find_free_time([(2, 4), (6, 8)], 5, 10))  