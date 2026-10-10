def calculate_gpa(grades: list) -> float:
    total = 0
    for i in grades:
        if i < 50:
            total += 0
        elif i < 55:
            total += 1
        elif i < 60:
            total += 1.5
        elif i < 65:
            total += 2
        elif i < 70:
            total += 2.5
        elif i < 75:
            total += 3
        elif i < 80:
            total == 3.5
        else: 
            total += 4 
            
    return  float(total / len(grades))

grades = [85, 72, 63, 58, 49]

print(calculate_gpa(grades))