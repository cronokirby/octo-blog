---
published: "2025-08-08"
link: "https://eprint.iacr.org/2025/1446"
authors: ["[[Giacomo Fenzi]]", "[[Yuwen Zhang]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The argument size of succinct non-interactive arguments (SNARG) is a crucial metric to minimize, especially when the SNARG is deployed within a bandwidth constrained environment.
> 
> We present a non-recursive proof compression technique to reduce the size of hash-based succinct arguments. The technique is black-box in the underlying succinct arguments, requires no trusted setup, can be instantiated from standard assumptions (and even when $\mathsf{P} = \mathsf{NP}$!) and is concretely efficient.
> 
> We implement and extensively benchmark our method on a number of concretely deployed succinct arguments, achieving compression across the board to as much as $60\%$ of the original proof size.
> We further detail non-black-box analogues of our methods to further reduce the argument size.