---
published: "2025-11-14"
link: "https://eprint.iacr.org/2025/2094"
authors: ["[[Darya Kaviani]]", "[[Srinath Setty]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> As digital identity verification becomes increasingly pervasive, existing privacy-preserving approaches are still limited by complex circuit designs, large proof sizes, trusted setups, or high latency. We present Vega, a practical zero-knowledge proof system that proves statements about existing credentials without revealing anything else. Vega is simple, does not require a trusted setup, and is more efficient than the prior state-of-the-art: for a 1920-byte credential, Vega achieves 212 ms proving time, 51 ms verification time, 150 kB proofs, and a 436 kB proving key. At the heart of Vega are two principles that together enable a lightweight proof system that pays only for what it needs. First, fold-and-reuse proving exploits repetition and folding opportunities (i) across presentations, by pushing repeated work to a rerandomizable precomputation; (ii) across uniform hashing steps, by folding many steps into a single step; and (iii) for zero-knowledge, by folding the public-coin transcript with a random one. Second, lookup-centric arithmetization extracts relevant values from credential bytes, both for extracting relevant fields without full in-circuit parsing, and to enable length-hiding hashing.