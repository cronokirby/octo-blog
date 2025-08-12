---
published: "2025-08-05"
link: "https://eprint.iacr.org/2025/1424"
authors: ["[[Luke Beckwith]]", "[[Andre Esser]]", "[[Edoardo Persichetti]]", "[[Paolo Santini]]", "[[Floyd Zweydinger]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> LESS is a signature scheme based on the code equivalence problem that has advanced to the second round of the NIST PQC standardization process. While promising, the scheme suffers from relatively large signatures and moderate to slow signing and verification times. Chou, Santini, and Persichetti recently introduced a variant of LESS relying on canonical forms to significantly reduce signature sizes. However, the overall performance impact of this approach remained largely unclear. In this work, we provide the first implementation of the new LESS variant and show that, in its original form, it performs poorly due to the overhead of computing canonical forms in a naïve way. We then introduce a series of algorithmic and implementation-level optimizations that reduce this overhead to about 10%, showing that the signature size reduction comes at minor cost. In addition, we present further improvements to the signature scheme as a whole, as well as a re-parameterization. The resulting scheme achieves speedups of 2.5× to 10× over the Round 1 NIST submission, while maintaining the reduced signature sizes.