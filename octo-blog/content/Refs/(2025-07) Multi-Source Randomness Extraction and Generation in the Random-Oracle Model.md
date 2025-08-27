---
published: "2025-07-08"
link: "https://eprint.iacr.org/2025/1258"
authors: ["[[Sandro Coretti]]", "[[Pooya Farshim]]", "[[Patrick Harasser]]", "[[Karl Southern]]"]
tags: ["cryptography", "paper"]
---

# Abstract

> We study the multi-source randomness extraction and generation properties of the monolithic random oracle (RO), whereby one is tasked with extracting or generating uniform random bits from multiple arbitrary unpredictable sources. We formalize this problem according to the query complexities of the involved parties—sources, distinguishers, and predictors, where the latter are used to define unpredictability.
> 
> We show both positive and negative results. On the negative side, we rule out definitions where the predictor is not at least as powerful as the source or the distinguisher. On the positive side, we show that the RO is a multi-source extractor when the query complexity of the distinguisher is bounded. Our main positive result in this setting is with respect to arbitrary unpredictable sources, which we establish via a combination of a compression argument (Dodis, Guo, and Katz, EUROCRYPT'17) and the decomposition of high min-entropy sources into flat sources.
> 
> Our work opens up a rich set of problems, ranging from statistical multi-source extraction with respect to unbounded distinguishers to novel decomposition techniques (Unruh, CRYPTO'07; Coretti et al., EUROCRYPT'18) and multi-source extraction for non-monolithic constructions.