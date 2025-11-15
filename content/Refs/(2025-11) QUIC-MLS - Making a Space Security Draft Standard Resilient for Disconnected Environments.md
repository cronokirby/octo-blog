---
published: "2025-11-07"
link: "https://eprint.iacr.org/2025/2063"
authors: ["[[Benjamin Dowling]]", "[[Britta Hale]]", "[[Xisen Tian]]", "[[Bhagya Wimalasiri]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Among standardization efforts for space and interplanetary
> network security, the Internet Engineering Task Force (IETF) is driv-
> ing work on space network security, accounting for the unique proper-
> ties of space environments that make space communication challenging.
> This includes long, variable-length delays, packet loss, and intermittent
> end-to-end connectivity. Within these efforts, there is a focus on using
> IP-based protocols for security, and in particular the use of the QUIC
> protocol. This is unsurprising given QUIC’s growing popularity and of-
> fer of optimization intended for reducing latency. However, QUIC uses
> the Transport Layer Security (TLS) key exchange handshake protocol,
> which was originally designed for ‘connect and forget’ style Internet con-
> nections at scale. It is also session-based, where protocol participants
> require reestablishment of the session for each reconnection – a costly
> maneuver in the space setting. Furthermore, TLS by default does not
> achieve strong post-compromise security properties within sessions, ex-
> hibiting a risk under long-lived connections, and need for synchronous
> handshakes to counteract this are in functional contrast to the space
> environment, which has intermittent end-to-end connectivity.
> We address both drawbacks of QUIC by introducing QUIC-MLS: a vari-
> ant of QUIC which replaces the session-based, synchronous TLS hand-
> shake with the standardized continuous key agreement protocol, Mes-
> saging Layer Security (MLS), which achieves asynchronous forward se-
> crecy and post-compromise security. In addition to the design itself, we
> implement our design and provide benchmarks, and analyze our new
> construction in a formal cryptographic model.