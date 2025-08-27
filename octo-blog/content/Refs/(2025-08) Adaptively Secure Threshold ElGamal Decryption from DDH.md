---
published: "2025-08-14"
link: "https://eprint.iacr.org/2025/1477"
authors: ["[[Sourav Das]]", "[[Ling Ren]]", "[[Ziling Yang]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Threshold decryption schemes allow a group of decryptors, each holding a private key share, to jointly decrypt ciphertexts. Over the years, numerous threshold decryption schemes have been proposed for applications such as secure data storage, internet auctions, and voting, and recently as a tool to protect against miner-extractable value attacks in blockchain. Despite the importance and popularity of threshold decryption, many natural and practical threshold decryption schemes have only been proven secure against static adversaries. 
> 
> In this paper, we present two threshold decryption schemes that withstand malicious adaptive corruption. Our first scheme is based on the standard ElGamal encryption scheme and is secure against chosen plaintext attack~(CPA). Our second scheme, based on the chosen ciphertext attack~(CCA) secure Shoup-Gennaro encryption scheme, is also CCA secure. Both of our schemes have non-interactive decryption protocols and comparable efficiency to their static secure counterparts. Building on the technique introduced by Das and Ren (CRYPTO 2024), our threshold ElGamal decryption scheme relies on the hardness of Decisional Diffie-Hellman and the random oracle model.