from abc import ABC, abstractmethod
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

    
class BillingProcessor(ABC):
    @abstractmethod
    def pay(self, order, security_code):
        pass


class DebitBillingProcessor(BillingProcessor):
    def pay(self, order, security_code):
        print("Processing debit payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


class CreditBillingProcessor(BillingProcessor):
    def pay(self, order, security_code):
        print("Processing credit payment")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"


order = Order()
order.add_item("Paracetamol", 2, 20)
order.add_item("Amoxicillin", 1, 80)
order.add_item("Cough Syrup", 1, 45)

print(order.total_price())
processor = DebitBillingProcessor()
processor.pay(order, "0372846")