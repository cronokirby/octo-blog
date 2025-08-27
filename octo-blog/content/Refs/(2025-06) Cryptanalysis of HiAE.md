---
published: "2025-06-23"
link: "https://eprint.iacr.org/2025/1180"
authors: ["[[Alexander Bille]]", "[[Elmar Tischhauser]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We describe key recovery attacks on the authenticated stream cipher HiAE, which was recently proposed for future high-throughput communication networks such as 6G by Huawei.  HiAE uses a 2048-bit state, a 256-bit key and produces 128-bit tags, targeting 256-bit security against key and state recovery.  As a nonce-based AEAD scheme, it relies on the uniqueness of the nonce per key for these security claims. Our analysis indicates that a complete recovery of the 256-bit key of HiAE is possible with a complexity of $2^{128}$ data and at most $2^{129.585}$ time in the nonce-respecting attack setting, with various small tradeoffs concerning the data and time complexity.  While infeasible in practice, this attack therefore violates the 256-bit security claim for HiAE.   We describe further complete key-recovery attacks in the nonce-misuse and release of unverfied plaintext (RUP) settings which require only a small constant number of repeated nonces or unverified decryption queries, respectively.