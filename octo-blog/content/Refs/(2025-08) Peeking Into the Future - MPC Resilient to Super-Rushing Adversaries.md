---
published: "2025-08-01"
link: "https://eprint.iacr.org/2025/1394"
authors: ["[[Gilad Asharov]]", "[[Anirudh Chandramouli]]", "[[Ran Cohen]]", "[[Yuval Ishai]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> An important requirement in synchronous protocols is that, even when a party receives all its messages for a given round ahead of time, it must wait until the round officially concludes before sending its messages for the next round. In practice, however, implementations often overlook this waiting requirement. This leads to a mismatch between the security analysis and real-world deployments, giving adversaries a new, unaccounted-for capability: the ability to ``peek into the future.'' Specifically, an adversary can force certain honest parties to advance to round $r+1$, observe their round $r+1$ messages, and then use this information to determine its remaining round $r$ messages. We refer to adversaries with this capability as ``super-rushing" adversaries.
> 
> We initiate a study of secure computation in the presence of super-rushing adversaries. We focus on understanding the conditions under which existing synchronous protocols remain secure in the presence of super-rushing adversaries. We show that not all protocols remain secure in this model, highlighting a critical gap between theoretical security guarantees and practical implementations. Even worse, we show that security against super-rushing adversaries is not necessarily maintained under sequential composition.
> 
> Despite those limitations, we present a general positive result: secret-sharing based protocols in the perfect setting, such as BGW, or those that are based on multiplication triplets, remain secure against super-rushing adversaries. This general theorem effectively enhances the security of such protocols ``for free.'' It shows that these protocols do not require parties to wait for the end of a round, enabling potential optimizations and faster executions without compromising security. Moreover, it shows that there is no need to spend efforts to achieve perfect synchronization when establishing the communication networks for such protocols.