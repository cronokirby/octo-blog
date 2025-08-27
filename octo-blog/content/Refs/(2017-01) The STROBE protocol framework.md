---
published: "2017-01-05"
link: "https://eprint.iacr.org/2017/003"
authors: []
tags: ["cryptography", "paper"]
---

# Abstract

> The “Internet of Things” (IoT) promises ubiquitous, cheap, connected devices. Unfortunately, most of these devices are hastily developed and will never receive code updates. Part of the IoT’s security problem is cryptographic, but established cryptographic solutions seem too heavy or too inflexible to adapt to new use cases.
> 
> Here we describe Strobe, a new lightweight framework for building both cryptographic primitives and network protocols. Strobe is a sponge construction in the same family as Markku Saarinen’s BLINKER framework.
> 
> The Strobe framework is simple and extensible. It is suitable for use as a hash, authenticated cipher, pseudorandom generator, and as the symmetric component of a network protocol engine. With an elliptic curve or other group primitive, it also provides a flexible Schnorr signature variant.
> 
> Strobe can be instantiated with different sponge functions for different purposes. We show how to instantiate Strobe as an instance of NIST’s draft cSHAKE algorithm. We also show a lightweight implementation which is especially suitable for 16- and 32- bit microcontrollers, and also for small but high-speed hardware.