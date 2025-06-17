---
published: "2025-03-07"
link: "https://eprint.iacr.org/2025/437"
authors: ["[[Antonio Flórez-Gutiérrez]]", "[[Yosuke Todo]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> ChaCha is a widely deployed stream cipher and one of the most important symmetric primitives. Due to this practical importance, many cryptanalysis have been proposed. Until now, Probabilistic Neutral Bits (PNBs) have been the most successful. Given differential-linear distinguishers, PNBs are the technique for key recovery relying on an experimental backward correlation obtained through blackbox analysis. A careful theoretical analysis exploiting the round function design may find a better attack and improve our understanding, but the complicated nature of the ARX structure makes such analysis difficult.  
> %
> We propose a theoretical methodology inspired by bit puncturing, which was recently proposed at Eurocrypt 2024. Our method has a theoretical foundation and is thus fundamentally different from PNBs, to which it is the first effective alternative. As a result, we significantly improved the attack complexity for 6, 7, and 7.5-round ChaCha. The 7-round attack is about $2^{40}$ times faster than the previous best. Furthermore, we propose the first 7.5-round attack with a non-negligible advantage over an exhaustive search.
