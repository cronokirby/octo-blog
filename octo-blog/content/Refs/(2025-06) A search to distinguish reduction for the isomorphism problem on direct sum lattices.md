---
published: "2025-06-27"
link: "https://eprint.iacr.org/2025/1204"
authors: ["[[Daniël van Gent]]", "[[Wessel van Woerden]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> At Eurocrypt 2003, Szydlo presented a search to distinguish reduction for the Lattice Isomorphism Problem (LIP) on the integer lattice $\mathbb{Z}^n$. Here the search problem asks to find an isometry between $\mathbb{Z}^n$ and an isomorphic lattice, while the distinguish variant asks to distinguish between a list of auxiliary lattices related to $\mathbb{Z}^n$.
> 
> In this work we generalize Szydlo's search to distinguish reduction in two ways. Firstly, we generalize the reduction to any lattice isomorphic to $\Gamma^n$, where $\Gamma$ is a fixed base lattice. Secondly, we allow $\Gamma$ to be a module lattice over any number field. Assuming the base lattice $\Gamma$ and the number field $K$ are fixed, our reduction is polynomial in $n$.
> 
> As a special case we consider the module lattice $\mathcal{O}_K^2$ used in the module-LIP based signature scheme HAWK, and we show that one can solve the search problem, leading to a full key recovery, with less than $2d^2$ distinguishing calls on two lattices each, where $d$ is the degree of the power-of-two cyclotomic number field and $\mathcal{O}_K$  its ring of integers.