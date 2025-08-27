---
published: "2022-03-02"
link: "https://eprint.iacr.org/2022/283"
authors: ["[[Aldo Gunsing]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> First of all we take a thorough look at an error in a paper by Daemen et al. (ToSC 2018) which looks at minimal requirements for tree-based hashing based on multiple primitives, including block ciphers. This reveals that the error is more fundamental than previously shown by Gunsing et al. (ToSC 2020), which is mainly interested in its effect on the security bounds. It turns out that the cause for the error is due to an essential oversight in the interaction between the different oracles used in the indifferentiability proofs. In essence, it reduces the claim from the normal indifferentiability setting to the weaker sequential indifferentiability one. As a matter of fact, this error appeared in multiple earlier indifferentiability papers, including the optimal indifferentiability of the sum of permutations (EUROCRYPT 2018) and the recent ABR+ construction (EUROCRYPT 2021). We discuss in detail how this oversight is caused and how it can be avoided.
> 
> We next demonstrate how the negative effects on the security bound of the construction by Daemen et al. can be resolved. Instead of only allowing a truncated output, we generalize the construction to allow for any finalization function and investigate the security of this for five different types of finalization. Our findings, among others, show that the security of the SHA-2 mode does not degrade if the feed-forward is dropped and that the modern BLAKE3 construction is secure in principle but that its use of the extendable output requires its counter used for random access to be public. Finally, we introduce the tree sponge, a generalization of the sequential sponge construction with parallel absorbing and squeezing.