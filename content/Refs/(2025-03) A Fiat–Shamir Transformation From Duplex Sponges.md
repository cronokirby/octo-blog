---
published: "2025-03-22"
link: "https://eprint.iacr.org/2025/536"
authors: ["[[Alessandro Chiesa]]", "[[Michele Orrù]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We analyze a variant of the Fiat–Shamir transformation based on an ideal permutation. The transformation relies on the popular duplex sponge paradigm, and minimizes the number of calls to the permutation (given the information to absorb/squeeze). This closely models deployed variants of the Fiat–Shamir transformation, and our analysis provides concrete security bounds to guide security parameters in practice. Our results contribute to the ongoing community-wide effort to achieve rigorous, and ultimately formally verified, security proofs for deployed cryptographic proofs. Along the way, we find that indifferentiability (a property proven for many modes of operation, including the duplex sponge) is ill-suited for establishing the knowledge soundness and zero knowledge of a non-interactive argument.
> 
> We additionally contribute spongefish, an open-source Rust library implementing our Fiat–Shamir transformation. The library is interoperable across multiple cryptographic frameworks, and works with any choice of permutation. The library comes equipped with Keccak and Poseidon permutations, as well as several "codecs" for re-mapping prover and verifier messages to the permutation's domain.