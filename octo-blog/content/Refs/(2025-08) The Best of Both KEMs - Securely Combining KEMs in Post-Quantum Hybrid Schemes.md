---
published: "2025-08-08"
link: "https://eprint.iacr.org/2025/1444"
authors: ["[[Gorjan Alagic]]", "[[Fahran Bajaj]]", "[[Aybars Kocoglu]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Transitioning secure information systems to post-quantum cryptography (PQC) comes with certain risks, such as the potential for switching to PQC schemes with as yet undiscovered vulnerabilities. Such risks can be mitigated by combining multiple schemes in such a way that the resulting hybrid scheme is secure provided at least one of the ingredient schemes is secure. In the case of key-encapsulation mechanisms (KEMs), this approach is already in use in practice, where the PQC scheme ML-KEM is combined with “traditional” X25519 key exchange.
> Combining multiple KEMs to construct a single hybrid KEM is largely straightforward, except for the crucial choice of how to derive the final shared secret key. A generic method for doing this in a manner that preserves IND-CCA security is to include the keys and ciphertexts of all ingredient KEMs in an appropriate key derivation step. In the specialized X-Wing construction, one instead relies on a special property of ML-KEM to avoid including its ciphertext in key derivation.
> In this work, we show that this optimization can be done in a more general setting. Specifically, when combining multiple KEMs one need not include the ciphertext of any KEM that satisfies ciphertext second preimage resistance (C2PRI)—provided the key combination step is performed using a split-key pseudorandom function. We also prove that any KEM constructed from a certain set of Fujisaki-Okamoto (FO) transforms satisfies C2PRI in the random oracle model. This applies to KEMs such as BIKE, Classic McEliece, HQC, and ML-KEM.