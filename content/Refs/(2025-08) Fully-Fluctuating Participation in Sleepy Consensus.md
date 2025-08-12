---
published: "2025-08-11"
link: "https://eprint.iacr.org/2025/1455"
authors: ["[[Yuval Efron]]", "[[Joachim Neu]]", "[[Toniann Pitassi]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Proof-of-work allows Bitcoin to boast security amidst arbitrary fluctuations in participation of miners throughout time, so long as, at any point in time, a majority of hash power is honest. In recent years, however, the pendulum has shifted in favor of proof-of-stake-based consensus protocols. There, the sleepy model is the most prominent model for handling fluctuating participation of nodes. However, to date, no protocol in the sleepy model rivals Bitcoin in its robustness to drastic fluctuations in participation levels, with state-of-the-art protocols making various restrictive assumptions. In this work, we present a new adversary model, called external adversary. Intuitively, in our model, corrupt nodes do not divulge information about their secret keys. In this model, we show that protocols in the sleepy model can meaningfully claim to remain secure against fully fluctuating participation, without compromising efficiency or corruption resilience. Our adversary model is quite natural, and arguably naturally captures the process via which malicious behavior arises in protocols, as opposed to traditional worst-case modeling. On top of which, the model is also theoretically appealing, circumventing a barrier established in a recent work of Malkhi, Momose, and Ren.