---
published: "2025-08-15"
link: "https://eprint.iacr.org/2025/1483"
authors: ["[[Yue Huang]]", "[[Xin Wang]]", "[[Haibin Zhang]]", "[[Sisi Duan]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Conventional Byzantine fault-tolerant protocols focus on the workflow within a group of nodes. In recent years, many applications of consensus involve communication across groups. Examples include communication between infrastructures running replicated state machine, sharding-based protocols, and cross-chain bridges. Unfortunately, little efforts have been made to model the properties for communication across groups. 
> 
> In this work, we propose a new primitive called cross-consensus reliable broadcast (XRBC). The XRBC primitive models the security properties of communication between two groups, where at least one group executes a consensus protocol. We provide three constructions of XRBC under different assumptions and present three different applications for our XRBC protocols: a cross-shard coordination protocol via a case study of Reticulum (NDSS 2024), a protocol for cross-shard transactions via a case study of Chainspace (NDSS 2018), and a solution for cross-chain bridge. Our evaluation results show that our protocols are highly efficient and benefit different applications. For example, in our case study on Reticulum, our approach achieves 61.16% lower latency than the vanilla approach.