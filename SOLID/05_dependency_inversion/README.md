# DIP - Dependency Inversion Principle

## What I Learned

High-level modules shouldn't depend directly on low-level, concrete implementations. Both should depend on an abstraction instead.

In my before version, `DebitBillingProcessor`/`UpiBillingProcessor` had `authorizer: AuthorizerSMS` in their constructor - locked to one exact class.
If I wanted a different auth method (captcha, fingerprint, whatever), I'd have to go edit the processor class itself just to change that type hint.

## What I Changed

Created an abstract `Authorizer` class with just one method, `is_authorized()`. Made `AuthorizerSMS` implement it, and added a second, completely different implementation - `AuthorizerCaptcha` (no code to verify, just a direct trigger method `not_a_robot()`). Changed processor constructors from `authorizer: AuthorizerSMS` to `authorizer: Authorizer`.

## Proof It Worked

Swapped `AuthorizerSMS` for `AuthorizerCaptcha` in the demo - a completely different internal mechanism - and `UpiBillingProcessor` needed zero changes. It just worked, because both follow the same `Authorizer` contract.

## Takeaway

Processor shouldn't care exactly how authorization happens internally - only that it can ask "are you authorized?" and get an answer.
Depending on the abstraction instead of a specific class means new auth types can be added later without ever touching the processor code again.