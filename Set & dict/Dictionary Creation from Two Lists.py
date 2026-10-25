def create_employee_dict(names, salaries):
    zip_ = list(zip(names, salaries))
    # print(zip_)
    
    result = {}
    for k, v in zip_:
        if k not in result:
            result[k] = v
        elif v >= result[k]:
            result[k] = v
            
    return result
        
names = ["Alice", "Bob", "Charlie"] 
salaries = [50000, 35000, 60000] 
print(create_employee_dict(names, salaries)) 
# output = {'Alice': 50000, 'Bob': 35000, 'Charlie': 60000}
    
names = ["Alice", "Bob", "Alice", "David", "Eve"] 
salaries = [50000, 35000, 55000, 40000] 

print(create_employee_dict(names, salaries))
# salaries มีแค่ 4 สมาชิก print(create_employee_dict(names, salaries)) 
# output = {'Alice': 55000, 'Bob': 35000, 'David': 40000}