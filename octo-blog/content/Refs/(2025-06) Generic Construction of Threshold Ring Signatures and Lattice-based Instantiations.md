---
published: "2025-06-27"
link: "https://eprint.iacr.org/2025/1205"
authors: ["[[Hao Lin]]", "[[Mingqiang Wang]]", "[[Weiqiang Wen]]", "[[Shi-Feng Sun]]", "[[Kaitai Liang]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> A t-out-of-n threshold ring signature allows $t$ parties to jointly sign a message on behalf of $n$ parties without revealing the identities of the signers. In this paper, we introduce a new generic construction for threshold ring signature, called GCTRS, which can be built on top of a selection on identification schemes, commitment schemes and a new primitive called t-out-of-n proof protocol which is a special type of zero-knowledge proof. In general, our design enables a group of $t$ signers to first generate an aggregated signature by interacting with each other; then they are able to compute a t-out-of-n proof to convince the verifier that the aggregated signature is indeed produced by $t$ individuals among a particular set. The signature is succinct, as it contains only one aggregated signature and one proof in the final signature. We define all the properties required for the building blocks to capture the security of the GCTRS and provide a detailed security proof. Furthermore, we propose two lattice-based instantiations for the GCTRS, named LTRS and CTRS, respectively. Notably, the CTRS scheme is the first scheme that has a logarithmic signature size relative to the ring size. Additionally, during the instantiation process, we construct two t-out-of-n proof protocols, which may be of independent interest.