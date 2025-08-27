---
published: "2024-10-09"
link: "https://eprint.iacr.org/2024/1609"
authors: ["[[Martijn Brehm]]", "[[Binyi Chen]]", "[[Ben Fisch]]", "[[Nicolas Resch]]", "[[Ron D. Rothblum]]", "[[Hadas Zeilberger]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> In this work we construct a new and highly efficient multilinear polynomial commitment scheme (MLPCS) over binary  fields, which we call \emph{Blaze}.    Polynomial commitment schemes allow a server to commit to a large polynomial and later decommit to its evaluations. Such schemes have emerged as a key component in recent efficient SNARK constructions.
>     
> Blaze has an extremely efficient prover, both asymptotically and concretely. The commitment is dominated by $8n$ field additions (i.e., XORs) and one Merkle tree computation. The evaluation proof generation is dominated by $6n$ additions and $5n$ multiplications over the field. The verifier runs in time $O_\lambda(\log^2(n))$. Concretely, for sufficiently large message sizes, the prover is faster than all prior schemes except for Brakedown (Golovnev et al., Crypto 2023), but offers significantly smaller proofs than the latter.
> 
> The scheme is obtained by combining two ingredients:
> 
> 1. Building on the code-switching technique (Ron-Zewi and Rothblum, JACM 2024), we show how to compose any error-correcting code together with an interactive oracle proof of proximity (IOPP) underlying existing MLPCS constructions, into a new MLPCS. The new MLPCS inherits its proving time from the code's encoding time, and its verification complexity from the underlying MLPCS. The composition is distinctive in that it is done purely on the information-theoretic side.
> 
> 2. We apply the above methodology using an extremely efficient error-correcting code known as the Repeat-Accumulate-Accumulate (RAA) code. We give new asymptotic and concrete bounds, which demonstrate that (for sufficiently large message sizes) this code has a better encoding time vs. distance tradeoff than previous linear-time encodable codes that were considered in the literature.
