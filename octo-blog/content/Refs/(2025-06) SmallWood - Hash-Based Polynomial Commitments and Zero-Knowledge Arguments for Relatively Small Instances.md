---
published: "2025-06-09"
link: "https://eprint.iacr.org/2025/1085"
authors: ["[[Thibauld Feneuil]]", "[[Matthieu Rivain]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Zero-knowledge proofs (ZKPs) are a fundamental building block in cryptography, enabling powerful privacy-preserving and verifiable computations. In the post-quantum era, hash-based ZKPs have emerged as a promising direction due to their conjectured resistance to quantum attacks, along with their simplicity and efficiency.
> 
> In this work, we introduce SmallWood, a hash-based polynomial commitment scheme (PCS) and zero-knowledge argument system optimized for relatively small instances. Building on the recent degree-enforcing commitment scheme (DECS) from the Threshold-Computation-in-the-Head (TCitH) framework, we refine its formalization and combine it with techniques from Brakedown. This results in a new hash-based PCS that is particularly efficient for polynomials of relatively small degree —typically up to $2^{16}$— outperforming existing approaches in this range.
> 
> Leveraging this new PCS, we design a hash-based zero-knowledge argument system that outperforms the state-of-the-art in terms of proof sizes for witness size ranging from $2^6$ to $2^{16}$. Additionally, we present exact zero-knowledge arguments for lattice-based problems using SmallWood, demonstrating highly competitive performance: our scheme yields proof sizes under 25 KB across a wide range of lattice parameters, including Kyber and Dilithium instances.
