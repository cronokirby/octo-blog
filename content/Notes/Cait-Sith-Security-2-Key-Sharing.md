---
title: "Cait-Sith Security (2): Key Sharing"
date: "2023-03-13 16:52:30+01:00"
aliases:
  - "../notes/2023/03/cait-sith-security-2-key-sharing"
note-tags:
  - "cait-sith"
  - "cryptography"
  - "protocols"
  - "tss"
katex: "True"
type: "note"
---

So, there'a few steps to defining key sharing,
since we want to reuse some of these intermediate protocols.

Basically, first we define a way to convert additive shares to threshold
shares,
then a way to do key sharing,
but with each of the steps accessible,
then we define a way to do key generation, with each step accessible,
and then then we can collapse all of the steps by performing them in sequence.

The reason we need this "accessible steps" thing is because other protocols
will call them interleaved with other protocols, so we need to be able
to analyze this aspect.

# Conversion

As mentioned above, the goal here is to define a protocol for transforming
additive shares into threshold shares.


**Definition: (Conversion)**

We define the following protocol for conversion.

$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{Convert}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&Z\_{j i}, f_i \gets \bot\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
  &\enspace
    f_i \xleftarrow{\$} \{ f_i \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f_i(0) = 0 \}
  \cr
  &\enspace
    F_i \gets f_i \cdot G
  \cr
  &\enspace
    \text{SetCommit}_i(F_i)
  \cr
  &\enspace
    \text{Commit}_i()
  \cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \text{WaitCommit}_i()
  \cr
\cr
&\underline{
  (1)\text{Share}_i(z_i):
}\cr
  &\enspace
    \text{Open}_i()
  \cr
  &\enspace
    Z_i \gets z_i \cdot G
  \cr
  &\enspace
    \pi_i \gets \text{Prove}_i^\varphi(Z_i; z_i)
  \cr
  &\enspace
    \Rsh_i(\star, (Z_i, \pi_i), 0)
  \cr
  &\enspace
    \Rsh_i(\star, [z_i + f_i(j) \mid j \in [n]], 1)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    F\_\bullet \gets \text{WaitOpen}_i()
  \cr
  &\enspace
    (Z\_{\bullet i}, \pi\_{\bullet i}) \gets \Lsh_i(\star, 0)
  \cr
  &\enspace
    \texttt{if } \exists j.\ \neg \text{Verify}^\varphi(\pi\_{ji}, Z_j)
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 0)
  \cr
  &\enspace
    x\_{\bullet i} \gets \Lsh_i(\star, 1)
  \cr
  &\enspace
    x_i \gets \sum_j x\_{ji},\ Z \gets \sum_j Z_j, \enspace F \gets Z + \sum_j F_j
  \cr
  &\enspace
    \texttt{if } \exists j.\ (\text{deg}(F_j) \neq t - 1 \lor F_j(0) \neq 0) \lor x_i \cdot G \neq F(i):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
    \texttt{return } (x_i, Z)
  \cr
\cr
&\underline{
  \text{Z}_i(j):
}\cr
  &\enspace
    \texttt{return } Z\_{ji}
  \cr
\end{aligned}
}
}
\quad
\begin{matrix}
F[\text{ZK}(\varphi)]\cr
\otimes\cr
F[\text{SyncComm}]\cr
\circledcirc \cr
F[\text{Stop}]
\end{matrix}\cr
\cr
\text{Leakage} := \{\texttt{stop}\}
\end{matrix}
}
\lhd \mathscr{P}[\text{Commit}]
$$

$\square$

The basic idea behind this protocol is that you first commit
to a polynomial you'll use for the threshold sharing,
without committing to the value you want to share.
Then, in a later step, you'll contribute your additive share of the secret
value,
and send threshold shares using this polynomial.

Next, we get to the ideal functionality this protocol implements.
The basic idea is that parties get $z + f(j)$,
where $z$ is the secret, and $f$ is a random polynomial.
One slight catch is that $f$ isn't quite random, but rather
a random polynomial $f^h$, plus a polynomial $f^m$ to which the adversary
must commit in advance, via $f^m \cdot G$.

**Definition (Ideal Conversion):**

$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{IdealConvert}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
  &\enspace
    \text{SetMask}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \text{WaitMask}_i(\star, \texttt{true})
  \cr
\cr
&\underline{
  (1)\text{Share}_i(z):
}\cr
  &\enspace
    \text{Share}_i(\star, z)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\cr
&\underline{
  \text{Z}_i(j):
}\cr
  &\enspace
    \texttt{return } \text{Z}_i(j)
  \cr
\end{aligned}
}
}
\quad
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $F[\text{Convert}]$
}\cr
\cr
&f^h \xleftarrow{\$} \{f \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f(0) = 0\}\cr
&F^m, \text{ready}\_{ij}, z\_{ij}, x_j \gets \bot\cr
\cr
&\underline{
  \text{SetMask}_i(S):
}\cr
  &\enspace
    \text{ready}\_{ij} \gets \texttt{true}\ (\forall j \in S)
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  (1)\text{Cheat}(F):
}
}\cr
  &\enspace
    \texttt{assert } F(0) = 0 \land \text{deg}(F) = t - 1
  \cr
  &\enspace
    F^m \gets F
  \cr
\cr
&\underline{
  \text{WaitMask}_i(S, m):
}\cr
  &\enspace
    \texttt{wait}\_{(i, 0)} \forall j \in S.\ \text{ready}\_{ji} \land (m \to F^m \neq \bot)
  \cr
\cr
&\underline{
  \text{Share}_i(S, z\_\bullet):
}\cr
  &\enspace
    \texttt{assert } \exists j.\ \text{ready}\_{ij}
  \cr
  &\enspace
    z\_{ij} \gets z_j\ (\forall j \in S)
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  \text{CheatShare}(S, \hat{x}\_\bullet):
}
}\cr
  &\enspace
    \texttt{assert } F^m \neq \bot \land \forall j \in S.\ \hat{x}_j \cdot G = F^m(j)
  \cr
  &\enspace
    \texttt{for } j. x_j = \bot: x_j \gets \hat{x}_j
  \cr
\cr
&\underline{
  \text{WaitShare}_i(h):
}\cr
  &\enspace
    \texttt{if } h:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} x_i \neq \bot \land \forall j. \land z\_{ji} \neq \bot
  \cr
  &\enspace\enspace
    \texttt{return } \sum\_j z\_{ji} + f^h(i) + x_i
  \cr
  &\enspace
    \texttt{else}:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} \forall j \in \mathcal{H}. z\_{ji} \neq \bot
  \cr
  &\enspace\enspace
    \texttt{return } \sum\_{j \in \mathcal{H}} z\_{ji} + f^h(i)
  \cr
&\underline{
  \text{Z}_j(i):
}\cr
  &\enspace
    \texttt{return } z\_{ij} \cdot G
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  \text{F}^h():
}
}\cr
  &\enspace
    \texttt{wait } F^m \neq \bot \land \forall i. \exists j. \text{ready}\_{ij}
  \cr
  &\enspace
    \texttt{return } f^h \cdot G
  \cr
\end{aligned}
}
}\cr
\circledcirc \cr
F[\text{Stop}]
\end{matrix}\cr
\cr
\text{Leakage} := \{\texttt{stop}\}
\end{matrix}
}
$$

$\square$

For slight technical reasons, this functionality can't be reduced
to one where the polynomial is simply chosen randomly,
although it's functionally equivalent.
This is because the adversary has to effectively commit to their contribution
to the random polynomial in advance, before having seen any other information,
which thus prevents this contribution from meaningfully affecting the randomness.

In fact, if you have a stronger model of how the group here functions,
like the AGM or something, then in fact this would reduce to the standard
functionality, because you would be able to extract out the discrete
logarithm of the cheating polynomial early.
However, to make the analysis more concrete, we instead deal with this
annoyance of functionality directly.

**Lemma:**

For a negligible $\epsilon$, and up to $t - 1$ malicious corruptions,
we have:
$$
\mathscr{P}[\text{Convert}] \overset{\epsilon}{\leadsto} \mathscr{P}[\text{IdealConvert}]
$$

**Proof:**

First, $\mathscr{P}[\text{Convert}] \leadsto \mathscr{P}^0$,
where $\mathscr{P}^0$ replaces $\mathscr{P}[\text{Commit}]$
with $\mathscr{P}[\text{IdealCommit}]$.

Unrolling, we get:

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^0_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
&\enspace
  \ldots
\cr
\end{aligned}
}
}
\otimes
\boxed{\colorbox{FBCFE8}{\large
  $\Gamma^0_M$
} = 1
\begin{pmatrix}
    \Rsh_k
  ,\cr
    \Lsh_k
  ,\cr
    \text{Prove}_k
  ,\cr
    \text{Verify}
  ,\cr
    \text{SetCommit}_k
  ,\cr
    \text{WaitCommit}_k
  ,\cr
    \text{Open}_k
  ,\cr
    \text{WaitOpen}_k
  ,\cr
    \text{Sync}_k
  ,\cr
    \text{WaitSync}_k
  ,\cr
    \texttt{stop}
\end{pmatrix}
}
\cr
  \circ
\cr
F[\text{ZK}(\varphi)] \otimes F[\text{SyncComm}] \otimes F[\text{Commit}] \otimes F[\text{Sync}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

Next, inline messages to get rid of synchronous communication.
Our goal for now is to simplify the communication patterns, merging
what's going on into a functionality.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^1_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
  &\enspace
    f_i \xleftarrow{\$} \{ f_i \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f_i(0) = s_i \}
  \cr
  &\enspace
    F_i \gets f_i \cdot G
  \cr
  &\enspace
    \text{SetCommit}_i(F_i)
  \cr
  &\enspace
    \text{Commit}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \text{WaitCommit}_i(\star)
  \cr
  &\enspace
    \text{Sync}_i(\star, 0)
  \cr
\cr
&\underline{
  (1)\text{Share}_i(z_i):
}\cr
  &\enspace
    \text{Open}_i(\star)
  \cr
  &\enspace
    Z_i \gets z_i \cdot G
  \cr
  &\enspace
    \pi_i \gets \text{Prove}_i(Z_i; z_i)
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    Z\_{ij} \gets Z_i,\ \pi\_{ij} \gets \pi_i
  $}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    x\_{ij} \gets z_i + f_i(j)
  $}
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \text{WaitSync}_i(\star, 0)
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    F\_\bullet \gets \text{WaitOpen}_i(\star)
  $}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{wait}\_{(i, 1)} \forall j.\ Z\_{ji}, \pi\_{ji} \neq \bot
  $}
  \cr
  &\enspace
    \texttt{if } \exists j.\ \text{deg}(F_j) \neq t - 1 \lor F_j(0) \neq 0 \lor \neg \text{Verify}(\pi\_{ji}, Z\_{ji}):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{wait}\_{(i, 2)} \forall j.\ x\_{ji} \neq \bot
  $}
  \cr
  &\enspace
    x_i \gets \sum_j x\_{ji}, \enspace F \gets \sum_j Z\_{ji} + \sum_j F_j
  \cr
  &\enspace
    \texttt{if } x_i \cdot G \neq F(i):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 2)
  \cr
  &\enspace
    \texttt{return } (x_i, F(0))
  \cr
\end{aligned}
}
}
\otimes
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^1_M$
}\cr
&\ldots\cr
\cr
&\underline{
  \Rsh_k(S, m\_\bullet, 1):
}\cr
  &\enspace
    \forall j \in S.\ (Z\_{kj}, \pi\_{kj}) \gets m\_j
  \cr
\cr
&\underline{
  \Rsh_k(S, m\_\bullet, 2):
}\cr
  &\enspace
    \forall j \in S.\ x\_{kj} \gets m\_j
  \cr
\cr
&\underline{
  \Lsh_k(S, 1):
}\cr
  &\enspace
    \texttt{wait}\_{(k, 1)} \forall j \in S.\ Z\_{jk}, \pi\_{jk} \neq \bot
  \cr
  &\enspace
    \texttt{return } [(Z\_{jk}, \pi\_{jk}) \mid j \in S]
  \cr
\cr
&\underline{
  \Lsh_k(S, 2):
}\cr
  &\enspace
    \texttt{wait}\_{(k, 2)} \forall j \in S.\ x\_{jk} \neq \bot
  \cr
  &\enspace
    \texttt{return } [x\_{jk} \mid j \in S]
  \cr
\end{aligned}
}
}\cr
\otimes\cr1(\ldots)
\end{matrix}
\cr
  \circ
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $F^0$
}\cr
\cr
&F_i, \text{com}\_{ij}, \text{open}\_{ij} \gets \bot\cr
&\texttt{pub } Z\_{ij}, \pi\_{ij}, x\_{ij} \gets \bot\cr
\cr
&\underline{
  (1)\text{SetCommit}_i(F):
}\cr
  &\enspace
    F_i \gets F
  \cr
\cr
&\underline{
  \text{Commit}_i(S):
}\cr
  &\enspace
    \texttt{assert } F_i \neq \bot
  \cr
  &\enspace
    \text{com}\_{ij} \gets \texttt{true}\ (\forall j \in S)
  \cr
\cr
&\underline{
  \text{WaitCommit}_i(S):
}\cr
  &\enspace
    \texttt{wait}\_{(i, 0)} \forall j \in S.\ \text{com}\_{ji}
  \cr
\cr
&\underline{
  \text{Open}_i(S):
}\cr
  &\enspace
    \texttt{assert } F_i \neq \bot
  \cr
  &\enspace
    \text{open}\_{ij} \gets \texttt{true} (\forall j \in S)
  \cr
\cr
&\underline{
  \text{WaitOpen}_i(S):
}\cr
  &\enspace
    \text{wait}\_{(i, 2)} \forall j \in S.\ \text{open}\_{ji}
  \cr
  &\enspace
    \texttt{return } F\_\bullet
  \cr
\end{aligned}
}
}
\otimes
F[\text{ZK}(\varphi)] \otimes F[\text{SyncComm}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

By stopping inside $\Gamma_M$, we can merge the last two messages
more easily.
Any proof not coming from the prove function is false, except with neglible probability.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^2_H$
}\cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \ldots
  \cr
  &\enspace
    \texttt{wait}\_{(i, 1)} \forall j.\ Z\_{ji}, \pi\_{ji} \neq \bot
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{wait}\_{(i, 1)} \forall j.\ x\_{ji} \neq \bot
  $}
  \cr
  &\enspace
    \texttt{if } \exists j.\ \text{deg}(F_j) \neq t - 1 \lor F_j(0) \neq 0 \lor \neg \text{Verify}(\pi\_{ji}, Z\_{ji}):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
    \ldots
  \cr
\end{aligned}
}
}
\otimes
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^2_M$
}\cr
&\ldots\cr
&\colorbox{bae6fd}{$
F_k, \mu[\bullet] \gets \bot
$}\cr
\cr
&\underline{
  (1)\text{SetCommit}_k(F):
}\cr
  &\enspace
  \colorbox{bae6fd}{$
    F_k \gets F
  $}
  \cr
  &\enspace
    \text{SetCommit}_k(F)
  \cr
\cr
&\underline{
  \text{Prove}_k(Z;z):
}\cr
  &\enspace
  \colorbox{bae6fd}{$
    \pi \gets \text{Prove}_k(B;b)
  $}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \mu[\pi] \gets Z
  $}
  \cr
  &\enspace
    \texttt{return } \pi
  \cr
\cr
&\underline{
  \Rsh_k(S, m\_\bullet, 1):
}\cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{for } j \in S \cap \mathcal{H}:
  $}
  \cr
  &\enspace\enspace
  \colorbox{bae6fd}{$
    (Z_j, \pi_j) \gets m_j
  $}
  \cr
  &\enspace\enspace
  \colorbox{bae6fd}{$
    \texttt{if } \text{deg}(F_k) \neq t - 1 \lor F_k(0) \neq 0 \lor \mu[\pi] \neq Z_j
  $}
  \cr
  &\enspace\enspace\enspace
  \colorbox{bae6fd}{$
    \texttt{stop}(\{j\}, 1)
  $}
  \cr
  &\enspace
    \forall j \in S.\ (Z\_{kj}, \pi\_{kj}) \gets m\_j
  \cr
\end{aligned}
}
}\cr
\otimes\cr
1(\ldots)
\end{matrix}
\cr
  \circ
\cr
F^0
\otimes
F[\text{ZK}(\varphi)] \otimes F[\text{SyncComm}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

Next, make it so that we open 3 things at once.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^4_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
  &\enspace
    f_i \xleftarrow{\$} \{ f_i \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f_i(0) = s_i \\}
  \cr
  &\enspace
    F_i \gets f_i \cdot G
  \cr
  &\enspace
    \text{SetCommit}_i(F_i)
  \cr
  &\enspace
    \text{Commit}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \text{WaitCommit}_i(\star)
  \cr
  &\enspace
    \text{Sync}_i(\star, 0)
  \cr
\cr
&\underline{
  (1)\text{Share}_i(z_i):
}\cr
  &\enspace
    Z_i \gets z_i \cdot G
  \cr
  &\enspace
    \pi_i \gets \text{Prove}_i(Z_i; z_i)
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \text{Open}_i(\star, Z_i, \pi_i, z_i + f_i(j))
  $}
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \text{WaitSync}_i(\star, 0)
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    (F\_\bullet, Z\_\bullet, \pi\_\bullet, x\_\bullet) \gets \text{WaitOpen}_i(\star)
  $}
  \cr
  &\enspace
    \texttt{if } \exists j.\ \text{deg}(F_j) \neq t - 1 \lor F_j(0) \neq 0 \lor \neg \text{Verify}(\pi\_{ji}, Z\_{ji}):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
    x_i \gets \sum_j x\_{ji}, \enspace F \gets \sum_j Z\_{ji} + \sum_j F_j
  \cr
  &\enspace
    \texttt{if } x_i \cdot G \neq F(i):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
    \texttt{return } (x_i, F(0))
  \cr
\cr
\end{aligned}
}
}
\otimes
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $\Gamma^4_M$
}\cr
\cr
&\mu[\bullet], \text{open}\_{kj}, \text{sync}\_{kj}, Z\_{kj}, \pi\_{kj}, x\_{kj} \gets \bot\cr
\cr
&\underline{
  (1)\text{SetCommit}_k(F):
}\cr
  &\enspace
    F_k \gets F
  \cr
  &\enspace
    \text{SetCommit}_k(F)
  \cr
\cr
&\underline{
  (1)\text{Prove}_k(Z;z):
}\cr
  &\enspace
    \pi \gets \text{Prove}_k(Z;z)
  \cr
  &\enspace
    \mu[Z] \gets z
  \cr
  &\enspace
    \texttt{return } \pi
  \cr
\cr
&\underline{
  \Rsh_k(S, m\_\bullet, 1):
}\cr
  &\enspace
    \texttt{for } j \in S \cap \mathcal{H}:
  \cr
  &\enspace\enspace
  \colorbox{bae6fd}{$
    (Z_j, \pi_j) \gets m_j
  $}
  \cr
  &\enspace\enspace
  \colorbox{bae6fd}{$
    \texttt{if } \text{deg}(F_k) \neq t - 1 \lor F_k(0) \neq 0 \lor \mu[\pi] \neq Z_j
  $}
  \cr
  &\enspace\enspace\enspace
  \colorbox{bae6fd}{$
    \texttt{stop}(\{j\}, 1)
  $}
  \cr
  &\enspace
    \forall j \in S.\ (Z\_{kj}, \pi\_{kj}) \gets m\_j
  \cr
  &\enspace
    \text{Open?}_k()
  \cr
\cr
&\underline{
  \Rsh_k(S, m\_\bullet, 2):
}\cr
  &\enspace
    \forall j \in S.\ x\_{kj} \gets m\_j
  \cr
  &\enspace
    \text{Open?}_k()
  \cr
\cr
&\underline{
  \Lsh_k(S, 1):
}\cr
  &\enspace
    (\forall j \in \mathcal{H})\ (\bullet, Z\_{jk}, \pi\_{j k}, \bullet) \gets \texttt{nowait } \text{WaitOpen}\_k(\{j\})
  \cr
  &\enspace
    \texttt{wait}\_{(k, 3)} \forall j \in S.\ Z\_{jk}, \pi\_{jk} \neq \bot
  \cr
  &\enspace
    \texttt{return } [(Z\_{jk}, \pi\_{jk}) \mid j \in S]
  \cr
\cr
&\underline{
  \Lsh_k(S, 2):
}\cr
  &\enspace
    (\forall j \in \mathcal{H})\ (\bullet, \bullet, \bullet, x\_{j k}) \gets \texttt{nowait } \text{WaitOpen}\_k(\{j\})
  \cr
  &\enspace
    \texttt{wait}\_{(k, 3)} \forall j \in S.\ x\_{jk} \neq \bot
  \cr
  &\enspace
    \texttt{return } [x\_{jk} \mid j \in S]
  \cr
\cr
&\underline{
  \text{Sync}_k(S):
}\cr
  &\enspace
    \forall j \in S.\ \text{sync}\_{kj} \gets \texttt{true}
  \cr
  &\enspace
    \text{Open?}_k()
  \cr
\cr
&\underline{
  \text{WaitSync}_k(S):
}\cr
  &\enspace
    o\_{kj} \gets \texttt{nowait } \text{WaitOpen}_k(\{j\})\ (j \in S \cap \mathcal{H})
  \cr
  &\enspace
    o\_{kj} \gets \text{sync}\_{kj}\ (j \in S \cap \mathcal{M})
  \cr
  &\enspace
    \texttt{wait}\_{(k, 1)} \forall j \in S.\ o\_{kj}
  \cr
\cr
&\underline{
  \text{Open}_k(S):
}\cr
  &\enspace
    \text{open}\_{kj} \gets \texttt{true}\ (\forall j \in S)
  \cr
  &\enspace
    \text{Open?}_k()
  \cr
\cr
&\underline{
  \text{WaitOpen}_k(S):
}\cr
  &\enspace
    (F_j, \bullet, \bullet, \bullet) \gets \text{WaitOpen}_k(S \cap \mathcal{H})\ (j \in S \cap \mathcal{H})
  \cr
  &\enspace
    \texttt{wait}\_{(k, 1)} \forall j \in S \cap \mathcal{M}.\ \text{open}\_{kj}
  \cr
  &\enspace
    \texttt{return } [F_j \mid j \in S]
  \cr
\cr
&\underline{
  \text{Open?}_k():
}\cr
  &\enspace
    \texttt{for } j \in \mathcal{H}.\ \text{open}\_{kj}, \text{sync}\_{kj}, Z\_{kj}, \pi\_{kj}, x\_{kj} \neq \bot:
  \cr
  &\enspace\enspace
    \text{Open}_i(\{j\}, Z\_{kj}, \pi\_{kj}, x\_{kj})
  \cr
\cr
\ldots
\end{aligned}
}
}\cr
\otimes\cr1(\ldots)
\end{matrix}
\cr
  \circ
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $F^1$
}\cr
\cr
&F_i, \text{com}\_{ij}, \text{open}\_{ij} \gets \bot\cr
&Z\_{ij}, \pi\_{ij}, x\_{ij} \gets \bot\cr
\cr
&\ldots\cr
\cr
&\colorbox{bae6fd}{$
\underline{
  \text{Open}_i(S, Z\_\bullet, \pi\_\bullet, x\_\bullet):
}$}\cr
  &\enspace
    \texttt{assert } F_i \neq \bot
  \cr
  &\enspace
    \text{open}\_{ij} \gets \texttt{true} (\forall j \in S)
  \cr
  &\enspace
    \texttt{for } j \in S.\ Z\_{ij}, \pi\_{ij}, x\_{ij} = \bot:
  \cr
  &\enspace\enspace
    Z\_{ij}, \pi\_{ij}, x\_{ij} \gets Z_j, \pi_j, x\_j
  \cr
\cr
&\underline{
  \text{WaitOpen}_i(S):
}\cr
  &\enspace
    \text{wait}\_{(i, 1)} \forall j \in S.\ \text{open}\_{ji}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{return } (F\_\bullet, Z\_{\bullet i}, \pi\_{\bullet i}, x\_{\bullet i})
  $}
  \cr
\end{aligned}
}
}
\otimes
F[\text{ZK}(\varphi)] \circledcirc F[\text{Stop}]
\end{matrix}
$$

This is just a simulation of a protocol $\mathscr{P}_1$ where we need
to open along with a proof and shares,
simplifying communication substantially.

Let's unroll again.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^5_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
&\enspace
  \ldots
\cr
\end{aligned}
}
}
\otimes
\boxed{\colorbox{FBCFE8}{\large
  $\Gamma^5_M$
} = 1
\begin{pmatrix}
    \text{Prove}_k
  ,\cr
    \text{Verify}
  ,\cr
    \text{SetCommit}_k
  ,\cr
    \text{WaitCommit}_k
  ,\cr
    \text{Open}_k
  ,\cr
    \text{WaitOpen}_k
  ,\cr
    \texttt{stop}
\end{pmatrix}
}
\cr
  \circ
\cr
F^1 \otimes F[\text{ZK}(\varphi)] \circledcirc F[\text{Stop}]
\end{matrix}
$$

Next, except with negligible probability, we can extract
a $z_i$ value because of the ZK proof.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^6_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
&\enspace
  \ldots
\cr
\end{aligned}
}
}
\otimes
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^6_M$
}\cr
&\ldots\cr
&\mu[\bullet] \gets \bot\cr
\cr
&\colorbox{bae6fd}{$
\underline{
  (1)\text{Prove}_k(Z; z):
}$}\cr
  &\enspace
    \pi \gets \text{Prove}_k(Z; z)
  \cr
  &\enspace
    \mu[\pi] \gets z
  \cr
  &\enspace
    \texttt{return } \pi
  \cr
\cr
&\underline{
  \text{Open}_k(S, Z\_\bullet, \pi\_\bullet, x\_\bullet):
}\cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{for } j \in S \cap \mathcal{H}.\ \mu[\pi_j] \cdot G \neq Z_j:
  $}
  \cr
  &\enspace\enspace
  \colorbox{bae6fd}{$
    \texttt{stop }(\{j\}, 1)
  $}
  \cr
  &\enspace
    \text{Open}_k(S, Z\_\bullet, \pi\_\bullet, x\_\bullet)
  \cr
\end{aligned}
}
}
\cr
  \circ
\cr
F^1 \otimes F[\text{ZK}(\varphi)] \circledcirc F[\text{Stop}]
\end{matrix}
$$

Now, we can get rid of the ZK proofs entirely,
by adding verification to the functionality itself.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^7_H$
}\cr
\cr
&\underline{
  (1)\text{Share}_i(z_i):
}\cr
  &\enspace
    \ldots
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \text{Open}_i(\star, z_i, z_i + f_i(\bullet))
  $}
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
  \colorbox{bae6fd}{$
    (F\_\bullet, Z\_{\bullet i}, x\_{\bullet i}) \gets \text{WaitOpen}_i(\star)
  $}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{if } \exists j.\ \text{deg}(F_j) \neq t - 1 \lor F_j(0) \neq 0:
  $}
  \cr
  &\enspace
    \ldots
  \cr
\end{aligned}
}
}
\otimes
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^7_M$
}\cr
&\ldots\cr
&\colorbox{bae6fd}{$
\pi_1, \ldots, \pi_n \xleftarrow{\$} \texttt{01}^{\lambda}
$}\cr
&\colorbox{bae6fd}{$
F_k, m\_{ij}, \mu[\bullet] \gets \bot
$}\cr
\cr
&\colorbox{bae6fd}{$
\underline{
  (1)\text{SetCommit}_k(F):
}$}\cr
  &\enspace
    F_k \gets F
  \cr
  &\enspace
    \text{SetCommit}_k(F)
  \cr
\cr
&\colorbox{bae6fd}{$
\underline{
  (1)\text{Prove}_k(B; b):
}$}\cr
  &\enspace
    \mu[\pi_k] \gets b
  \cr
  &\enspace
    \texttt{return } \pi_k
  \cr
\cr
&\colorbox{bae6fd}{$
\underline{
  \text{Open}_k(S, Z\_\bullet, \pi\_\bullet, x\_\bullet):
}$}\cr
  &\enspace
    \texttt{for } j \in S \cap \mathcal{H}.\ \mu[\pi_j] \cdot G \neq Z\_j:
  \cr
  &\enspace\enspace
    \texttt{stop }(\{j\}, 3)
  \cr
  &\enspace
    \forall j \in S.\ m\_{kj} \gets \pi_j
  \cr
  &\enspace
    \text{Open}_k(S, \mu[\pi\_\bullet], x\_\bullet)
  \cr
\cr
&\colorbox{bae6fd}{$
\underline{
  \text{WaitOpen}_k(S):
}$}\cr
  &\enspace
    (F\_\bullet, Z\_{\bullet k}, x\_{\bullet k}) \gets \text{WaitOpen}_i(\star)
  \cr
  &\enspace
    \forall j \in S \cap \mathcal{H}.\ m_j \gets \pi_j
  \cr
  &\enspace
    \forall j \in S \cap \mathcal{M}.\ m_j \gets m\_{j k}
  \cr
  &\enspace
    \texttt{return } (F\_\bullet, Z\_{\bullet k}, m\_\bullet, x\_{\bullet k})
  \cr
\end{aligned}
}
}
\cr
  \circ
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $F^2$
}\cr
\cr
&F_i, \text{com}\_{ij}, \text{open}\_{ij} \gets \bot\cr
&z\_{ij}, x\_{ij} \gets \bot\cr
\cr
&\ldots\cr
\cr
&\colorbox{bae6fd}{$
\underline{
  \text{Open}_i(S, z\_\bullet, x\_\bullet):
}$}\cr
  &\enspace
    \texttt{assert } F_i \neq \bot
  \cr
  &\enspace
    \text{open}\_{ij} \gets \texttt{true} (\forall j \in S)
  \cr
  &\enspace
    \texttt{for } j \in S.\ z\_{ij}, x\_{ij} = \bot:
  \cr
  &\enspace\enspace
    z\_{ij}, x\_{ij} \gets z_j, x_j
  \cr
\cr
&\underline{
  \text{WaitOpen}_i(S):
}\cr
  &\enspace
    \text{wait}\_{(i, 2)} \forall j \in S.\ \text{open}\_{ji}
  \cr
  &\enspace
  \colorbox{bae6fd}{$
    \texttt{return } (F\_\bullet, z\_{\bullet i } \cdot G, x\_{\bullet i})
  $}
  \cr
\end{aligned}
}
} \circledcirc F[\text{Stop}]
\end{matrix}
$$

At this point, we're simulating a protocol $\mathscr{P}^2$,
which uses this functionality instead of having ZK proofs,
and so we can reset and unroll again.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^8_H$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
&\enspace
  \ldots
\cr
\end{aligned}
}
}
\otimes
\boxed{\colorbox{FBCFE8}{\large
  $\Gamma^8_M$
} = 1
\begin{pmatrix}
    \text{SetCommit}_k
  ,\cr
    \text{Commit}_k
  ,\cr
    \text{WaitCommit}_k
  ,\cr
    \text{Open}_k
  ,\cr
    \text{WaitOpen}_k
  ,\cr
    \texttt{stop}
\end{pmatrix}
}
\cr
  \circ
\cr
F^2 \circledcirc F[\text{Stop}]
\end{matrix}
$$

From this point, we can jump directly to our desired protocol.

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{SetMask}_i():
}\cr
  &\enspace
    \text{SetMask}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitMask}_i():
}\cr
  &\enspace
    \text{WaitMask}_i(\star, \texttt{true})
  \cr
\cr
&\underline{
  (1)\text{Share}_i(z):
}\cr
  &\enspace
    \text{Share}_i(\star, z)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\end{aligned}
}
}
\otimes
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $S$
}\cr
\cr
&\text{left} \gets \mathcal{H}\cr
&\text{bad}_k, \text{sampled}_i \gets \texttt{false}\cr
&F^m, F_i, \alpha\_{ik} \gets \bot\cr
\cr
&\underline{
  (1)\text{SetCommit}_k(F):
}\cr
  &\enspace
    F_k \gets F
  \cr
  &\enspace
    \text{bad}_k \gets \text{deg}(F) \neq t - 1 \lor F(0) \neq 0
  \cr
  &\enspace
    \texttt{if } \forall k \in \mathcal{M}.\ F_k \neq \bot \land F^h = \bot:
  \cr
  &\enspace\enspace
    F^m \gets \sum_k F_k
  \cr
  &\enspace\enspace
    \text{Cheat}(F^m)
  \cr
\cr
&\underline{
  \text{Commit}_k(S):
}\cr
  &\enspace
    \texttt{assert } F_k \neq \bot
  \cr
  &\enspace
    \text{SetMask}_k(S)
  \cr
\cr
&\underline{
  \text{WaitCommit}_k(S):
}\cr
  &\enspace
    \text{WaitMask}_k(S, \texttt{false})
  \cr
\cr
&\underline{
  \text{Open}_k(S, z\_\bullet, x\_\bullet):
}\cr
  &\enspace
    \texttt{if } \text{bad}_k:\ \texttt{stop}(S \cap \mathcal{H}, 1)
  \cr
  &\enspace
    \texttt{for } j \in S \cap \mathcal{H}.\ \forall k.\ x\_{kj} \neq \bot \land \sum_k x\_{kj} \cdot G \neq F^m(j):
  \cr
  &\enspace\enspace
    \texttt{stop}(\{j\}, 1)
  \cr
  &\enspace
    \text{Share}(S, z\_\bullet)
  \cr
  &\enspace
    \text{CheatShare}(S, x\_\bullet)
  \cr
\cr
&\underline{
  \text{WaitOpen}_k(S):
}\cr
  &\enspace
   r_j \gets (F_j, z\_{kj} \cdot G, x\_{kj})\ (j \in S \cap \mathcal{M})
  \cr
  &\enspace
    r_j \gets \text{Sim}_k(j)\ (j \in S \cap \mathcal{H})
  \cr
  &\enspace
    \texttt{return } [r_j \mid j \in S]
  \cr
\cr
&\underline{
  \text{Sim}_k(j):
}\cr
  &\enspace
     \texttt{wait}\_{(k, 1)} \text{Z}_k(j) \neq \bot
  \cr
  &\enspace
    \text{left} \gets \text{left} / \{j\}
  \cr
  &\enspace
    \texttt{if } |\text{left}| = 0:
  \cr
  &\enspace\enspace
    Z \gets \sum\_{i \in \mathcal{H}} \text{Z}_k(i)
  \cr
  &\enspace\enspace
    F \gets \text{F}^h() - \sum\_{i \in \mathcal{H} / \{j\}} F_j
  \cr
  &\enspace\enspace
    x_k \gets \text{WaitShare}_k(\texttt{false}) - \sum\_{i \in \mathcal{H} / \{j \}} \alpha\_{ik}
  \cr
  &\enspace
    \texttt{else}:
  \cr
  &\enspace\enspace
    (Z, F, x\_\bullet) \gets \text{Sample}_k()
  \cr
  &\enspace
    \texttt{return } (Z, F(k), x_k)
  \cr
\cr
&\underline{
  \text{Sample}_k(j)
}\cr
  &\enspace
    \texttt{if } \neg \text{sampled}_j:
  \cr
  &\enspace\enspace
    \text{sampled}_j \gets \texttt{true}
  \cr
  &\enspace\enspace
    Z_j \gets \text{Z}_k(j) 
  \cr
  &\enspace\enspace
    f \xleftarrow{\$} \mathbb{F}_q[X]\_{\leq t - 1}
  \cr
  &\enspace\enspace
    F_j \gets f \cdot G
  \cr
  &\enspace\enspace
    F_j(0) \gets 0
  \cr
  &\enspace\enspace
    \alpha\_{jk} \xleftarrow{\$} \mathbb{F}_q \ (\forall k \in \mathcal{M})
  \cr
  &\enspace\enspace
    F_j(k) \gets \alpha\_{jk} \cdot G - Z_j\ (\forall k \in \mathcal{M})
  \cr
  &\enspace
    \texttt{return } (Z_j, F_j, \alpha\_{j \bullet})
  \cr
\cr
&\ldots
\end{aligned}
}
}
\cr
  \circ
\cr
F[\text{Convert}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

The main trick used in the simulator here is that all of the shares
of the honest parties, save one, can be completely random.
All we need to do is ensure
that the *sum* of the honest parties shares corresponds to the
honest part generated by the ideal functionality.

$\blacksquare$

# Sharing

Next we look at key sharing, which is like conversion,
except that we know our share from the very start of the protocol,
allowing us to commit to it, and thus provide stronger guarantees.

We also look at a "split" version, where each phase of the protocol
has its own function.

**Definition: (Key Sharing)**
$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{SplitShare}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{Set}_i(z):
}\cr
  &\enspace
    f_i \xleftarrow{\$} \{ f_i \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f_i(0) = z \\}
  \cr
  &\enspace
    F_i \gets f_i \cdot G
  \cr
  &\enspace
    \text{SetCommit}_i(F_i)
  \cr
  &\enspace
    \text{Commit}_i()
  \cr
\cr
&\underline{
  \text{WaitSet}_i():
}\cr
  &\enspace
    \text{WaitCommit}_i()
  \cr
\cr
&\underline{
  \text{Share}_i():
}\cr
  &\enspace
    \text{Open}_i()
  \cr
  &\enspace
    \pi_i \gets \text{Prove}_i^\varphi(F_i(0); z_i)
  \cr
  &\enspace
    \Rsh_i(\star, \pi_i, 0)
  \cr
  &\enspace
    \Rsh_i(\star, [f_i(j) \mid j \in [n]], 1)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    F\_\bullet \gets \text{WaitOpen}_i()
  \cr
  &\enspace
    \pi\_{\bullet i} \gets \Lsh_i(\star, 1)
  \cr
  &\enspace
    \texttt{if } \exists j.\ \neg \text{Verify}^\varphi(\pi\_{ji}, F_j(0))
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 0)
  \cr
  &\enspace
    x\_{\bullet i} \gets \Lsh_i(\star, 1)
  \cr
  &\enspace
    x_i \gets \sum_j x\_{ji}, \enspace F \gets \sum_j F_j(0)
  \cr
  &\enspace
    \texttt{if } \exists j.\ \text{deg}(F_j) \neq t - 1 \lor x_i \cdot G \neq F(i):
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 3)
  \cr
  &\enspace
    \texttt{return } (x_i, F(0))
  \cr
\end{aligned}
}
}
\quad
\begin{matrix}
F[\text{SyncComm}]\cr
\circledcirc \cr
F[\text{Stop}]
\end{matrix}\cr
\cr
\text{Leakage} := \{\texttt{stop}\}
\end{matrix}
}
\lhd \mathscr{P}[\text{Commit}]
$$

$\square$

This protocol is basically the same as conversion, just with an earlier
secret value.

Thus, the ideal protocol it implements is going to look quite similar:

**Definition: (Ideal Key Sharing)**
$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{IdealSplitShare}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{Set}_i(z):
}\cr
  &\enspace
    \text{Set}_i(\star, z, \bot)
  \cr
\cr
&\underline{
  \text{WaitSet}_i():
}\cr
  &\enspace
    \text{WaitSet}_i(\star, \texttt{true})
  \cr
\cr
&\underline{
  (1)\text{Share}_i():
}\cr
  &\enspace
    \text{Share}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\end{aligned}
}
}
\quad
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $F[\text{SplitShare}]$
}\cr
\cr
&f^h \xleftarrow{\$} \{f \in \mathbb{F}_q[X]\_{\leq t - 1} \mid f(0) = 0\}\cr
&F^m, \text{ready}\_{ij}, z\_{ij}, x_j \gets \bot\cr
\cr
&\underline{
  \text{Set}_i(S, z, Z):
}\cr
  &\enspace
    \text{ready}\_{ij} \gets \texttt{true}\ (\forall j \in S)
  \cr
  &\enspace
    \texttt{assert } z \neq \bot \lor Z \neq \bot
  \cr
  &\enspace
    \texttt{if } z_i, Z_i = \bot \land z \neq \bot:\ z_i \gets z, Z_i \gets z_i \cdot G
  \cr
  &\enspace
    \texttt{if } Z_i = \bot \land z = \bot = :\ Z_i \gets Z
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  (1)\text{Cheat}(F):
}
}\cr
  &\enspace
    \texttt{assert } \forall ij.\ \text{ready}\_{ij} \land F(0) = 0 \land \text{deg}(F) = t - 1
  \cr
  &\enspace
    F^m \gets F
  \cr
\cr
&\underline{
  \text{WaitSet}_i(S, m):
}\cr
  &\enspace
    \texttt{wait}\_{(i, 0)} \forall j \in S.\ \text{ready}\_{ji} \land (m \to F^m \neq \bot)
  \cr
\cr
&\underline{
  \text{Share}_i(S, z):
}\cr
  &\enspace
    \texttt{assert } Z_i \neq \bot
  \cr
  &\enspace
    \texttt{if } z_i = \bot:
  \cr
  &\enspace\enspace
    \texttt{assert } z \cdot G = Z_i
  \cr
  &\enspace\enspace
    z_i \gets z
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  \text{CheatShare}(S, \hat{x}\_\bullet):
}
}\cr
  &\enspace
    \texttt{assert } F^m \neq \bot \land \forall j \in S.\ \hat{x}_j \cdot G = F^m(j)
  \cr
  &\enspace
    \texttt{for } j. x_j = \bot: x_j \gets \hat{x}_j
  \cr
\cr
&\underline{
  \text{WaitShare}_i(h):
}\cr
  &\enspace
    \texttt{if } h:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} x_i \neq \bot \land \forall j. \land z_j \neq \bot
  \cr
  &\enspace\enspace
    \texttt{return } \sum\_j z_j + f^h(i) + x_i
  \cr
  &\enspace
    \texttt{else}:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} \forall j \in \mathcal{H}. z_j \neq \bot
  \cr
  &\enspace\enspace
    \texttt{return } \sum\_{j \in \mathcal{H}} z_j + f^h(i)
  \cr
&\underline{
  \text{Z}(i):
}\cr
  &\enspace
    \texttt{return } z_i \cdot G
  \cr
&\underline{
\textcolor{ef4444}{
  \text{F}^h():
}
}\cr
  &\enspace
    \texttt{wait } F^m \neq \bot \land \forall i. \exists j. \text{ready}\_{ij}
  \cr
  &\enspace
    \texttt{return } f^h \cdot G
  \cr
\end{aligned}
}
}\cr
\otimes\cr
F[\text{Sync}]\cr
\circledcirc \cr
F[\text{Stop}]
\end{matrix}\cr
\cr
\text{Leakage} := \{\texttt{stop}\}
\end{matrix}
}
$$

**Lemma:**

For some negligible $\epsilon$ and up to $t - 1$ malicious corruptions, we have:

$$
\mathscr{P}[\text{SplitShare}] \overset{\epsilon}{\leadsto} \mathscr{P}[\text{IdealSplitShare}]
$$

**Proof:**

$\mathscr{P}[\text{SplitShare}] \leadsto \mathscr{P}^0 \lhd (\mathscr{P}[\text{Commit}] \otimes \mathscr{P}[\text{Convert}])$, as demonstrated by the following:

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&z_i, Z_i \gets \bot\cr
\cr
&\underline{
  (1)\text{Set}_i(z):
}\cr
  &\enspace
    \text{SetMask}_i()
  \cr
  &\enspace
    z_i \gets z, Z_i \gets z \cdot G
  \cr
  &\enspace
    \text{SetCommit}_i(Z_i)
  \cr
  &\enspace
    \text{Commit}_i()
  \cr
\cr
&\underline{
  \text{WaitSet}_i():
}\cr
  &\enspace
    \text{WaitMask}_i()
  \cr
  &\enspace
    \text{WaitCommit}_i()
  \cr
\cr
&\underline{
  \text{Share}_i():
}\cr
  &\enspace
    \text{Share}_i(z_i)
  \cr
  &\enspace
    \text{Open}_i()
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    Z\_\bullet \gets \text{WaitOpen}_i()
  \cr
  &\enspace
    x_i \gets \text{WaitShare}_i()
  \cr
  &\enspace
    \texttt{if } \exists j.\ \text{Z}_j(i) \neq Z_j:
  \cr
  &\enspace\enspace
    \texttt{stop}(\star, 1)
  \cr
  &\enspace
    \texttt{return } (x_i, \sum_j \text{Z}_j(i))
  \cr
\end{aligned}
}
}
\quad
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $S$
}\cr
\cr
&\underline{
  (1)\text{SetCommit}'_i(F):
}\cr
  &\enspace
    \text{SetCommit}_i(F(0))
  \cr
  &\enspace
    \text{SetCommit}'_i(F - F(0))
  \cr
\cr
&\underline{
  \text{Open}'_i(S):
}\cr
  &\enspace
    \text{Open}_i(S)
  \cr
  &\enspace
    \text{Open}'_i(S)
  \cr
\cr
&\ldots
\end{aligned}
}
}
\cr
\circ\cr
F[\text{Commit}] \otimes F[\text{Commit}] \otimes F[\text{ZK}(\varphi)] \otimes F[\text{SyncComm}] \otimes F[\text{Sync}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

Then:
$$
\mathscr{P}^0 \lhd \ldots \leadsto \mathscr{P}^1 = \mathscr{P}^0 \lhd (\mathscr{P}[\text{IdealCommit}] \otimes \mathscr{P}[\text{IdealConvert}])
$$

Unrolling, we get:

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^0_H$
}\cr
\cr
&\underline{
  (1)\text{Set}_i():
}\cr
&\enspace
  \ldots
\cr
\end{aligned}
}
}
\otimes
\boxed{\colorbox{FBCFE8}{\large
  $\Gamma^0_M$
} = 1
\begin{pmatrix}
    \text{SetCommit}_k
  ,\cr
    \text{Commit}_k
  ,\cr
    \text{WaitCommit}_k
  ,\cr
    \text{Open}_k
  ,\cr
    \text{WaitOpen}_k
  ,\cr
    \text{SetMask}_k
  ,\cr
    \text{WaitMask}_k
  ,\cr
    \text{Share}_k
  ,\cr
    \text{WaitShare}_k
  ,\cr
    \text{Z}_k
  ,\cr
    \text{Cheat}
  ,\cr
    \text{CheatShare}
  ,\cr
    \texttt{stop}
\end{pmatrix}
}
\cr
  \circ
\cr
F[\text{Convert}] \otimes F[\text{Commit}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

This simulates the desired protocol:

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^1_H$
} = \Gamma^0_H\cr
\end{aligned}
}
}
\otimes
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $S$
}\cr
\cr
&\underline{
  (1)\text{Cheat}(F):
}\cr
  &\enspace
    F^m \gets F
  \cr
  &\enspace
    \texttt{return } \text{Cheat}(F)
  \cr
\cr
&\underline{
  (1)\text{SetCommit}_k(Z):
}\cr
  &\enspace
    Z_k \gets Z
  \cr
\cr
&\underline{
  \text{Commit}_k(S):
}\cr
  &\enspace
    \texttt{assert } Z_k \neq \bot
  \cr
  &\enspace
    \text{com}\_{kj} \gets \texttt{true}\ (\forall j \in S)
  \cr
  &\enspace
    \text{Set?}_k()
  \cr
\cr
&\underline{
  \text{SetMask}_k(S):
}\cr
  &\enspace
    \text{ready}\_{kj} \gets \texttt{true}
  \cr
  &\enspace
    \text{Set?}_k()
  \cr
\cr
&\underline{
  \text{Set?}_k():
}\cr
  &\enspace
    \texttt{for } j \in \mathcal{H}.\ \text{com}\_{kj} \land \text{ready}\_{kj}:
  \cr
  &\enspace\enspace
    \text{Set}_k(\{j\}, \bot, Z_k)
  \cr
\cr
&\underline{
  \text{WaitCommit}_k(S):
}\cr
  &\enspace
    \texttt{wait}\_{(i, 0)} \forall j \in S \cap \mathcal{M}.\ \text{com}\_{jk}
  \cr
  &\enspace
    \text{WaitMask}_k(S \cap \mathcal{H}, \texttt{false})
  \cr
\cr
&\underline{
  \text{WaitMask}_k(S, m):
}\cr
  &\enspace
    \texttt{wait}\_{(k, 0)} \forall j \in \mathcal{S} \cap \mathcal{M}.\ \text{ready}\_{jk} \land (m \implies F^m \neq \bot)
  \cr
  &\enspace
    \text{WaitSet}_k(S \cap \mathcal{H}, m)
  \cr
\cr
&\underline{
  \text{Open}_k(S):
}\cr
  &\enspace
    \text{open}\_{kj} \gets \texttt{true}\ (\forall j \in S)
  \cr
  &\enspace
    \text{Share?}_k()
  \cr
\cr
&\underline{
  \text{Share}_k(S, z\_\bullet):
}\cr
  &\enspace
    \texttt{assert } Z_k \neq \bot
  \cr
  &\enspace
    z\_{kj} \gets z\_j \ (\forall j \in S)
  \cr
  &\enspace
    \text{Share?}_k()
  \cr
\cr
&\underline{
  \text{Share?}_k()
}\cr
  &\enspace
    \texttt{for } j \in \mathcal{H}.\ \text{open}\_{kj} \land z\_{kj} \neq \bot:
  \cr
  &\enspace\enspace
    \texttt{if } z\_{kj} \cdot G \neq Z_k:
  \cr
  &\enspace\enspace\enspace
    \texttt{stop}(\{j\}, 1)
  \cr
  &\enspace\enspace
    \texttt{else}:
  \cr
  &\enspace\enspace\enspace
    \text{Share}_k(\{j\}, z\_{kj})
  \cr
\cr
&\underline{
  \text{WaitOpen}_k(S):
}\cr
  &\enspace
    \texttt{wait}\_{(k, 1)} \forall j \in S \cap \mathcal{M}.\ \text{open}\_{kj}
  \cr
  &\enspace
    \texttt{wait}\_{(k, 1)} \forall j \in S \cap \mathcal{H}.\ \text{Z}(j) \neq \bot
  \cr
  &\enspace
    r_j \gets Z\_j\ (\forall j \in S \cap \mathcal{M})
  \cr
  &\enspace
    r_j \gets \text{Z}(j)\ (\forall j \in S \cap \mathcal{H})
  \cr
  &\enspace
    \texttt{return } r\_\bullet
  \cr
\cr
&\ldots
\end{aligned}
}
}
\cr
  \circ
\cr
F[\text{SplitShare}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

This is quite similar to the previous simulator we had,
where we try and aggregate all of the malicious contributions
into a single one.

$\blacksquare$

# Key Generation

Finally, we apply these ideas to key generation.
The basic idea is to do key sharing, but with a random additive share.

**Definition (Key Generation):**

$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{SplitGen}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{Set}_i():
}\cr
  &\enspace
    z \xleftarrow{\$} \mathbb{F}_q
  \cr
  &\enspace
    \text{Set}_i(\star, z, \bot)
  \cr
\cr
&\underline{
  \text{WaitSet}_i():
}\cr
  &\enspace
    \text{WaitSet}_i(\star, \texttt{true})
  \cr
\cr
&\underline{
  (1)\text{Share}_i():
}\cr
  &\enspace
    \text{Share}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\cr
\end{aligned}
}
}
\end{matrix}
}
\lhd \mathscr{P}[\text{SplitShare}]
$$

$\square$

The main interest in doing this is that we get a slightly
more succinct ideal functionality out of it.

The idea here is that we have a random polynomial
$f^h$, which includes the secret value,
and the adversary can also add a tweak polynomial $f^m$,
This tweak also doesn't bias the distribution, because it has to be committed
to in advance, via $f^m \cdot G$.

**Definition (Ideal Key Generation):**

$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{IdealSplitGen}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{Set}_i(z):
}\cr
  &\enspace
    \text{Set}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitSet}_i():
}\cr
  &\enspace
    \text{WaitSet}_i(\star, \texttt{true})
  \cr
\cr
&\underline{
  (1)\text{Share}_i():
}\cr
  &\enspace
    \text{Share}_i(\star)
  \cr
\cr
&\underline{
  \text{WaitShare}_i():
}\cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\end{aligned}
}
}
\quad
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $F[\text{SplitGen}]$
}\cr
\cr
&f^h \xleftarrow{\$} \mathbb{F}_q[X]\_{\leq t - 1}\cr
&F^m, \text{ready}\_{ij}, x_j \gets \bot\cr
\cr
&\underline{
  \text{Set}_i(S):
}\cr
  &\enspace
    \text{ready}\_{ij} \gets \texttt{true}\ (\forall j \in S)
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  (1)\text{Cheat}(F):
}
}\cr
  &\enspace
    \texttt{assert } \text{deg}(F) = t - 1
  \cr
  &\enspace
    F^m \gets F
  \cr
\cr
&\underline{
  \text{WaitSet}_i(S, m):
}\cr
  &\enspace
    \texttt{wait}\_{(i, 0)} \forall j \in S.\ \text{ready}\_{ji} \land (m \to F^m \neq \bot)
  \cr
\cr
&\underline{
  \text{Share}_i(S):
}\cr
  &\enspace
    \text{shared}\_{ij} \gets \texttt{true}\ (\forall j \in S)
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  \text{CheatShare}(S, z, \hat{x}\_\bullet):
}
}\cr
  &\enspace
    \texttt{assert } F^m \neq \bot
  \cr
  &\enspace
    \texttt{assert } z \cdot G = F^m(0)
  \cr
  &\enspace
    \texttt{assert } \forall j \in S.\ \hat{x}_j \cdot G = F^m(j)
  \cr
  &\enspace
    \texttt{for } j \in S.\ x_j = \bot: x_j \gets \hat{x}_j
  \cr
\cr
&\underline{
  \text{WaitShare}_i(h):
}\cr
  &\enspace
    \texttt{if } h:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} x_i \neq \bot \land \forall j. \text{shared}\_{ji}
  \cr
  &\enspace\enspace
    \texttt{return } f^h(i) + x_i
  \cr
  &\enspace
    \texttt{else}:
  \cr
  &\enspace\enspace
    \texttt{wait}\_{(i, 1)} \forall j \in \mathcal{H}. \text{shared}\_{ji}
  \cr
  &\enspace\enspace
    \texttt{return } f^h(i)
  \cr
\cr
&\underline{
\textcolor{ef4444}{
  \text{F}^h():
}
}\cr
  &\enspace
    \texttt{wait } F^m \neq \bot \land \forall i.\ \exists j.\ \text{ready}\_{ij}
  \cr
  &\enspace
    \texttt{return } f^h \cdot G
  \cr
\end{aligned}
}
}\cr
\circledcirc \cr
F[\text{Stop}]
\end{matrix}\cr
\cr
\text{Leakage} := \{\texttt{stop}\}
\end{matrix}
}
$$

**Lemma:**

For some negligible $\epsilon$, and up to $t - 1$ corrupt parties, we have:
$$
\mathscr{P}[\text{SplitGen}] \lhd \mathcal{P}[\text{SplitShare}] \overset{\epsilon}{\leadsto} \mathscr{P}[\text{IdealSplitGen}]
$$

**Proof**

First, we can jump to a protocol where $\mathcal{P}[\text{SplitShare}]$ has been replaced with $\mathcal{P}[\text{IdealSplitShare}]$, and then appeal to a direct simulation:

$$
\begin{matrix}
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $\Gamma^0_H$
}
\ldots
\end{aligned}
}
}
\otimes
\boxed{
\small{
\begin{aligned}
&\colorbox{bae6fd}{\large
  $S$
}\cr
\cr
&\hat{Z}_i \xleftarrow{\$} \mathbb{G}\cr
&F^m, Z_k, z_k, x_i \gets \bot\cr
\cr
&\underline{
  \text{Set}_k(S, z, Z):
}\cr
  &\enspace
    \text{Set}_k(S)
  \cr
  &\enspace
    \texttt{assert } z\neq \bot \lor Z \neq \bot
  \cr
  &\enspace
    \texttt{if } z_k, Z_k = \bot \land z \neq \bot:
  \cr
  &\enspace\enspace
    z_k \gets z
  \cr
  &\enspace\enspace
    Z_k \gets z \cdot G
  \cr
  &\enspace
    \texttt{elif } Z_k \neq \bot \land Z \neq \bot :\ Z_k \gets Z
  \cr
  &\enspace
    \text{Cheat?}()
  \cr
\cr
&\underline{
  (1)\text{Cheat}(F):
}\cr
  &\enspace
    \texttt{assert } F(0) = 0 \land \text{deg}(F) = t - 1
  \cr
  &\enspace
    F^m \gets F
  \cr
  &\enspace
    \text{Cheat?}()
  \cr
\cr
&\underline{
  \text{Cheat?}()
}\cr
  &\enspace
    \texttt{if } \forall k.\ Z_k, F^m \neq \bot:
  \cr
  &\enspace\enspace
    \text{Cheat}(F^m + \sum\_{k \in \mathcal{M}} Z_k)
  \cr
\cr
&\underline{
  \text{WaitSet}_k(S, m):
}\cr
  &\enspace
    \text{WaitSet}_k(S, m)
  \cr
\cr
&\underline{
  \text{Share}_k(S, z):
}\cr
  &\enspace
    \texttt{assert } Z_k \neq \bot
  \cr
  &\enspace
    \texttt{if } z_k = \bot:
  \cr
  &\enspace\enspace
    \texttt{assert } z \cdot G = Z_k
  \cr
  &\enspace\enspace
    z_k \gets z
  \cr
  &\enspace
    \text{CheatShare?}()
  \cr
\cr
&\underline{
  \text{CheatShare}_k(S, \hat{x}\_\bullet):
}\cr
  &\enspace
    \texttt{assert }  F^m \neq \bot \land \forall j \in S.\ \hat{x}_j \cdot G = F^m(j)
  \cr
  &\enspace
    \texttt{for } j.\ x_j = \bot:\ x_j \gets \hat{x}_j
  \cr
  &\enspace
    \text{CheatShare?}()
  \cr
\cr
&\underline{
  \text{CheatShare?}():
}\cr
  &\enspace
    \texttt{if } \forall k \in \mathcal{M}.\ z_k \neq \bot:
  \cr
  &\enspace\enspace
    \texttt{for } j.\ x_j \neq \bot:
  \cr
  &\enspace\enspace\enspace
    z \gets \sum_k z_k
  \cr
  &\enspace\enspace\enspace
    \text{CheatShare}(\{j\}, z, x\_\bullet + z)
  \cr
\cr
&\underline{
  \text{WaitShare}_k(h):
}\cr
  &\enspace
    \text{WaitShare}_k(h)
  \cr
\cr
&\underline{
  \text{Z}(i):
}\cr
  &\enspace
    \texttt{nowait } \text{F}^h(0) - \sum\_{i \in \mathcal{H}} \hat{Z}_i \texttt{ if } i = 1 \texttt{ else } \hat{Z}_i
  \cr
\cr
&\underline{
  \text{F}^h():
}\cr
  &\enspace
    \texttt{return } \text{F}^h() - \text{F}^h(0)
  \cr
\end{aligned}
}
}
\cr
  \circ
\cr
F[\text{SplitGen}] \circledcirc F[\text{Stop}]
\end{matrix}
$$

The core thing the simulator needs to accomplish is to 
fold the $Z$ value into the $F^m$ value,
which now needs to hold both the contribution to the secret value,
and to the secret sharing.

We also need to simulate an honest polynomial without the secret $0$
value.

$\blacksquare$

As a final note, the actual key sharing protocol one might
use in practice directly doesn't expose each individual functionality,
instead calling them in sequence:

$$
\boxed{
\begin{matrix}
\colorbox{FBCFE8}{\large
  $\mathscr{P}[\text{KeyShare}]$
}\cr
\cr
\boxed{
\small{
\begin{aligned}
&\colorbox{FBCFE8}{\large
  $P_i$
}\cr
\cr
&\underline{
  (1)\text{Share}_i(z):
}\cr
  &\enspace
    \text{Set}_i(\star, z, \bot)
  \cr
  &\enspace
    \text{WaitSet}_i(\star, \texttt{true})
  \cr
  &\enspace
    \text{Share}_i(\star)
  \cr
  &\enspace
    \texttt{return } \text{WaitShare}_i(\texttt{true})
  \cr
\end{aligned}
}
}
\end{matrix}
}
\lhd \mathscr{P}[\text{SplitShare}]
$$

This protocol should match the one implemented in the specification,
although with less modularity, naturally.