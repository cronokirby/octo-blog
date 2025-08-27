---
published: "2025-08-11"
link: "https://eprint.iacr.org/2025/1454"
authors: ["[[Maxim Jourenko]]", "[[Marcus Völker]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Designing cryptographic protocols and proving these rigorously secure is an arduous and challenging task. Among the methods commonly used to prove security of cryptographic protocols, formalizing it in Canneti's Universal Composability (UC) Framework offers several benefits: (1) Modular design, (2) demonstrating that security remains under arbitrary composition and concurrent execution, (3) the security against any computationally polynomially bound adversary. However, working within the UC Framework can be cumbersome, requires a long time commitment by the prover, and it is prone to errors. While utilization of proof assistants in Cryptography and IT Security is a prominent research area, proof assistants for UC are still in their infancy. Here we show our ongoing work to utilize model checking for verification of proofs in the UC Framework, which to the best of our knowledge is the first attempt to do so. In this work we (1) formally create a Markov Decision Process (MDP) encoding a given proof in the UC Framework, (2) define and proof notions of soundness and completeness for the constructed MDP, (3) implement a proof of concept and (4) demonstrate practical feasibility through experimental evaluation. In summary, in this work we lay out the formal foundations for model checking UC proofs and create a tool that can not only be used for proof verification but also as an assistant for developing proofs in the UC Framework.