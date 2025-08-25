---
published: "2025-06-20"
link: "https://eprint.iacr.org/2025/1171"
authors: ["[[Alberto Leporati]]", "[[Lorenzo Rovida]]", "[[Wessel van Woerden]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We suggest a generalization of homomorphic encryption (HE) schemes from a purely geometrical and lattice-based perspective. All the current reference HE schemes are based on the ring version of the Learning with Errors (LWE) problem. In this proposal, we first investigate LWE-based cryptosystems from a lattice point of view and present a framework that allows to obtain the same result, in geometrical terms, from any lattice — as long as it contains a sufficiently short trapdoor vector. 
> 
> More precisely, we generalize the classical BGV (Brakerski, Gentry and Vaikuntanathan, ITCS '12) and GSW (Gentry, Sahai and Waters, CRYPTO '14) schemes to purely lattice-based variants, which we call Lattice-BGV and Lattice-GSW.
> By abstracting away the particular hardness assumption, our lattice framework allows to be instantiated with a broader range of lattices and hardness assumptions.
> For example, LWE gives a natural trapdoor for random $q$-ary lattices, and when plugged into our framework one obtains the original BGV and GSW schemes, while in this work we will also consider an instantiation based on the Lattice Isomorphism Problem (LIP), leading to the first more advanced cryptographic scheme build from LIP$^*$. Our framework also gives a geometrical and natural explanation of HE procedures and generalizes some properties, such as the ability to store many messages in a single ciphertext, one for each short trapdoor vector, without relying on any particular algebraic structure.
> 
> $^*$ In a concurrent work Branco, Malavolta and Maradni (ePrint 2025/993) propose an alternative LIP-based FHE construction.