---
published: "2025-08-17"
link: "https://eprint.iacr.org/2025/1487"
authors: ["[[Anasuya Acharya]]", "[[Carmit Hazay]]", "[[Vladimir Kolesnikov]]", "[[Manoj Prabhakaran]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> SCALES (Small Clients And Larger Ephemeral Servers) (Acharya et al., TCC 2022, CRYPTO 2024) is a recently proposed model for MPC with several attractive features, including resilience to adaptive corruption. Known SCALES constructions, while offering reasonable asymptotics for large-scale MPC, incur high concrete costs both in computation and communication. 
>     
> As our primary contribution, we dramatically improve both asymptotic and concrete costs of SCALES for permutation branching programs (PBP), a well-motivated practical model of computation. We achieve linear cost in program length, input size, and the security parameter. Our instantiations of the building blocks may be of independent interest.
>     
> Further, we present generic transformations to extend any semi-honestly secure SCALES protocol to achieve (1) guaranteed output delivery in the presence of mixed adversaries (that corrupt servers maliciously and clients semi-honestly) in the all-but-one corruption setting; and (2) protocols for computing general functionalities where each server's computation scales sub-linearly in the function~size.