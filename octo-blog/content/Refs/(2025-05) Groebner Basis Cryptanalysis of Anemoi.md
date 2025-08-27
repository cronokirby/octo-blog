---
published: "2025-05-07"
link: "https://eprint.iacr.org/2025/814"
authors: ["[[Luca Campa]]", "[[Arnab Roy]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Arithmetization-Oriented (AO) symmetric primitives play an important role in the efficiency and security of zero-knowledge (ZK) proof systems. The design and cryptanalysis of AO symmetric-key primitives is a new topic particularly focusing on algebraic aspects. An efficient AO hash function aims at lowering the multiplicative complexity in the arithmetic circuit of the hash function over a suitable finite field. The AO hash function Anemoi was proposed in CRYPTO 2023.   
> 
> In this work we present an in-depth Groebner basis (GB) cryptanalysis of Anemoi over GF(p). The main aim of any GB cryptanalysis is to obtain a well-structured set of polynomials representing the target primitive, and finally solve this system of polynomials using an efficient algorithm.
> 
> We propose a new polynomial modelling for Anemoi that we call ACICO. We show that using ACICO one can obtain a GB defined by a well-structured set of polynomials. Moreover, by utilising ACICO we can prove the exact complexity of the Groebner basis computation (w.r.t Buchberger's algorithm) in the cryptanalysis of Anemoi. The structured GB further allows us to prove the dimension of the quotient space which was conjectured in a recently published work. 
> Afterwards, we provide the complexity analysis for computing the variety (or the solutions) of the GB polynomial system (corresponding to Anemoi) which is the final step in GB cryptanalysis, by using known approaches. In particular, we show that GB polynomial structure allows us to use the Wiedemann algorithm and improve the efficiency of cryptanalysis compared to previous works.
> 
> Our GB cryptanalysis is applicable to more than two branches (a parameter in Anemoi), while the previously published results showed cryptanalysis only for two branches. Our complexity analysis implies that the security of Anemoi should not be relied upon the GB computation.
> 
> We also address an important mathematical question in GB cryptanalysis of Anemoi namely, does the Anemoi polynomial system has a Shape form?, positively. By proving this we guarantee that upon application of basis conversion method like FGLM one can obtain a convenient system of polynomials that is easy to solve.
