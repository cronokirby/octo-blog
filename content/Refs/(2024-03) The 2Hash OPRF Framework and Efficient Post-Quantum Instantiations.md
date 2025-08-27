---
published: "2024-03-15"
link: "https://eprint.iacr.org/2024/450"
authors: ["[[Ward Beullens]]", "[[Lucas Dodgson]]", "[[Sebastian Faller]]", "[[Julia Hesse]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> An Oblivious Pseudo-Random Function (OPRF) is a two-party protocol for jointly evaluating a Pseudo-Random Function (PRF), where a user has an input x and a server has an input k. At the end of the protocol, the user learns the evaluation of the PRF using key k at the value x, while the server learns nothing about the user's input or output. 
> 
> OPRFs are a prime tool for building secure authentication and key exchange from passwords, private set intersection, private information retrieval, and many other privacy-preserving systems. While classical OPRFs run as fast as a TLS Handshake, current *quantum-safe* OPRF candidates are still practically inefficient. 
> 
> In this paper, we propose a framework for constructing OPRFs from post-quantum multi-party computation. The framework captures a family of so-called "2Hash PRFs", which sandwich a function evaluation in between two hashes. The core of our framework is a compiler that yields an OPRF from a secure evaluation of any function that is key-collision resistant and one-more unpredictable. We instantiate this compiler by providing such functions built from Legendre symbols, and from AES encryption. We then give a case-tailored protocol for securely evaluating our Legendre-based function, built from oblivious transfer (OT) and zero-knowledge proofs (ZKP). Instantiated with lattice-based OT and ZKPs, we obtain a quantum-safe OPRF that completes in 0.57 seconds, with less than 1MB of communication.
