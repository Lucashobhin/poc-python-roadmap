>>> SRP  Single Responsibility Principle

# What I Learned:

A class should have only one reason to change. It can have multiple methods, but they should all belong to the same responsibility.

In my first implementation, the `Order` class was managing order details and processing payments. 
These are two different responsibilities because changes to payment logic shouldnt affect the order itself.

# What I Changed:

I moved the payment logic into a separate `BillingProcessor` class.
=>  `Order` → Manages items and calculates the total.
=>  `BillingProcessor` → Handles payment and updates the order status.

Now, if payment requirements change, I only need to modify `BillingProcessor`.

## Takeaway

Before adding a new method to a class, I'll ask myself:

**"Does this method belong to this class, or is it a different responsibility?"**
