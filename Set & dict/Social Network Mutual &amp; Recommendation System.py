friends = { 
    "Alice": {"Bob", "Charlie", "David"}, 
    "Bob": {"Alice", "Charlie", "Eve"}, 
    "Charlie": {"Alice", "Bob", "David", "Eve"}, 
    "David": {"Alice", "Charlie", "Frank"}, 
    "Eve": {"Bob", "Charlie", "Frank"}, 
    "Frank": {"David", "Eve"}
}

#**Mutual Friends:** หาเพื่อนร่วมกันระหว่าง `"Alice"` และ `"Eve"`
Alice_Eve = friends["Alice"].intersection(friends["Eve"])

print("Mutual Friends (Alice & Eve): ", Alice_Eve)
# Mutual Friends (Alice & Eve):  {'Bob', 'Charlie'}


# **Friend Recommendations:** หาคนที่ระบบควร **"แนะนำให้ Alice เพิ่มเป็นเพื่อน"** โดยมีเงื่อนไขดังนี้:
# * ต้อง **ไม่ใช่** คนที่ Alice เป็นเพื่อนอยู่แล้ว
# * ต้อง **ไม่ใช่** ตัว Alice เอง
# * ต้องเป็นคนที่เป็นเพื่อนกับเพื่อนของ Alice **อย่างน้อย 2 คนขึ้นไป**
alice_f = friends["Alice"]
result = set()

for person, friends_ in friends.items():
    if person != "Alice" and person not in alice_f:
        fri_2 = alice_f.intersection(friends_)
        if len(fri_2) >= 2:
            result.add(person)
            
print("Recommended for Alice: ", result)
# Recommended for Alice:  {'Eve'}