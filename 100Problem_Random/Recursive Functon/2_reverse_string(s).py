def reverse_string(s):
    if len(s) == 1:
        return s

    current = s[0]
    after = s[1:]
    
    return reverse_string(after) + current

print(reverse_string("abc"))   # "cba"
print(reverse_string("a"))  # "a"