---
published: "2025-08-04"
link: "https://eprint.iacr.org/2025/1420"
authors: ["[[Sebastian Angel]]", "[[Sofía Celi]]", "[[Elizabeth Margolin]]", "[[Pratyush Mishra]]", "[[Martin Sander]]", "[[Jess Woods]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We introduce Coral, a system for proving in zero-
> knowledge that a committed byte stream corresponds to a
> structured object in accordance to a Context Free Grammar.
> Once a prover establishes the validity of the parsed object with
> Coral, they can selectively prove facts about the object—such as
> fields in Web API responses or in JSON Web Tokens—–to third
> parties or blockchains. Coral reduces the problem of correct
> parsing to a few simple checks over a left-child right-sibling
> tree and introduces a novel segmented memory abstraction that
> unifies and extends prior constructions for RAM in zkSNARKs.
> Our implementation of Coral runs on a standard laptop, and
> non-interactively proves the parsing of real Web responses
> (JSON) and files (TOML and C) in seconds. The resulting
> proofs are small and cheap to verify.