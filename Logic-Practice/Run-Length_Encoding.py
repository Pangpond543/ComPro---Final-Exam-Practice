def compress(text: str) -> str:
    chract = text[0]
    str_ = ''
    count = 0
    
    for chr in text:
        if chr == chract:
            count += 1
        else:
            str_ += chract + str(count)
            chract = chr
            count = 1
    str_ += chract + str(count)
        
    return str_

print(compress("aaabbbccd"))
# -> "a3b3c2d1"
print(compress("abcd"))
# -> "a1b1c1d1"