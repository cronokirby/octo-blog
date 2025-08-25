---
published: "2025-07-07"
link: "https://eprint.iacr.org/2025/1254"
authors: ["[[Dan Boneh]]", "[[Evan Laufer]]", "[[Ertem Nusret Tas]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Suppose Alice holds a secret key $\mathsf{sk}$ in a public key encryption scheme. For a given set of ciphertexts, Alice wants to create a short pre-decryption key that lets anyone decrypt this exact set of ciphertexts and nothing else. This problem is called batch decryption. When the secret key $\mathsf{sk}$ is shared among a number of decryption parties the problem is called batch threshold decryption. This question comes up in the context of an encrypted mempool where the goal is to publish a short pre-decryption key that can be used to decrypt all ciphertexts in a block. Prior work constructed batch threshold decryption with some limitations. 
> 
> In this work, we construct three new batch decryption and batch threshold decryption schemes. We first observe that a key-policy ABE (KP-ABE) scheme directly gives a batch decryption scheme. However, the best KP-ABE schemes, which happen to be lattice-based, lead to relatively long public keys and ciphertexts. We then use very different techniques to construct a new lattice-based batch decryption scheme with shorter parameters. Our construction employs a recent preimage sampler due to Waters, Wee, and Wu. Finally, for completeness, we show that a trilinear map leads to a highly efficient threshold batch decryption scheme.