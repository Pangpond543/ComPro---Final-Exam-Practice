def analyze_attendance(attendance: list) -> None:
    # แปลง List ข้อมูลการเข้าเรียนในแต่ละวันให้เป็น Set
    days = [set(day) for day in attendance]
    
    # 1. นักเรียนที่มาเรียนครบทุกวัน (ใช้ Intersection หาตัวที่ซ้ำกันทุกวัน)
    all_days = days[0].intersection(*days[1:])
    
    # 2. นักเรียนที่มาวันแรกแต่ไม่มาวันสุดท้าย (ใช้ Difference)
    first_not_last = days[0] - days[-1]
    
    # 3. นักเรียนทั้งหมดที่มาเรียนอย่างน้อย 1 วัน (ใช้ Union หาคนทั้งหมด)
    at_least_one_day = set().union(*days)
    
    # แสดงผลลัพธ์
    print(f"นักเรียนที่มาเรียนครบทุกวัน: {all_days}")
    print(f"นักเรียนที่มาวันแรกแต่ไม่มาวันสุดท้าย: {first_not_last}")
    print(f"จำนวนนักเรียนทั้งหมดที่มาเรียนอย่างน้อย 1 วัน: {len(at_least_one_day)} คน ({at_least_one_day})")


# --- ตัวอย่างการทดสอบ ---
attendance = [
    ["Alice", "Bob", "Charlie", "David"],  # Day 1
    ["Alice", "Charlie", "David"],         # Day 2
    ["Alice", "Bob", "David"],             # Day 3
    ["Alice", "David", "Eve"],             # Day 4
    ["Bob", "Charlie", "David"]            # Day 5
]

analyze_attendance(attendance)