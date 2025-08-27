---
published: "2025-07-30"
link: "https://eprint.iacr.org/2025/1388"
authors: ["[[Zhiyong Fang]]", "[[Sanjam Garg]]", "[[Bhaskar Roberts]]", "[[Wenxuan Wu]]", "[[Yupeng Zhang]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Collaborative zkSNARKs, proposed by Ozdemir and Boneh in 2022, allow a prover to delegate the generation of zkSNARK proofs to multiple servers, without compromising the confidentiality of the secret witness. They enable the use of zkSNARK techniques on computational limited devices in critical applications such as blockchains. However, the running time of each server is at least as slow as computing the proof on a single server. Garg et al. attempted to improve the efficiency in their scheme named zkSaaS using packed secret sharing, but the scheme still requires a powerful central server with linear computation, communication and memory usage. 
> 
>     In this paper, we propose a new collaborative zkSNARK scheme with $O(\frac{C}{n}\log\frac{C}{n})$ prover time and $O(1)$ proof size with $n$ servers for a circuit of size $C$. An adversary compromising less than $\frac{n}{4}$ servers cannot learn any information about the witness. The core of our technique lies in a new zkSNARK scheme for the Plonkish constraint system that is friendly to packed secret sharing. We utilize bivariate polynomials to avoid a large Fast Fourier Transform on the entire witness, which was the major bottleneck in prior work. We also construct permutation constraints based on logarithmic derivatives and univariate sumcheck to avoid the computation of prefix products. Finally, we build a bivariate polynomial commitment scheme that can be computed directly on packed secret shares. 
>     Experimental results show that for a circuit of size $2^{20}$, with 128 servers, our scheme can accelerate the proof generation by 36.2$\times$ compared to running the zkSNARK on a single server. The prover time of our system is 25.9$\times$ faster than the prior work of zkSaaS. The proof size of our scheme is only 960 Bytes.