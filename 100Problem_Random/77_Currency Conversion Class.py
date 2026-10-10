class CurrencyConverter:
    dict_ = {
            "EUR" : 0.85,
            "GBP" : 0.75,
            "JPY" : 110,
            "THB" : 32,
            "USD" : 1
        }
    
    def __init__(self, amount: float, currency: str):
        self.usd = (amount / self.dict_.get(currency.upper()))
    def convert_to(self, target_currency: str) -> float:
        return (self.usd * self.dict_.get(target_currency.upper()))

def menu():
    
    amount = float(input("จำนวนเงิน : "))
    currency = input("ค่าเงินแรก : ")
    target_currency = input("ค่าเงินปลาย : ")

    curren = CurrencyConverter(amount, currency)

    print(f"{amount} {currency} is equal to {round(curren.convert_to(target_currency), 2)} {target_currency}")

menu()