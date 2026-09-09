def is_palindrome(text: str) -> bool:
    char_f = [char.lower() for char in text if char.isalnum()]
    
    return char_f == char_f[::-1]


print(is_palindrome("A man a plan a canal Panama"))
# -> True
print(is_palindrome("Hello World"))
# -> False