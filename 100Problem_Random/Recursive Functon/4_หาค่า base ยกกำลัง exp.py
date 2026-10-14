def power(base, exp):
    if exp == 0:
        return  1

    return base * power(base, exp - 1)

print(power(2, 5))   # 32
print(power(5, 0))   # 1