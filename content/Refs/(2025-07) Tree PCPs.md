---
published: "2025-07-07"
link: "https://eprint.iacr.org/2025/1252"
authors: ["[[Tamer Mour]]", "[[Alon Rosen]]", "[[Ron Rothblum]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Probabilistically checkable proofs (PCPs) allow encoding a computation so that it can be quickly verified by only reading a few symbols. Inspired by tree codes (Schulman, STOC'93), we propose tree PCPs; these are PCPs that evolve as the computation progresses so that a proof for time $t$ is obtained by appending a short string to the end of the proof for time $t-1$. At any given time, the tree PCP can be locally queried to verify the entire computation so far.
> 
> We construct tree PCPs for non-deterministic space-s computation, where at time step $t$, the proof only grows by an additional $poly(s,\log(t))$ bits, and the number of queries made by the verifier to the overall proof is $poly(s) \cdot t^\epsilon$, for an arbitrary constant $\epsilon > 0$.
> 
> Tree PCPs are well-suited to proving correctness of ongoing computation that unfolds over time. They may be thought of as an information-theoretic analog of the cryptographic notion of incrementally verifiable computation (Valiant, TCC'08). In the random oracle model, tree PCPs can be compiled to realize a variant of incrementally verifiable computation where the prover is allowed a small number of queries to a large evolving state. This yields the first construction of  (a natural variant of) IVC in the random oracle model.