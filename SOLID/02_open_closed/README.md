# OCP - Open/Closed Principle

## What I Learned

A class should be open for extension, closed for modification - add new behavior without editing existing, working code.

Before, `BillingProcessor` used one `pay()` method with if/elif for each payment type. Adding a new type meant editing that same method again, risking existing logic.

## What I Changed

Made `BillingProcessor` abstract with one method, `pay()`. Each payment type got its own class:

- `DebitBillingProcessor`
- `CreditBillingProcessor`

Adding a new type now just means a new class - existing ones stay untouched.

## Takeaway

Old code stays safe. New features come as new classes, not new conditions.