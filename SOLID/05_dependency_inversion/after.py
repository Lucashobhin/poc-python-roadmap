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

    
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):
    def __init__(self):
        self.authorized = False
    def verify_code(self, code):
        print(f"Verifying SMS code {code}")
        self.authorized = True
    def is_authorized(self) -> bool:
        return self.authorized

    
class AuthorizerCaptcha(Authorizer):
    def __init__(self):
        self.authorized = False
    def not_a_robot(self):
        self.authorized = True
    def is_authorized(self) -> bool:
        return self.authorized

    
class BillingProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class DebitBillingProcessor(BillingProcessor):
    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    def pay(self, order):
        if not self.authorizer.is_authorized():
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


class UpiBillingProcessor(BillingProcessor):
    def __init__(self, upi_id, authorizer: Authorizer):
        self.upi_id = upi_id
        self.authorizer = authorizer
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing UPI payment type")
        print(f"Using UPI ID: {self.upi_id}")
        order.status = "paid"


order = Order()
order.add_item("Paracetamol", 2, 20)
order.add_item("Amoxicillin", 1, 80)
order.add_item("Cough Syrup", 1, 45)

print(order.total_price())
authorizer = AuthorizerCaptcha()
authorizer.not_a_robot()
processor = UpiBillingProcessor("shobhin@upi", authorizer)
processor.pay(order)