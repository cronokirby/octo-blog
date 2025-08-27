- [Towards Modular Foundations for Protocol Security](https://eprint.iacr.org/2023/187) [[2023-02-13]]
  - Universally composable (UC) security is the most widely used framework for analyzing the security of cryptographic protocols. Many variants and simplifications of the framework have been proposed and developed, nonetheless, many practitioners find UC proofs to be both difficult to construct and understand.
    We remedy this situation by proposing a new framework for protocol security. We believe that our framework provides proofs that are both easier to write, but also more rigorous, and easier to understand. Our work is based on state-separable proofs allowing for modular proofs, by decomposing complicated protocols into simple components.

- [On Security Against Time Traveling Adversaries](https://eprint.iacr.org/2022/1148) [[2022-09-04]]
  - If you had a time machine, what cryptography would you be able to break?
    In this work, we investigate the notion of time travel, formally defining models for adversaries equipped with a time machine, and exploring the consequences for cryptography. We find that being able to rewind time breaks some cryptographic schemes, and being able to freely move both forwards and backwards in time breaks even more schemes.
    We look at the impacts of time travel on encryption and signatures in particular, finding that the **IND-CCA** and **EUF-CMA** security games are broken, while **IND-CPA** and **UUF-CMA** remain secure.

- [MPC for Group Reconstruction Circuits](https://eprint.iacr.org/2022/821) [[2022-06-22]]
  - In this work, we generalize threshold Schnorr signatures, ElGamal encryption, and a wide variety of other functionalities, using a novel formalism of group reconstruction circuits (GRC)s. We construct a UC secure MPC protocol for computing these circuits on secret shared inputs, even in the presence of malicious parties.
    Applied to concrete circuits, our protocol yields threshold signature and encryption schemes with similar round complexity and concrete eﬃciency to functionality-speciﬁc protocols. Our formalism also generalizes to other functionalities, such as polynomial commitments and openings.

- [Constant-Time Arithmetic for Safer Cryptography](https://eprint.iacr.org/2021/1121) [[2021-09-03]]
  - The humble integers,  are the backbone of many
    cryptosystems.
    When bridging the gap from theoretical systems to real-world
    implementations, programmers
    often look towards general purpose libraries
    to implement the arbitrary-precision arithmetic required.
    Alas, these libraries are often conceived without cryptography in mind,
    leaving applications potentially vulnerable to timing attacks.

    To address this, we present saferith, a library providing
    safer arbitrary-precision arithmetic for cryptography, through
    constant-time operations.
