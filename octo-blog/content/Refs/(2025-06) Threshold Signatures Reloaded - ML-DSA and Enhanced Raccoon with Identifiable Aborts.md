---
published: "2025-06-19"
link: "https://eprint.iacr.org/2025/1166"
authors: ["[[Giacomo Borin]]", "[[Sofía Celi]]", "[[Rafael del Pino]]", "[[Thomas Espitau]]", "[[Guilhem Niot]]", "[[Thomas Prest]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Threshold signatures enable multiple participants to collaboratively produce a digital signature, ensuring both fault tolerance and decentralization. As we transition to the post-quantum era, lattice-based threshold constructions have emerged as promising candidates. However, existing approaches often struggle to scale efficiently, lack robustness guarantees, or are incompatible with standard schemes — most notably, the NIST-standard ML-DSA.
> In this work, we explore the design space of Fiat-Shamir-based lattice threshold signatures and introduce the two most practical schemes to date. First, we present an enhanced TRaccoon-based [DKM+24] construction that supports up to 64 participants with identifiable aborts, leveraging novel short secret-sharing techniques to achieve greater scalability than previous state-of-the-art methods. Second — and most importantly — we propose the first practical ML-DSA-compatible threshold signature scheme, supporting up to 6 users.
> We provide full implementations and benchmarks of our schemes, demonstrating their practicality and efficiency for real-world deployment as protocol messages are computed in at most a few milliseconds, and communication cost ranges from 10.5 kB to 525 kB depending on the threshold.