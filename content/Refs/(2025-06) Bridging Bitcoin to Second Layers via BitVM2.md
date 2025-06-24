---
published: "2025-06-18"
link: "https://eprint.iacr.org/2025/1158"
authors: ["[[Robin Linus]]", "[[Lukas Aumayr]]", "[[Zeta Avarikioti]]", "[[Matteo Maffei]]", "[[Andrea Pelosi]]", "[[Orfeas Thyfronitis Litos]]", "[[Christos Stefo]]", "[[David Tse]]", "[[Alexei Zamyatin]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> A holy grail in blockchain infrastructure is a trustless bridge between Bitcoin and its second layers or other chains. We make progress toward this vision by introducing the first light-client based Bitcoin bridge. At the heart of its design lies BitVM2-core, a novel paradigm that enables arbitrary program execution on Bitcoin, combining Turing-complete expressiveness with the security of Bitcoin consensus. BitVM2-bridge advances prior approaches by reducing the trust assumption from an honest majority (t-of-n) to existential honesty (1-of-n) during setup. Liveness is guaranteed with only one rational operator, and any user can act as a challenger, enabling permissionless verification. A production-level implementation of BitVM2 has been developed and a full challenge verification has been executed on the Bitcoin mainnet.