---
published: "2025-07-09"
link: "https://eprint.iacr.org/2025/1266"
authors: ["[[Tom Godden]]", "[[Ruben De Smet]]", "[[Kris Steenhaut]]", "[[An Braeken]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Online services increasingly require users to verify their identity or parts of it, often by law. This verification is usually performed by processing data from official identity documents, like national identity cards. However, these documents often contain significantly more information than the verifying party needs to know, including information that should stay private. Disclosing this information is a significant privacy and security risk for the user.
> Traditional work has designed selective disclosure and zero-knowledge proof protocols for such use cases.
> However, because these require a complete reimplementation, recall and redistribution of existing identity documents, they have never been adopted on a large scale. More recent work has focused on creating zero-knowledge proofs from existing identity documents like the US passport or specific US driver licenses. In this article, we propose an R1CS protocol to efficiently parse and extract fields from existing European National Identity Cards, with an implementation for the Belgian BeID.
> The protocol is able to prove correct extraction of a date-of-birth field in 22 seconds on a consumer device, with verification taking 230 milliseconds. With this, we aim to provide EU citizens with a practical solution to the privacy and security risks that arise when one has to prove their authenticity or authority to a third party.