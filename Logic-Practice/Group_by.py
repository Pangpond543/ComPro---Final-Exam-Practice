def group_by_first_letter(names: list) -> dict :
    result = {}
    for str in names :
        letter = str[0]
        if letter not in result :
            result[letter] = []
        result[letter].append(str)
        
    return result
            
print(group_by_first_letter(["Anna", "Ben", "Amy", "Bob", "Carl"]))
# -> {"A": ["Anna", "Amy"], "B": ["Ben", "Bob"], "C": ["Carl"]}