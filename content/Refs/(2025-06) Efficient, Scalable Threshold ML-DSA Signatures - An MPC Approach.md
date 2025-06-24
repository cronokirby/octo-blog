---
published: "2025-06-19"
link: "https://eprint.iacr.org/2025/1163"
authors: ["[[Alexander Bienstock]]", "[[Leo de Castro]]", "[[Daniel Escudero]]", "[[Antigoni Polychroniadou]]", "[[Akira Takahashi]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> A threshold signature is an advanced protocol that splits a secret signing key among multiple parties, allowing any subset above a threshold to jointly generate a signature. While post-quantum (PQ) threshold signatures are actively being studied --- especially in response to NIST's recent call for threshold schemes --- most existing solutions are tailored to specially designed, threshold-friendly signature schemes. In contrast, many real-world applications, such as distributed certificate authorities and digital currencies, require signatures that remain verifiable under the standardized verification procedures already in use. Given NIST's recent standardization of PQ signatures and ongoing industry deployment efforts, designing an efficient threshold scheme that interoperates with NIST-standardized verification remains a critical open problem.
> 
> In this work, we present the first efficient and scalable solution for multi-party generation of the module-lattice digital signature algorithm (ML-DSA), one of NIST's PQ signature standards. Our contributions are two-fold. First, we present a variant of the ML-DSA signing algorithm that is amenable to efficient multi-party computation (MPC) and prove that this variant achieves the same security as the original ML-DSA scheme. Second, we present several efficient & scalable MPC protocols to instantiate the threshold signing functionality. Our protocols can produce threshold signatures with as little as 100 KB (per party) of online communication per rejection-sampling round. In addition, we instantiate our protocols in the honest-majority setting, which allows us to avoid any additional public key assumptions. 
> 
> The signatures produced by our protocols verify under the same implementation of ML-DSA verification for all three security levels. Thus, signatures and verification keys of our scheme are (naturally) the same size as that of ML-DSA; previous lattice-based threshold schemes could not match both of these sizes. Overall, our solution is the only method for producing threshold ML-DSA signatures compatible with NIST-standardized verification that scales to an arbitrary number of parties, without any new assumptions.