class Cashier:
    
    def __init__(self):
        self.products = {}
    def add_product(self, name: str, price: float, quantity: int):
        if name not in self.products:
            self.products[name] = {}
            self.products[name]["price"] = price
            self.products[name]["quantity"] = quantity
        else:
            self.products[name]["price"] = price
            self.products[name]["quantity"] += quantity
            
    def remove_product(self, name: str):
        if name not in self.products:
            print(f"\nxxx ไม่พบสินค้า - {name} xxx")
        else:
            self.products.pop(name)
        
    def calculate_total(self) -> float:
        total = 0
        for k, v in self.products.items():
            total += v["price"] * v["quantity"]
        return total
    
    def display_products(self):
        for k, v in self.products.items():
            print(f"{k} - Price: {v["price"]}, Quantity: {v["quantity"]}")
        return (f"Total Cost: {self.calculate_total()}")
    
def menu():
    cashier = Cashier()
    
    while True:
        print("\n1. Add a product. \n2. Remove a product. \n3. Calculate the total cost. \n4. Display all products. \n5. Exit the program.\n")
        num = int(input("เลือกเมณู 1-4: "))
        if num == 1:
            name = input("Name: ")
            price = float(input("price: "))
            quantity = int(input("quantity: "))
            cashier.add_product(name, price, quantity)
        elif num == 2:
            name = input("(Remove) Name: ")
            cashier.remove_product(name)
        elif num == 3:
            print(cashier.calculate_total())
        elif num == 4:
            print(cashier.display_products())
        elif num == 5:
            break
        else:
            print(f"xxx กรอกใหม่ xxx")
        
menu()