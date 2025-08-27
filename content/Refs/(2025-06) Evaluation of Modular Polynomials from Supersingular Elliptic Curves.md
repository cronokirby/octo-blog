---
published: "2025-06-18"
link: "https://eprint.iacr.org/2025/1154"
authors: ["[[Maria Corte-Real Santos]]", "[[Jonathan Komada Eriksen]]", "[[Antonin Leroux]]", "[[Michael Meyer]]", "[[Lorenz Panny]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We present several new algorithms to evaluate modular polynomials of level $\ell$ modulo a prime $p$ on an input $j$. 
>     More precisely, we introduce two new generic algorithms, sharing the following similarities: they are based on a CRT approach; they make use of supersingular curves and the Deuring correspondence; and, their memory requirements are optimal. 
> 
>     The first algorithm combines the ideas behind a hybrid algorithm of Sutherland in 2013 with a recent algorithm to compute modular polynomials using supersingular curves introduced in 2023 by Leroux. The complexity (holding around several plausible heuristic assumptions) of the resulting algorithm matches the $O(\ell^3 \log^{3} \ell + \ell \log p)$ time complexity of the best known algorithm by Sutherland, but has an optimal memory requirement.    
>     
>     Our second algorithm is based on a sub-algorithm that can evaluate modular polynomials efficiently on supersingular $j$-invariants defined over $\mathbb{F}_p$, and achieves heuristic complexity quadratic in both $\ell$ and $\log j$, and linear in $\log p$. In particular, it is the first generic algorithm with optimal memory requirement to obtain a quadratic complexity in~$\ell$. 
>     
>     Additionally, we show how to adapt our method to the computation of other types of modular polynomials such as the one stemming from Weber's function.  
>     
>     Finally, we provide an optimised implementation of the two algorithms detailed in this paper, though we emphasise that various modules in our codebase
>     may find applications outside their use in this paper.