---
published: "2025-08-02"
link: "https://eprint.iacr.org/2025/1405"
authors: ["[[Michele Ciampi]]", "[[Yun Lu]]", "[[Rafail Ostrovsky]]", "[[Vassilis Zikas]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Common blockchain protocols are monolithic, i.e., their security relies on a single assumption, e.g., honest majority of hashing power (Bitcoin) or stake (Cardano, Algorand, Ethereum). In contrast, so-called optimistic approaches (Thunderella, Meshcash) rely on a combination of assumptions to achieve faster transaction liveness.
> 
> We revisit, redesign, and augment the optimistic paradigm to a tiered approach. Our design assumes a primary (Tier 1) and a secondary (Tier 2, also referred to as fallback) blockchain, and achieves full security also in a tiered fashion: If the assumption underpinning the primary chain holds, then we guarantee safety, liveness and censorship resistance, irrespectively of the status of the fallback chain. And even if the primary assumption fails, all security properties are still satisfied (albeit with
> a temporary slow down) provided the fallback assumption holds. To our knowledge, no existing optimistic or tiered approach preserves both safety and liveness when any one of its underlying blockchain (assumptions) fails. The above is achieved by a new detection-and-recovery mechanism that links the two blockchains, so that any violation of safety, liveness, or censorship resistance on the (faster) primary blockchain is temporary—it is swiftly detected and recovered on the secondary chain—and thus cannot result in a persistent fork or halt of the blockchain ledger.
> 
> 
> We instantiate the above paradigm using a primary chain based on proof of reputation (PoR) and a fallback chain based on proof of stake (PoS). Our construction uses the PoR and PoS blockchains in a mostly black-box manner—where rather than assuming a concrete construction we distill abstract properties on the two blockchains that are sufficient for applying our tiered methodology. In fact, choosing reputation as the resource of the primary chain opens the door to an incentive mechanism—which we devise and analyze—that tokenizes reputation in order to deter cheating and boost participation (on both the primary/PoR and the fallback/PoS blockchain). As we demonstrate, such tokenization in combination with interpreting reputation as a built-in system-wide credit score, allows for embedding in our two-tiered methodology a novel mechanism which provides collateral-free, multi-use payment-channel-like functionality where payments can be instantly confirmed.