# LSP - Liskov Substitution Principle

## What I Learned

A subclass should be substitutable for its parent - not just "runs without crashing," but actually honors what the parent's method promises.

In my OCP version, the parent declared `pay(self, order, security_code)` - implying every subclass takes a security code. But `UpiBillingProcessor` stuffed a UPI ID into that same param. Technically it ran fine, but the meaning of that parameter was different for that subclass - which breaks the contract even though nothing crashes.

## What I Changed

Gave each subclass its own honestly-named field in `__init__` instead of forcing one shared param name across all types:

- `DebitBillingProcessor(security_code)`
- `CreditBillingProcessor(security_code)`
- `UpiBillingProcessor(upi_id)`

`pay(order)` is now uniform - no subclass is lying about what data it's holding.

## Takeaway

Substitutability isn't just "doesn't throw an error." It means the subclass genuinely behaves the way the parent's contract implies, so any subclass can replace another without hidden surprises.