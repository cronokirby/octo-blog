---
published: "2025-06-20"
link: "https://eprint.iacr.org/2025/1172"
authors: ["[[Yevgeniy Dodis]]", "[[Bernardo Magri]]", "[[Noah Stephens-Davidowitz]]", "[[Yiannis Tselekounis]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Secure messaging protocols allow users to communicate asynchronously over untrusted channels with strong guarantees of privacy, authenticity, forward secrecy, and post-compromise security. However, traditional security analyses of these protocols assume complete trust in the hardware and software of honest participants, overlooking a significant class of real-world threats known as subversion attacks. These attacks alter cryptographic algorithms to compromise security, by exfiltrating secrets or creating vulnerabilities that are often undetected.
> 
> The notion of reverse firewalls (EC'15), aims at protecting against subversion attacks by introducing a third party, called a "reverse firewall" (RF), which sits between a party and the outside world and modifies its  outgoing and incoming messages in a way such that, even if the party's machine has been corrupted (in a way that maintains functionality), security is still preserved. Importantly, the firewall shares no private information with the parties, and parties put no more trust in the firewall than they do in the communication channel. In this work, we address the existing gap in secure messaging and subversion attacks by presenting several key contributions: 
> 
> - We design the first subversion-resilient secure messaging protocol based on the model of RF. Our protocol is based on the Signal protocol---the current state-of-the-art in two-party secure messaging, though it lacks subversion resilience---and achieves subversion resilience with only constant overhead over Signal. 
> 
> - We develop a subversion-resilient version of the X3DH protocol in the RF model. X3DH is a core component that facilitates secure initial key agreement in Signal's protocol. 
> 
> - We introduce and formalize the notion of Continuous Key Agreement with Tamper Detection, an essential concept for subversion-resilient secure messaging. Our notion enables parties to continuously agree on keys, even in the presence of active adversaries capable of partially tampering with the key exchange transcript. We present a construction of our notion and prove its subversion resilience in the model of RF.
