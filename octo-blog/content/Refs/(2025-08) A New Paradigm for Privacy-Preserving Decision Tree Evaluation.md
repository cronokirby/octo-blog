---
published: "2025-08-09"
link: "https://eprint.iacr.org/2025/1447"
authors: ["[[Tianpei Lu]]", "[[Bingsheng Zhang]]", "[[Hao Li]]", "[[Kui Ren]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Privacy-preserving decision tree inference is a fundamental primitive in privacy-critical applications such as healthcare and finance, yet existing protocols still pay a heavy price for oblivious selection at every node. We introduce a new paradigm that eliminates this limitation by representing the entire tree as a permutation rather than an explicit set of nodes. 
> Under this representation, we can efficiently generate a shuffled randomized decision tree during the offline phase, where the indices can be directly revealed without leaking any information about the original tree structure. Our scheme significantly reduces both the online and offline computation and communication overhead compared to SOTA.
> Comprehensive benchmarks show an 86 % reduction in online communication versus the state-of-the-art FSS protocol by Ji et al., and a 99.9 % reduction versus the OT-based protocol of Ma et al. Overall, our benchmark shows that our protocol achieves a performance improvement of $20\times$ over Ma et al.’s scheme and $4.5\times$ over Ji et al.’s scheme.