```lean
inductive Program (R : Type) (α : Type) where
| Pure : α → Program R α
| Sample : (R → Program R α) → Program R α
| Eq : R → R → (Bool → Program R α) → Program R α
```

Here's a [[Lean]] fragment which defines a basic Monad for doing [[Formal Cryptography]]. You'd want to augment this more with effects for state, exception handling, etc.