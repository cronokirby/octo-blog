---
published: "2025-08-02"
link: "https://eprint.iacr.org/2025/1406"
authors: ["[[Yifan Song]]", "[[Xiaxi Ye]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> In this work, we study the communication complexity of MPC achieving perfect security with optimal resilience ($t<n/3$). We ask the question: ``Is it possible to build a perfectly secure MPC for arithmetic circuits of size $|C|$ with optimal resilience with communication of $o(|C|\cdot n)$ field elements?''
> 
> On the positive side, we construct a perfectly secure MPC protocol for SIMD circuits with a communication complexity of $O(|C|)$ elements assuming preprocessing data of size $O(|C|)$, where the preprocessing data consists of packed Beaver triples over bivariate polynomials. Furthermore, we show that packed Beaver triples over bivariate polynomials can be prepared at an amortized cost of $O(1)$ elements plus $O(1)$ three-party Beaver triples per secret.
> 
> On the negative side, we establish a communication lower bound proving that preparing packed Beaver triples over bivariate polynomials requires at least $\Omega(n)$ elements of communication per secret. This lower bound is derived by first proving a communication lower bound for verifying the correctness of packed Beaver triples with perfect security with abort, and then efficiently reducing the task of verifying packed Beaver triples to preparing packed Beaver triples over bivariate polynomials. To match this bound, we give a concrete construction for packed Beaver triples over bivariate polynomials with $O(n)$ elements per secret, demonstrating the tightness of our lower bound. 
> 
> Our proof technique also extends to show that for the task of computing the inner-product of two length-$|C|$ vectors, any MPC protocol that achieves perfect security with abort requires either $\Omega(|C|\cdot n)$ elements of communication or $\Omega(|C|)$ elements of preprocessing data.