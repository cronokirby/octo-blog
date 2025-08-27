---
published: "2025-06-26"
link: "https://eprint.iacr.org/2025/1198"
authors: ["[[Markku-Juhani O. Saarinen]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We evaluate the implementation aspects of Rijndael-256 using the ratified  RISC-V Vector Cryptography extension Zvkn. A positive finding is that Rijndael-256 can be implemented in constant time with the existing RISC-V ISA as the critical AES and fixed crossbar permutation instructions are in the DIEL (data-independent execution latency) set. Furthermore, simple tricks can be used to expand the functionality of key expansion instructions to cover the additional round constants required. However, due to the required additional byte shuffle in each round, Rijndael-256 will be significantly slower than AES-256 in terms of throughput. Without additional ISA modifications, the instruction count will be increased by the required switching of the  EEW (``effective element width'') parameter in each round between 8 bits (byte shuffle) and 32 bits (AES round instructions). Instruction counts for 1-kilobyte encryption and decryption with Rijndael-256 are factor $2.66\times$ higher than with AES-256. The precise amount of throughput slowdown depends on the microarchitectural details of a particular RISC-V ISA hardware instantiation, but it may be substantial with some high-performance vector AES architectures due to the breakdown of AES pipelining and the relative slowness of crossbar permutation instructions.