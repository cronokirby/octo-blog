---
published: "2025-08-14"
link: "https://eprint.iacr.org/2025/1474"
authors: ["[[Jonas Janneck]]", "[[Jonas Meers]]", "[[Massimo Ostuzzi]]", "[[Doreen Riepel]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> An Authenticated Key Encapsulation Mechanism (AKEM) combines public-key encryption and digital signatures to provide confidentiality and authenticity.
> AKEMs build the core of Hybrid Public Key Encryption (RFC 9180) and serve as a useful abstraction for messaging applications like the Messaging Layer Security (MLS) protocol (RFC 9420) and Signal's X3DH protocol. To date, most existing AKEM constructions either rely on classical (non post-quantum) assumptions or on unoptimized black-box approaches leading to suboptimal efficiency.
> 
> In this work, we choose a different abstraction level to combine KEMs and identification schemes more efficiently by leveraging randomness reuse. We construct a generic scheme and identify the necessary security requirements on the underlying KEM and identification scheme when reusing parts of their randomness. This allows for a concrete instantiation from isogenies based on the POKÉ KEM (EUROCRYPT'25) and the SQIsignHD identification scheme (EUROCRYPT'24). To be used in our black-box construction, the identification scheme requires the more advanced security property of response non-malleability. Hence, we further show that a slight modification of SQIsignHD satisfies this notion, which might be of independent interest.
> 
> Putting everything together, our final scheme yields the most compact AKEM from PQ assumptions with public keys of 366 bytes and ciphertexts of 216 bytes while fulfilling the strongest confidentiality and authenticity notions.