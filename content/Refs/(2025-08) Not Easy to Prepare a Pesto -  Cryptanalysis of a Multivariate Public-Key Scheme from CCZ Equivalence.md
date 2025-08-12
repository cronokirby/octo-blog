---
published: "2025-08-11"
link: "https://eprint.iacr.org/2025/1452"
authors: ["[[Christof Beierle]]", "[[Patrick Felke]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> Multivariate cryptography is one of the challenging candidates for post-quantum cryptography. There exists a huge variety of proposals, most of them have been broken substantially. Multivariate schemes are usually constructed by applying two secret affine invertible transformations $\mathcal S,\mathcal T$ to a set of multivariate
> polynomials $\mathcal{F}$ (often quadratic). The secret polynomials $\mathcal{F}$
> possess a trapdoor that allows the legitimate user to find a solution of the
> corresponding system, while the public polynomials $\mathcal G=\mathcal
> S\circ\mathcal F\circ\mathcal T$ look like random polynomials. In [Calderini, M., Caminata, A., Villa, I. A New Multivariate Primitive from CCZ Equivalence. J. Cryptol. 38, 25 (2025)], the authors addressed the above challenge by presenting a promising new way of constructing a multivariate scheme by considering the CCZ equivalence, which has been introduced and studied in the context of vectorial Boolean functions. The resulting proposal is called Pesto with security parameters $s,t,m,n,q$, where $n$ is the number of variables, $s,t,m\leq n$ and $q$ the size of the finite base field $\mathbb{F}_q$.  In this paper we present an attack against Pesto by constructing an equivalent secret key from the public key. This attack has a precomputation phase with a complexity of \[\textrm{max}\left\{{\mathcal{O}\left(n^{6}(m-t)\right),\mathcal{O}\left(\frac{(m-t)(n-t)^2(n-t-s)q^s}{\mathcal{P}(q,n-t-s)}\right)}\right\}\] 
> base field operations on average and an online complexity of \[\mathcal{O}(q^s(m-t)(n-t-s) \cdot \min(m-t,n-t-s) + q^st (n-t)^2 + q^st^3)\] base field operations to decipher a message or forge a signature, where $\mathcal{P}(q,k) := \prod_{i=1}^k (1-1/q^i)$.  
> Thus, our attack breaks Pesto for any practical choice of the security parameters $n,m,s,t,q$ and renders the concrete construction underlying Pesto insecure.