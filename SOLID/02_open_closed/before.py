class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    
class BillingProcessor:
    def pay(self, order, payment_type, security_code):
        if payment_type == "debit":
            print("Processing debit payment")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        elif payment_type == "credit":
            print("Processing credit payment")
            print(f"Verifying security code: {security_code}")
            order.status = "paid"
        else:
            raise Exception(f"Unknown payment type: {payment_type}")

        
order = Order()
order.add_item("Paracetamol", 2, 20)
order.add_item("Amoxicillin", 1, 80)
order.add_item("Cough Syrup", 1, 45)

print(order.total_price())
processor = BillingProcessor()
processor.pay(order, "debit", "0372846")