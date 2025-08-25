---
published: "2025-07-08"
link: "https://eprint.iacr.org/2025/1260"
authors: ["[[Robert Merget]]", "[[Nurullah Erinola]]", "[[Marcel Maehren]]", "[[Lukas Knittel]]", "[[Sven Hebrok]]", "[[Marcus Brinkmann]]", "[[Juraj Somorovsky]]", "[[Jörg Schwenk]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Many protocols, like HTTP, FTP, POP3, and SMTP, were origi-
> nally designed as synchronous plaintext protocols – commands
> and data are sent in the clear, and the client waits for the response
> to a pending request before sending the next one. Later, two main
> solutions were introduced to retrofit these protocols with TLS
> protection. (1) Implicit TLS: Designate a new, well-known TCP
> port for each protocol-over-TLS, and start with TLS immediately.
> (2) Opportunistic TLS: Keep the original well-known port and start
> with the plaintext protocol, then switch to TLS in response to a
> command like STARTTLS.
> In this work, we present a novel weakness in the way TLS is
> integrated into popular application layer protocols through implicit
> and opportunistic TLS. This weakness breaks authentication, even
> in modern TLS implementations if both implicit TLS and oppor-
> tunistic TLS are supported at the same time. This authentication
> flaw can then be utilized to influence the exchanged messages after
> the TLS handshake from a pure MitM position.In contrast to previ-
> ous attacks on opportunistic TLS, this attack class does not rely on
> bugs in the implementations and only requires one of the peers to
> support opportunistic TLS.
> We analyze popular application layer protocols that support
> opportunistic TLS regarding their vulnerability to the attack. To
> demonstrate the practical impact of the attack, we analyze exploita-
> tion techniques for HTTP (RFC 2817) in detail, and show four
> different exploit directions. To estimate the impact of the attack on
> deployed servers, we conducted a series of IPv4-wide scans over
> multiple protocols and ports to check for support of opportunistic
> TLS. We found that support for opportunistic TLS is still widespread
> for many application protocols, with over 3 million servers support-
> ing both, implicit and opportunistic TLS at the same time. In the
> case of HTTP, we found 20,121 servers that support opportunistic
> HTTP across 35 ports, with 2,268 of these servers also supporting
> HTTPS and 539 using the same domain names for implicit HTTPS,
> presenting an exploitable scenario.