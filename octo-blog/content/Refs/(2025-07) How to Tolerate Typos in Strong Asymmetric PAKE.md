---
published: "2025-07-30"
link: "https://eprint.iacr.org/2025/1386"
authors: ["[[Ian McQuoid]]", "[[Mike Rosulek]]", "[[Jiayu Xu]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Strong asymmetric password-authenticated key exchange (saPAKE) is the gold standard for password-based authentication. When authenticating using saPAKE, the client holds a cleartext password, and the server holds only a "digest" of the password. The two parties obtain a shared session key if and only if the client password matches the password encoded in the digest.
>     
> In this work we initiate the study of strong asymmetric fuzzy PAKE (safPAKE), which allows the client and server to obtain a shared session key if the client's password is "close enough" to the password encoded in the digest, according to some policy. safPAKE can be used to tolerate incidental password typos in the PAKE setting, which is becoming a standard industry practice outside the PAKE setting. Our safPAKE functionality supports any "typo policy", and our protocol is practical when there are a small number of permissible mistypings of a password.