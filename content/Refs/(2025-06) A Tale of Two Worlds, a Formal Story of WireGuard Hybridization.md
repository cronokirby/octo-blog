---
published: "2025-06-23"
link: "https://eprint.iacr.org/2025/1179"
authors: ["[[Pascal Lafourcade]]", "[[Dhekra Mahmoud]]", "[[Sylvain Ruhault]]", "[[Abdul Rahman Taleb]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> PQ-WireGuard is a post-quantum variant of WireGuard
> Virtual Private Network (VPN), where Diffie-Hellman-based key exchange is
> replaced by post-quantum Key Encapsulation Mechanisms-based key
> exchange. In this paper, we first conduct a thorough formal analysis
> of PQ-WireGuard's original design, in which we point out and fix a
> number of weaknesses. This leads us to an improved construction
> PQ-WireGuard*. Secondly, we propose and formally analyze a new
> protocol, based on both WireGuard and PQ-WireGuard*, named
> Hybrid-WireGuard, compliant with current best practices for
> post-quantum transition about hybridization techniques. For our
> analysis, we use the SAPIC+ framework that enables the generation of
> three state-of-the-art protocol models for the verification tools
> ProVerif, DeepSec and Tamarin from a single specification,
> leveraging the strengths of each tool. We formally prove that
> Hybrid-WireGuard is secure. Eventually, we propose a generic, efficient and usable Rust  implementation of our new protocol.