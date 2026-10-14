def generate_parentheses(n):
    result = []

    def build(current, open_used, close_used):
        if len(current) == 2 * n:                    # สร้างครบแล้ว
            result.append(current)
            return

        if open_used < n:                            # เติม "(" ได้ถ้ายังใช้ไม่ครบ n
            build(current + "(", open_used + 1, close_used)

        if close_used < open_used:                   # เติม ")" ได้ถ้ามี "(" เปิดค้างอยู่
            build(current + ")", open_used, close_used + 1)

    build("", 0, 0)
    return result

print(generate_parentheses(3))
# ["((()))", "(()())", "(())()", "()(())", "()()()"]