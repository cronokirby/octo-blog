---
published: "2025-08-01"
link: "https://eprint.iacr.org/2025/1402"
authors: ["[[Freja Elbro]]", "[[Violetta Weger]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The Syndrome Decoding Problem (SDP) underpins the security of most code-based cryptographic schemes, and Information Set Decoding (ISD) algorithms are the fastest known solvers for most parameter sets. While ISD is well developed in the binary setting, the landscape for non-binary ISD is less mature. Most $q$-ary methods are straightforward generalizations of their binary counterparts, with the recent projective Stern algorithm being the only exception. However, no existing algorithm is designed to leverage the specific algebraic properties of extension fields. This research gap -- highlighted by the first-round NIST PQC proposal SDitH -- motivates our central question: is decoding over an extension field fundamentally easier than over a prime field of similar size?
> 
> This work explores whether the algebraic structure of extension fields can accelerate ISD. We analyze several techniques for translating the SDP to the base field, including the expansion map, subfield subcodes, and the trace map. We also develop new BJMM variants that restrict base list vectors to “small” field elements, aiming to counter the performance loss of advanced ISD when $q$ is large.
> 
> Contrary to our initial intuition, our results provide no evidence of an asymptotic speedup, suggesting that decoding over extension fields is not easier than over prime fields. Additionally, we make two contributions of independent interest: we show that a three-level BJMM algorithm gives a slight improvement over the two-level version for small fields, and we extend Meurer’s proof to show that the complexity of advanced ISD algorithms converges to Prange’s, even when parameters grow simultaneously.