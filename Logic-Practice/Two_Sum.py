def find_pair(numbers: list, target: int) -> tuple:
    result = []
    for i in range(len(numbers)) :
        for i2 in range(i + 1, len(numbers)):
            # print(numbers[i], numbers[i2])
            if numbers[i] + numbers[i2] == target :
                result.append((numbers[i], numbers[i2]))
    if len(result) == 0:
        return None
    return tuple(result)

print(find_pair([2, 7, 11, 15, 5, 4], 9))
# -> (2, 7)   คู่แรกที่บวกกันได้ 9
print(find_pair([1, 2, 3], 100))
# -> None    ถ้าไม่มีคู่ไหนบวกกันได้ตามเป้า