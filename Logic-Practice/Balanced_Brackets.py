def is_balanced(expression: str) -> bool:
    stack = []
    
    for i in expression:
        if i == "(" :
            stack.append(i)
        elif i == ")" :
            if "(" not in stack :
                return False
            stack.pop()
            
    return len(stack) == 0


print(is_balanced("(a+b)*(c-d)"))
# -> True
print(is_balanced("((a+b)*(c-d)"))
# -> False
print(is_balanced(")("))
# -> False