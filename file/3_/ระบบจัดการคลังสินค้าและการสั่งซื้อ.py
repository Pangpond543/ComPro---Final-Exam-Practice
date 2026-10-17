def inventory(inven_file):
    while True:
        lines = []
        check = False
        print("1. Add\n2.Remove\n3.Exit")
        menu = int(input("1-3 : "))
        if menu == 1:
            id = input("id : ")
            with open(inven_file, "r", encoding="utf-8") as r1:
                for i in r1:
                    f_data = i.strip().split(",")
                    if id == f_data[0]:
                        print(f"สินค้า :{f_data[1]} จำนวน :{f_data[3]}")
                        qty = int(input("จำนวน เพิ่ม : "))
                        new_qty = int(f_data[3]) + qty
                        f_data[3] = str(new_qty)

                        check = True

                    jf_data = ",".join(f_data) + "\n"
                    lines.append(jf_data)
            print(lines)
            if check:
                with open(inven_file, "w", encoding="utf-8") as w1:
                    w1.writelines(lines)
                    print("เพิ่มสำเร็จ")
            else:
                print(f"ไม่พบสินค้า : {id}")
                yn = input(f"ต้องการสร้างสินค้าใหม่ใช่หรือไม่ id'{id}' y/n : ")
                if yn.lower() == "y":
                    name = input("Name : ")
                    price = float(input("Price : "))
                    qty = int(input("จำนวน : "))
                    with open(inven_file, "a", encoding="utf-8") as a1:
                        a1.write(f"{id},{name},{str(price)},{str(qty)}\n")
                else:
                    continue
                    
        elif menu == 2:
            id = input("id : ")
            with open(inven_file, "r", encoding="utf-8") as r1:
                for i in r1:
                    f_data = i.strip().split(",")
                    if id == f_data[0]:
                        yn = input(f"ต้องการลบ {f_data[1]} y/n : ")
                        if yn.lower() == "y":
                            continue
                        
                    jf_data = ",".join(f_data) + "\n"
                    lines.append(jf_data)
                    
            with open(inven_file, "w", encoding="utf-8") as w1:
                w1.writelines(lines)
                print("ลบสำเร็จ")
            
        elif menu == 3:
            break         

inventory("inventory.txt")