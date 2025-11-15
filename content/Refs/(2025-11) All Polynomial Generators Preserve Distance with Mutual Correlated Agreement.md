---
published: "2025-11-06"
link: "https://eprint.iacr.org/2025/2051"
authors: ["[[Sarah Bordage]]", "[[Alessandro Chiesa]]", "[[Ziyi Guan]]", "[[Ignacio Manzur]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> A generator is a function that maps a random seed to a list of coefficients. We study generators that preserve distance to a linear code: the linear combination of any list of vectors using coefficients sampled by the generator has distance to the code no smaller than that of the original vectors, except for a small error. Distance preservation plays a central role in modern probabilistic proofs, and has been formalized in several ways. We study \emph{mutual correlated agreement}, the strongest known form of distance preservation. 
> 
> We initiate the systematic study of mutual correlated agreement, aiming to characterize the class of generators with this property. Towards this, we study polynomial generators, a rich class that includes all examples of generators considered in the distance preservation literature. Our main result is that \emph{all polynomial generators guarantee mutual correlated agreement for every linear code}. This improves on prior work both in generality (the class of generators covered) and in parameters (the error bounds).
> 
> We additionally provide new results for the case where the linear code is a Reed--Solomon code, which is of particular interest in applications. We prove that all polynomial generators satisfy mutual correlated agreement for Reed–Solomon codes up to the Johnson bound. In particular, we improve upon the state-of-the-art by Ben-Sasson, Carmon, Ishai, Kopparty, and Saraf (FOCS 2020) and resolve a question posed by Arnon, Chiesa, Fenzi, and Yogev (Eurocrypt 2025). 
> 
> Along the way we develop a flexible and general toolbox for mutual correlated agreement, are the first to establish distance preservation for generators that lie beyond polynomial generators.