---
published: "2016-08-12"
link: "https://eprint.iacr.org/2016/770"
authors: []
tags: ["cryptography", "paper"]
---

# Abstract

> We present KangarooTwelve, a fast and secure arbitrary output-length hash function aiming at a higher speed than the FIPS 202's SHA-3 and SHAKE functions. While sharing many features with SHAKE128, like the cryptographic primitive, the sponge construction, the eXtendable Output Function (XOF) and the 128-bit security strength, KangarooTwelve offers two major improvements over its standard counterpart. First it has a built-in parallel mode that efficiently exploits multi-core or SIMD instruction parallelism for long messages, without impacting the performance for short messages. Second, relying on the cryptanalysis results on Keccak over the past ten years, we tuned its permutation to require twice less computation effort while still offering a comfortable safety margin. By combining these two changes KangarooTwelve consumes less than 0.55 cycles/byte for long messages on the latest Intel's SkylakeX architectures. The generic security of KangarooTwelve is guaranteed by the use of Sakura encoding for the tree hashing and of the sponge construction for the compression function.