---
published: "2025-08-01"
link: "https://eprint.iacr.org/2025/1404"
authors: ["[[Chen-Da Liu-Zhang]]", "[[Christian Matt]]", "[[Søren Eller Thomsen]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Message dissemination is a fundamental building block in distributed systems and guarantees that any message sent eventually reaches all parties. State of the art provably secure protocols for disseminating messages have a per-party communication complexity that is linear in the inverse of the fraction of parties that are guaranteed to be honest in the worst case. Unfortunately, this per-party communication complexity arises even in cases where the actual fraction of parties that behave honestly is close to 1. In this paper, we propose an optimistic message dissemination protocol that adopts to the actual conditions in which it is deployed, with optimal worst-case per-party communication complexity. Our protocol cuts the complexity of prior provably secure protocols for 49% worst-case corruption almost in half under optimistic conditions and allows practitioners to combine efficient heuristics with secure fallback mechanisms.