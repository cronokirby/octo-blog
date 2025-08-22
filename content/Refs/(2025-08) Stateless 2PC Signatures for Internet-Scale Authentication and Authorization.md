---
published: "2025-08-14"
link: "https://eprint.iacr.org/2025/1475"
authors: ["[[Michael Adjedj]]", "[[Geoffroy Couteau]]", "[[Arik Galansky]]", "[[Nikolaos Makriyannis]]", "[[Oren Yomtov]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> The industry is moving away from passwords for authentication and authorization, with hardware devices for storing long-term cryptographic keys emerging as the leading alternative. However, these devices often have limited displays and remain vulnerable to theft, malware, or tricking users into signing malicious payloads. Current systems provide little fallback security in such cases. Any solution must also meet strict requirements: compatibility with industry standards, scalability to handle high request volumes, and high availability.
> 
> We present a novel design for authentication and authorization that meets these demands. Our approach virtualizes the authenticating/authorizing party via a two-party signing protocol with a helper entity, ensuring that keys remain secure even if a device is compromised and that every signed message conforms to a security policy.
> 
> We formalize the required properties for such protocols and show how they are met by existing schemes (e.g., FROST for Schnorr, Boneh–Haitner–Lindell-Segev'25 for ECDSA). Motivated by the widespread use of ECDSA (FIDO2/Passkeys, blockchains), we introduce a new, optimized two-party ECDSA protocol that is significantly more efficient than prior work. At its core is a new variant of exponent-VRF, improving on earlier constructions and of independent interest. We validate our design with a proof-of-concept virtual authenticator for the FIDO2 Passkeys framework.