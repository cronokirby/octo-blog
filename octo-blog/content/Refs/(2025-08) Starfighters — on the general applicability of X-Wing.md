---
published: "2025-08-01"
link: "https://eprint.iacr.org/2025/1397"
authors: ["[[Deirdre Connolly]]", "[[Kathrin Hövelmanns]]", "[[Andreas Hülsing]]", "[[Stavros Kousidis]]", "[[Matthias Meijers]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> This work presents an exhaustive analysis of QSF, the KEM combiner used by X-Wing (Communications in Cryptology 1(1), 2024). While the X-Wing  paper focuses on the applicability of QSF for combining ML-KEM-768 with X25519, we discuss its applicability for combining other post-quantum KEM with other instantiations of ECDH. 
> 
> To this end, we establish simple conditions that allow one to check whether a KEM is compatible with QSF by proving ciphertext second‑preimage resistance C2PRI for several variants of the Fujisaki–Okamoto (FO) transform. Applying these results to post-quantum KEMs that are either standardized or under consideration for standardization, we show that QSF can also be used with all of these, including ML-KEM-1024, (e)FrodoKEM, HQC, Classic McEliece, and sntrup.
> 
> We also present QSI, a variation of QSF and show that any two KEM can be combined by hashing their concatenated keys. The result is a hybrid KEM which is IND-CCA-secure as long as one of the KEM is IND-CCA- and the other C2PRI-secure.
> 
> Finally, we also analyze QSF and QSI regarding their preservation of the recently introduced family of binding properties for KEM.