---
published: "2025-08-07"
link: "https://eprint.iacr.org/2025/1439"
authors: ["[[Malte Andersch]]", "[[Cezary Pilaszewicz]]", "[[Marian Margraf]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The development of cryptographic schemes which remain secure in the post-quantum era is an urgent challenge, particularly in light of the growing ubiquity of low-power devices and the looming threat of quantum computing. Identity-Based Encryption (IBE) offers a compelling alternative to traditional Public Key Infrastructures by simplifying key management, but most classical IBE schemes rely on number-theoretic assumptions that are vulnerable to quantum attacks. In response, Koshiba and Takashima proposed a novel approach based on Isogenous Pairing Groups (IPGs) [11], claiming partial quantum resistance. In this work, we critically examine their construction and security claims. We show that the proposed scheme, despite its theoretical elegance, reduces to the Elliptic Curve Discrete Logarithm Problem (ECDLP) on supersingular curves, which can be broken in polynomial time by quantum algorithms and in subexponential time classically. Our analysis reveals structural weaknesses inherent to the IPG framework, such as the use of explicit group elements in prime-order groups and exploitable isogeny homomorphisms, which undermine its claimed security guarantees. These findings suggest that IPG-based constructions, in their current form, are unlikely to provide robust post-quantum security.