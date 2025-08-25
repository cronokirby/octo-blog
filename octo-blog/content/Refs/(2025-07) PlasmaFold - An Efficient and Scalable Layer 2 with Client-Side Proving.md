---
published: "2025-07-16"
link: "https://eprint.iacr.org/2025/1300"
authors: ["[[Pierre Daix-Moreux]]", "[[Chengru Zhang]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Despite the growing popularity of blockchains, their scalability remains a significant challenge. Layer-2s (L2s) aim to address this by introducing an operator to process transactions off-chain and post compact summaries to the Layer-1 (L1). However, existing L2 designs struggle with unsatisfactory throughput improvements, complex exit games, limited data availability, or high computational overhead for users.
> 
> This paper introduces PlasmaFold, a novel L2 designed to overcome these limitations. PlasmaFold utilizes a hybrid architecture: an operator (aggregator) generates proofs on server side for the honest construction of blocks, while users maintain balance proofs on their own devices. This separation of concerns enables instant, non-interactive exits via balance proofs, while block proofs handle most of the validations, minimizing users’ costs. By leveraging Incrementally Verifiable Computation (IVC), PlasmaFold achieves concrete efficiency. Users can update their balance proofs within a browser in under 1 second per transaction using less than 1 GB of RAM. Furthermore, only the identities of users who have acknowledged data receipt are posted to L1, ensuring data availability with a minimal on-chain footprint. This design keeps L1 costs extremely low, enabling a theoretical throughput of over 14000 transactions per second.