---
published: "2025-05-30"
link: "https://eprint.iacr.org/2025/1001"
authors: ["[[Elizabeth Crites]]", "[[Alistair Stewart]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The standard notion of security for threshold signature schemes is static security, where the set of corrupt parties is assumed to be fixed before protocol execution. In this model, the adversary may corrupt up to t−1 out of a threshold of t parties. A stronger notion of security for threshold signatures considers an adaptive adversary, who may corrupt parties dynamically based on its view of the protocol execution, learning the corrupted parties’ secret keys as well as their states. Adaptive security of threshold signatures has become an active area of research recently due to ongoing standardization efforts. Of particular interest is full adaptive security, the analogue of static security, where the adversary
> may adaptively corrupt a full t−1 parties.
> 
> We present a plausible attack on the full adaptive security of threshold Schnorr signature schemes with public key shares of the form $pk_i = g^{sk_i},$ where all secret keys $sk_i$ lie on a polynomial. We show that a wide range of threshold Schnorr signature schemes, including all variants of FROST, Sparkle, and Lindell’22, cannot be proven fully adaptively secure without modifications or assuming the hardness of a search problem that we define in this work. We then prove a generalization that extends below t−1 adaptive corruptions.
