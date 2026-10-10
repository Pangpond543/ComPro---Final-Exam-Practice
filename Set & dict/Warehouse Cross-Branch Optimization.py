branches = { 
    "Branch_A": {"Laptop": 5, "Mouse": 12, "Keyboard": 8, "Monitor": 0}, 
    "Branch_B": {"Mouse": 4, "Keyboard": 15, "Headphones": 6}, 
    "Branch_C": {"Laptop": 2, "Monitor": 7, "Headphones": 0, "Webcam": 10}
}

# * **All Unique Products:** หาชื่อสินค้าทั้งหมดที่มีอยู่ในระบบโดยไม่ซ้ำกัน
# set_2 = set.union(*[set(item_set.keys()) for item_set in branches.values()])
set_ = set()
for branch, product in branches.items():
    for pro, v in product.items():
        set_.add(pro)
print(set_)

# * **Exclusive Products:** หาชื่อสินค้าที่มีปรากฏอยู่ **เพียงสาขาเดียวเท่านั้น** (ไม่ว่าจะหมดสต็อกหรือมีของก็ตาม)
# only = {pro for pro in set_ if sum(pro in bra for bra in branches.values()) == 1}
only_ = set()
for s in set_:
    count = 0
    for bra in branches.values():
        if s in bra:
            count += 1
    if count == 1:
        only_.add(s)
print(only_)

# * **Out of Stock Report:** สร้าง Dictionary ใหม่ที่เก็บเฉพาะรายการสินค้าที่ **หมดสต็อก (จำนวน = 0)** แยกตามสาขา (สาขาไหนไม่มีสินค้าหมดสต็อก ไม่ต้องใส่มาใน Dictionary)

result = {}
for bra, pro in branches.items():
    stock_0 = []
    for p, v in pro.items():
        if v == 0 :
            stock_0.append(p)
    if len(stock_0) > 0 :
        result[bra] = stock_0

print(result)
            
