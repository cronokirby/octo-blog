---
published: "2025-08-14"
link: "https://eprint.iacr.org/2025/1478"
authors: ["[[Paul Gerhart]]", "[[Davide Li Calsi]]", "[[Luigi Russo]]", "[[Dominique Schröder]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Threshold Schnorr signatures enable $t$-out-of-$n$ parties to collaboratively produce signatures that are indistinguishable from standard Schnorr signatures, ensuring compatibility with existing verification systems. While static-secure constructions are well understood and achieve optimal round complexity, obtaining full adaptive security - withstanding up to $t-1$ dynamic corruptions under standard assumptions has proven elusive: Recent impossibility results (CRYPTO’25) either rule out known proof techniques for widely deployed schemes or require speculative assumptions and idealized models, while positive examples achieving full adaptivity from falsifiable assumptions incur higher round complexity (EUROCRYPT’25, CRYPTO’25).
> 
> We overcome these barriers with the first round-optimal threshold Schnorr signature scheme that, under a slightly relaxed security model, achieves full adaptive security from DDH in the random oracle model. 
> 
> Our model is relaxed in the sense that the adversary may adaptively corrupt parties at any time, but each signer must refresh part of their public key after a fixed number of signing queries. These updates are executed via lightweight, succinct, stateless tokens, preserving the aggregated signature format. Our construction is enabled by a new proof technique, equivocal deterministic nonce derivation, which may be of independent interest.