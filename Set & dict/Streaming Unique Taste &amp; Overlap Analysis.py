user_history = { 
    "User1": ["Inception", "Matrix", "Interstellar", "Avatar"], 
    "User2": ["Matrix", "Interstellar", "Titanic", "Avatar"], 
    "User3": ["Inception", "Interstellar", "Titanic"], 
    "User4": ["Matrix", "Avatar", "Avengers"] 
}

# * **Core Favorites:** หาชื่อหนังที่ถูกดูโดย **อย่างน้อย 3 คนขึ้นไป**
set_all = set.union(*[set(move) for move in user_history.values()])

resut_1 = set()
for a in set_all:
    count = 0
    for u, m in user_history.items():
        if a in m :
            count += 1
    if count >= 3:
        resut_1.add(a)
        
print(resut_1)

# result_1_1 = {a for a in set_all if sum(a in v for v in user_history.values()) == 3} #เขียนย่อบรรทัดเดียว
# print(result_1_1)

# * **Unique Taste Users:** หาว่ามี User คนไหนบ้างที่มี "รสนิยมเฉพาะตัว" (มีหนังที่ดูอยู่คนเดียวโดยที่ไม่มี User คนอื่นดูเลย) พร้อมระบุชื่อหนังเรื่องนั้น
result_2 = {}
for a in set_all:
    count = 0
    for u, m in user_history.items():
        if a in m :
            count += 1
    if count == 1:
        result_2[u] = {a}
print(result_2)

# {'Avatar', 'Interstellar', 'Matrix'}
# {'User4': {'Avengers'}}

# result_2_1 = {u: {a for a in set_all if sum(a in m for u, m in user_history.items()) == 1}} #เขียนย่อบรรทัดเดียว
# print(result_2_1)