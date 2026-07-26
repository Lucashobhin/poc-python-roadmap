# ISP - Interface Segregation Principle

## What I Learned

A class shouldn't be forced to implement methods it doesn't need. If an interface is too fat, split it into smaller, focused ones.

In my before version, the parent `BillingProcessor` had an abstract `auth_sms()` method - meaning every subclass had to implement it. But `CreditBillingProcessor` doesn't support SMS auth at all, so it was forced to raise an exception just to satisfy the interface. That's the violation - being forced to implement something meaningless to you.

## What I Changed (two attempts)

**First attempt - inheritance:** Split into `BillingProcessor` (just `pay`) and `BillingProcessorSMS` (adds `auth_sms`). `CreditBillingProcessor` only extends the base, `DebitBillingProcessor`/`UpiBillingProcessor` extend the SMS variant. This fixed ISP, but adding another auth type later (say fingerprint) would mean another subclass tier - gets messy fast.

**Final version - composition:** Instead of inheritance tricks, made `SMSAuthorizer` a separate standalone class with its own `verify_code()` and `is_authorized()`. Processors that need SMS auth just hold an authorizer object in their constructor (`self.authorizer = authorizer`) and call `is_authorized()` before paying. `CreditBillingProcessor` simply never gets one - no forced method, no fake implementation.

## Takeaway

If a feature applies to some subclasses but not others, don't force it into a shared parent.
Either split the interface, or better - pull it out as its own object and let classes hold it only if they actually need it.
Composition over inheritance made this cleaner and more flexible for future auth types.