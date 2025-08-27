---
published: "2025-06-13"
link: "https://eprint.iacr.org/2025/1117"
authors: ["[[Suyash Bagad]]", "[[Quang Dao]]", "[[Yuval Domb]]", "[[Justin Thaler]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> At the core of the fastest known SNARKs is the sum-check protocol. In this paper, we describe two complementary optimizations that significantly accelerate sum-check proving in key applications.
> 
> The first targets scenarios where polynomial evaluations involve small values, such as unsigned 32-bit integers or elements of small subfields within larger extension fields. This setting is common in applications such as Jolt, a state-of-the-art zero-knowledge virtual machine (zkVM) built on the sum-check protocol. Our core idea is to replace expensive multiplications over large fields with cheaper operations over smaller domains, yielding both asymptotic speedups and significant constant-factor improvements.
> 
> The second optimization addresses a common pattern where sum-check is applied to polynomials of the form $g(x) = \mathsf{eq}(r, x) \cdot p(x)$, where $\mathsf{eq}$ is the multilinear extension of the equality function. We present a technique that substantially reduces the prover's cost associated with the equality polynomial component. We also describe how to combine both optimizations, which is essential for applications like Spartan within Jolt.
> 
> We have implemented and integrated our optimizations into the Jolt zkVM. Our benchmarks show consistent $2\text{-}3\times$ speedups for proving the first sum-check of Spartan within Jolt, with performance gains reaching 20$\times$ or more when baseline methods approach their memory limits.
