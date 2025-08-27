---
published: "2025-08-03"
link: "https://eprint.iacr.org/2025/1414"
authors: ["[[Dan Boneh]]", "[[Joachim Neu]]", "[[Valeria Nikolaenko]]", "[[Aditi Partap]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Data availability sampling (DAS) is an important technique to horizontally scale consensus protocols without compromising on the number of adversarial nodes that can be tolerated. DAS is on the technical roadmap of major blockchains such as Ethereum. A major challenge for DAS schemes, that has not been formally studied in the literature, is how incomplete shares can be repaired. The need for repairing data shares motivates key aspects of Ethereum's DAS-based sharding vision called "Danksharding".
> In this work, we make two contributions. First, we provide a new definitional framework that formalizes the notion of repair, along with the security guarantees that a DAS scheme must provide. Second, we propose a new DAS scheme designed with efficient repair in mind, based on locally-correctable multiplicity codes. To facilitate using these codes, we introduce a new multivariate polynomial commitment scheme that (i) supports efficient openings of partial derivatives of a committed polynomial, (ii) supports fast batch opening proof generation at many points, and (iii) has an algorithm to recompute (repair) opening proofs at a point from only a few other proofs. The proposed scheme improves upon the state-of-the-art Ethereum Fulu DAS scheme, slated for deployment in late 2025/early 2026, in storage overhead, repair bandwidth and coordination, while only slightly increasing dispersal cost and sampling bandwidth. Our techniques readily carry over to data availability schemes based on verifiable information dispersal (VID).