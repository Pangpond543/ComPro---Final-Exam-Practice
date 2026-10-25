def get_unique_consonants(text) :
    result = set()
    
    aeiou = {'a', 'e', 'i', 'o', 'u'}
    for i in text.lower():
        if i.isalpha():
            result.add(i)
            
    return result-aeiou
    
text = "Hello World! 123" 

print(get_unique_consonants(text))
# output = {'h', 'l', 'r', 'd', 'w'}