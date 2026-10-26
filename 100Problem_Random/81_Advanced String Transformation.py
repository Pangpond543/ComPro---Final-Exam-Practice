def advanced_string_transformation(s: str) -> str:
    words = s.split(" ")
    result2 = []
    
    for i in words:
        revers = i[::-1]
        result2.append(revers)
        
    words2 = ' '.join(result2).swapcase()
    
    aeiou = {"a" : "e", "e" :"i", "i" : "o", "o" :"u","u" : "a", "A" : "E", "E" :"I" , "I" :"O", "O" : "U", "U" : "A"}    
    result3 = []
    
    for i in words2:
        if i in aeiou:
            result3.append(aeiou.get(i))
        else:
            result3.append(i)
            
    result4 = []
    count = 0
    for i in result3:
        count += 1
        result4.append(i)
        if count == 3:
            result4.append("#")
            count = 0
    
    return "".join(result4)

print(advanced_string_transformation("Hello World"))
# ULL#Ih #DLR#Uw