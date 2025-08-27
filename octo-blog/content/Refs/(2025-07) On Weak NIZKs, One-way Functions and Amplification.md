---
published: "2025-07-11"
link: "https://eprint.iacr.org/2025/1276"
authors: ["[[Suvradip Chakraborty]]", "[[James Hulett]]", "[[Dakshita Khurana]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> An $(\epsilon_\mathsf{s},\epsilon_{\mathsf{zk}})$-weak non-interactive zero knowledge (NIZK) argument has soundness error at most $\epsilon_\mathsf{s}$ and zero-knowledge error at most $\epsilon_{\mathsf{zk}}$.  We show that as long as $\mathsf{NP}$ is hard in the worst case, the existence of an $(\epsilon_\mathsf{s}, \epsilon_{\mathsf{zk}})$-weak NIZK proof or argument for $\mathsf{NP}$ with $\epsilon_{\mathsf{zk}} + \sqrt{\epsilon_\mathsf{s}} < 1$ implies the existence of one-way functions.  To obtain this result, we introduce and analyze a strong version of universal approximation that may be of independent interest.
> 
> As an application, we obtain NIZK amplification theorems based on very mild worst-case complexity assumptions.  Specifically, [Bitansky-Geier, CRYPTO'24] showed that $(\epsilon_\mathsf{s}, \epsilon_{\mathsf{zk}})$-weak NIZK proofs (with $\epsilon_\mathsf{s}$ and $\epsilon_{\mathsf{zk}}$ constants such that $\epsilon_\mathsf{s} + \epsilon_{\mathsf{zk}} < 1$) can be amplified to make their errors negligible, but needed to assume the existence of one-way functions.  Our results can be used to remove the additional one-way function assumption and obtain NIZK amplification theorems that are (almost) unconditional; only requiring the mild worst-case assumption that if $\mathsf{NP} \subseteq \mathsf{ioP/poly}$, then $\mathsf{NP} \subseteq \mathsf{BPP}$.