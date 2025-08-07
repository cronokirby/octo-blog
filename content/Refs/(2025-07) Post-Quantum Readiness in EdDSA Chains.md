---
published: "2025-07-26"
link: "https://eprint.iacr.org/2025/1368"
authors: ["[[Foteini Baldimtsi]]", "[[Konstantinos Chalkias]]", "[[Arnab Roy]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The impending threat posed by large-scale quantum computers necessitates a reevaluation of signature schemes deployed in blockchain protocols. In particular, blockchains relying on ECDSA, such as Bitcoin and Ethereum, exhibit inherent vulnerabilities due to on-chain public key exposure and the lack of post-quantum security guarantees. Although several post-quantum transition proposals have been introduced, including hybrid constructions and zero-knowledge-based key migration protocols, these approaches often fail to protect inactive "sleeping" accounts, are cumbersome, or require address changes, violating core immutability and full backward compatibility assumptions.
> 
> In this work, we observe that blockchains employing EdDSA with RFC 8032-compliant key derivation (e.g., Sui, Solana, Near, Stellar, Aptos, Cosmos) possess an underexplored structural advantage. Specifically, EdDSA’s hash-based deterministic secret key generation enables post-quantum zero-knowledge proofs of elliptic curve private key ownership, which can help switching to a quantum-safe algorithm proactively without requiring transfer of assets to new addresses.
> 
> We demonstrate how Post-Quantum NIZKs can be constructed to prove knowledge of the "seed" used in EdDSA key derivation, enabling post-quantum-secure transaction authorization without altering addresses or disclosing elliptic curve data. By post-quantum readiness, we mean that with a single user action all future signatures can be made post-quantum secure, even if past transactions used classical elliptic curve cryptography. This allows even users who have previously exposed their public key to seamlessly enter the post-quantum era without transferring assets or changing their account address.
> 
> As part of this analysis, we also show that BIP32-based ECDSA wallets are not post-quantum ready without breaking changes, as they rely on direct scalar exposure in derivation, making backward-compatible upgrades infeasible. In contrast, SLIP-0010  hash-chain based EdDSA private key derivation provides a foundation for seamless, backwards-compatible migration to quantum-safe wallets, supporting secure upgrades even for dormant or legacy accounts.
> 
> This mechanism affords a quantum-resilient path and is the first of its kind that preserves full backward compatibility, supports account abstraction, and critically secures dormant accounts, whether from users or custodians, that would otherwise be compromised under quantum adversaries.