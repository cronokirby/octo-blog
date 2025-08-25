---
published: "2024-11-19"
link: "https://eprint.iacr.org/2024/1886"
authors: ["[[Cas Cremers]]", "[[Niklas Medinger]]", "[[Aurora Naska]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Modern secure communication systems, such as iMessage, WhatsApp, and Signal include intricate mechanisms that aim to achieve very strong security properties. These mechanisms typically involve continuously merging in new fresh secrets into the keying material, which is used to encrypt messages during communications. In the literature, these mechanisms have been proven to achieve forms of Post Compromise Security (PCS): the ability to provide communication security even if the full state of a party was compromised some time in the past. However, recent work has shown these proofs do not transfer to the end-user level, possibly because of usability concerns. This has raised the question of whether end-users can actually obtain PCS or not, and under which conditions.
> 
> Here we show and formally prove that communication systems that need to be resilient against certain types of state loss (which can occur in practice) fundamentally cannot achieve full PCS for end-users.  Whereas previous work showed that the Signal messenger did not achieve this with its current session-management layer,  we isolate the exact conditions that cause this failure, and why this cannot be simply solved  in communication systems by implementing a different session-management layer or an entirely different protocol. Moreover, we clarify the trade-off of the maximum number of sessions between two users (40 in Signal) in terms of failure-resilience versus security.
> 
> Our results have direct consequences for the design of future secure communication systems, and could motivate either the simplification of redundant mechanisms, or the improvement of session-management designs to provide better security trade-offs with respect to state loss/failure tolerance.

# Notes
They model messaging frameworks as consisting of a broader conversation, which may be broken up into *sessions*, each of which starts with the establishment of a basic set of keys, which then are used to encrypt messages, potentially being ratcheted, like for [[Signal (messaging)|Signal]]. They assume that there’s a *static* state, which is used to establish new sessions, and a *dynamic* state, used for encryption within a session.

The core result they prove is that it’s not possible to have post-compromise security if the static state can be compromised. Intuitively, this makes sense. When only the dynamic state is compromised, then you can recover by using the static state to reestablish communication. With the static state compromised, there’s no difference between your knowledge and that of the adversary.

The way they prove this is a bit odd, they use [[Tamarin Prover|Tamarin]] to model-check that certain scenarios are impossible. This makes sense given the authors, but I think suffers from two flaws:
- While providing confidence, a model-checked result like this doesn’t, technically, constitute a proof of impossibility.
- By not proving the result directly (or in a theorem prover), we don’t learn how to prove similar results more easily.

Another issue with model checking is that it makes understanding the validity of their analysis very much contingent on the details of how they’ve encoded it into the program. When proving that something is impossible by having the model checker fail, the result is fragile, in that mistakes in formalization will lead to false positives. When attempting to prove something positively, generally mistakes in the formalization are repairable, and still directionally correct.