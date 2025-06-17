---
published: "2025-03-25"
link: "https://eprint.iacr.org/2025/554"
authors: ["[[Joseph Jaeger]]", "[[Akshaya Kumar]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We analyze the composition of symmetric encryption and digital signatures in secure group messaging protocols where group members share a symmetric encryption key. In particular, we analyze the chat encryption algorithms underlying MLS, Session, Signal, and Matrix using the formalism of symmetric signcryption introduced by Jaeger, Kumar, and Stepanovs (Eurocrypt 2024). We identify theoretical attacks against each of the constructions we analyze that result from the insufficient binding between the symmetric encryption scheme and the digital signature scheme. In the case of MLS and Session, these translate into practically exploitable replay and reordering attacks by a group-insider. For Signal this leads to a forgery attack by a group-outsider with access to a user’s signing key, an attack previously discovered by Balbás, Collins, and Gajland (Asiacrypt 2023). In Matrix there are mitigations in the broader ecosystem that prevent exploitation. We provide formal security theorems that each of the four constructions are secure up to these attacks. Additionally, in Session we identified two attacks outside the symmetric signcryption model. The first allows a group-outsider with access to an exposed signing key to forge arbitrary messages and the second allows outsiders to replay ciphertexts.
