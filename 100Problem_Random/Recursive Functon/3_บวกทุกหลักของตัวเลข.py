def sum_digits(num):
    st = str(num)
    if len(st) == 1:
        return int(st)
    
    current = st[0]
    after = st[1:]
    
    return sum_digits(int(after)) + int(current)

print(sum_digits(1234))   # 10

# -------------------------------------------------
def sum_digits2(num):
    if num < 10:
        return num

    current = num % 10
    after = num // 10
    return sum_digits2(after) + current




print(sum_digits2(1234))   # 10