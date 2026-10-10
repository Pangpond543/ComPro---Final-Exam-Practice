def bank_account_management():
    total = 0
    while True:
        print("1. Deposit Money (ฝากเงิน)\n2. Withdraw Money (ถอนเงิน):\n3. Check Balance (เช็กยอดเงิน):\n4. Exit Program (ออกจากโปรแกรม):")
        menu = int(input("เลือกเมนู 1-4: "))
        if menu == 1:
            Deposit_Money = int(input("กรอกจำนวนเงินที่ต้องการฝาก: "))
            total += Deposit_Money
        elif menu == 2:
            Withdraw_Money = int(input("กรอกจำนวนเงินที่ต้องการถอน: "))
            while True:
                if Withdraw_Money > total:
                    print("ยอดรวม ", total)
                    Withdraw_Money = int(input("เงินในบัญชีไม่พอ กรุณากรอกใหม่: "))
                else:
                    total -= Withdraw_Money
                    print("ถอนเงินเรียบร้อย")
                    print("ยอดถอน ", Withdraw_Money)
                    print("ยอดคงเหลือ: ", total )
                    break
        elif menu == 3 :
            print("ยอดเงิน: ", total)
        elif menu == 4 :
            print("หยุดโปรแกรม")
            break
        
print(bank_account_management())