---
published: "2025-06-27"
link: "https://eprint.iacr.org/2025/1206"
authors: ["[[Ivan Damgård]]", "[[Shravani Patil]]", "[[Arpita Patra]]", "[[Lawrence Roy]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We consider perfectly secure MPC for $n$ players and $t$ malicious corruptions. We ask whether requiring only security with abort (rather than guaranteed output delivery, GOD) can help to achieve protocols with better resilience, communication complexity or round complexity. We show that for resilience and communication complexity, abort security does not help, one still needs $3t< n$ for a synchronous network and $4t< n$ in the asynchronous case. And, in both cases, a communication overhead of $O(n)$ bits per gate is necessary. 
> 
> When $O(n)$ overhead is inevitable, one can explore if this overhead can be pushed to the preprocessing phase and the online phase can be achieved with $O(1)$ overhead. This result was recently achieved in the synchronous setting, in fact, with GOD guarantee. We show this same result in the asynchronous setting. This was previously open since the main standard approach to getting constant overhead in a synchronous on-line phase fails in the asynchronous setting. In particular, this shows that we do not need to settle for abort security to get an asynchronous perfectly secure protocol with overheads $O(n)$ and $O(1)$.
> 
> Lastly, in the synchronous setting, we show that perfect secure MPC with abort requires only 2 rounds, in contrast to protocols with GOD that require 4 rounds.