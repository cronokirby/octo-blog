---
published: "2025-11-06"
link: "https://eprint.iacr.org/2025/2048"
authors: ["[[Amit Agarwal]]", "[[Kushal Babel]]", "[[Sourav Das]]", "[[Babak Poorebrahim Gilkalaye]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We introduce time-lock encrypted storage (tTLES), a storage service provided by blockchains. In tTLES, clients store encrypted values towards a future decryption time $\tau_{tgt}$ (measured in block height). The security of tTLES requires that a value is decrypted only if (i) the encrypted value is included in the blockchain, and (ii) the time $\tau_{tgt}$ has passed. This is crucially different from existing schemes, which only enforce either of these conditions but not both. We formalize tTLES, and present an efficient protocol that relies on (in a black-box manner) a threshold identity-based encryption scheme, and a recent batch threshold decryption scheme. Finally, we discuss various applications that will benefit from tTLES.