def custom_fizzbuzz(n: int) -> list:
    result = []
    for i in range(1,n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Buzz")
        elif i % 5 == 0:
            result.append("Fizz")
        else:
            result.append(i)
        
    return result


print(custom_fizzbuzz(15))
# -> [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]

#(หารด้วย 3 ลงตัว → "Fizz", หารด้วย 5 ลงตัว → "Buzz", หารด้วยทั้งคู่ → "FizzBuzz")