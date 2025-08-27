---
published: "2023-03-30"
link: "https://eprint.iacr.org/2023/463"
authors: ["[[Benjamin Y Chan]]", "[[Rafael Pass]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We present a theoretical framework for analyzing the efficiency of consensus protocols, and apply it to analyze the optimistic and pessimistic confirmation times of state-of-the-art partially-synchronous protocols in the so-called "rotating leader/random leader" model of consensus (recently popularized in the blockchain setting).
> 
> We next present a new and simple consensus protocol in the partially synchronous setting, tolerating $f < n/3$ byzantine faults; in our eyes, this protocol is essentially as simple to describe as the simplest known protocols, but it also enjoys an even simpler security proof, while matching and, even improving, the efficiency of the state-of-the-art (according to our theoretical framework).
> 
> As with the state-of-the-art protocols, our protocol assumes a (bare) PKI, a digital signature scheme, collision-resistant hash functions, and a random leader election oracle, which may be instantiated with a random oracle (or a CRS).