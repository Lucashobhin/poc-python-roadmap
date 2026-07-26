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
    def pay(self, order):
        pass


class BillingProcessorSMS(BillingProcessor):
    @abstractmethod
    def auth_sms(self, code):
        pass
    @abstractmethod
    def pay(self, order):
        pass


class DebitBillingProcessor(BillingProcessorSMS):
    def __init__(self, security_code):
        self.security_code = security_code
        self.verified = False
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditBillingProcessor(BillingProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class UpiBillingProcessor(BillingProcessorSMS):
    def __init__(self, upi_id):
        self.upi_id = upi_id
        self.verified = False
    def auth_sms(self, code):
        print(f"Verifying SMS code {code}")
        self.verified = True
    def pay(self, order):
        if not self.verified:
            raise Exception("Not authorized")
        print("Processing UPI payment type")
        print(f"Using UPI ID: {self.upi_id}")
        order.status = "paid"


order = Order()
order.add_item("Paracetamol", 2, 20)
order.add_item("Amoxicillin", 1, 80)
order.add_item("Cough Syrup", 1, 45)

print(order.total_price())
processor = UpiBillingProcessor("shobhin@upi")
processor.auth_sms(465839)
processor.pay(order)