---
title: "Explaining Yao's Garbled Circuits"
date: "2022-05-01 18:18:47+02:00"
aliases:
  - "../posts/2022/05/explaining-yaos-garbled-circuits"
tags:
  - "cryptography"
  - "mpc"
draft: "False"
katex: "True"
---

The protocol so fun you have to implement it! Like
[I did recently](https://github.com/cronokirby/yao-gc).

<!--more-->

Yao's Garbled Circuits is a Cryptographic scheme that allows
two parties with secret inputs to evaluate an arbitrary function
on those inputs, without revealing them to each other.
As far as I can tell, the protocol was first described
orally by Andrew Yao in 1986, but the first written description
was in the subsequent [How to Play Any Mental Game](https://dl.acm.org/doi/pdf/10.1145/28395.28420) paper, by Goldreich, Micali, and Wigderson.
But, I'm not an academic historian, so take this with a grain of salt,
and feel free to correct me on Twitter if you know better.

I first heard about this scheme last summer, and like so
many things in Cryptography, it seemed
quite mysterious to me at the time.
And just like so many of those things, it turned out to be
a lot simpler than I expected; hopefully this post can impart
a bit of that feeling to you as well.

# MPC in a Nutshell

Garbled Circuits are a special case of a more general idea called
(secure) Multi-Party Computation (MPC).

The premise is that you have a group of parties $P_1, \ldots, P_n$.
Each party $P_i$ has their own secret input $x_i$. The
parties want to compute some function $f(x_1, \ldots, x_n)$ on their inputs,
learning the result $y$.

![](../Images/529b70eaee758068fbd00ac8d25f0014da55658bd9525570e28257f7e7ebce5a.png)

The simplest way to do this would be for the parties to share their
inputs with each other. Each party would know all of the inputs $x_1, \ldots,
x_n$, and thus be able to compute $y = f(x_1, \ldots, x_n)$ on their own.

The problem with this naive approach is that each party would like
to keep their input $x_i$ _secret_. The difficulty in MPC is not
in computing the function $f$ among multiple parties, but rather in
keeping all of the inputs hidden while performing that computation.

## Example: The Millionaire Problem

One of the classic examples of a situation where MPC is useful
is [Yao's Millionaire Problem](https://doi.ieeecomputersociety.org/10.1109/SFCS.1982.88).

The premise is that several millionaires want to know which of
them is the richest. They could do this by revealing their exact
wealth to each other, but they'd like to each keep that amount
secret.
In other words, they'd like to learn who has the most money,
without revealing the amount of money that person, or any
other member of the group has.

This is a problem which can be solved through an MPC protocol.
The inputs $x_1, \ldots, x_n$ will be set to the wealth of each
party, and the function $f$ to compute will be:

$$
f(x_1, \ldots, x_n) := \argmax_{i} x_i
$$

which returns the index $j$ of the largest amount $x_j$.

An MPC protocol for $f$ would let the millionaires collaborate
by exchanging messages, eventually learning the result
$f(x_1, \ldots, x_n)$, but no other information about the inputs.

This is a somewhat artificial example, but there are plenty
of more realistic applications of MPC. Another example
people like to give is that of the [Danish Sugar Beet Auction](https://www.wikiwand.com/en/Danish_Sugar_Beet_Auction), where MPC was used to
organize an auction for sugar beet production contracts without
revealing individual bids.

Another interesting application of MPC is allowing companies to
collaborate to train Machine Learning models on private data, without sharing
that data with each other. For example, several hospitals could
collaborate to train a model for identifying cancer, without having
sensitive health information leave the individual hospitals.

> [!note] **Note:**
> The result of such a process would be a Machine Learning model,
> and it can be surprisingly easy to use such a model to extract
> information about the data it was trained on. See
> ["Extracting Training Data from Large Language Models"](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf)
> as a recent example.
> 
> MPC allows you to only learn the result of your function $f$,
> but that result can sometimes imply a lot of information about
> the inputs involved. Beware.

## Our Specific Setting

So far we've seen MPC in the case with an
arbitrary number of parties, computing some arbitrary function $f$.
Garbled Circuits is a technique for doing MPC when
there are only two parties. We also assume that the participants
are _semi-honest_. They might be curious about what the input
of the other party is, but they won't cheat by misbehaving,
and deviating from what the protocol asks them to do.

### Boolean Circuits

This technique nonetheless works with an arbitrary function $f$,
although we need to assume a more concrete representation for
that function. We assume that $f$ can be represented as a
_boolean circuit_. You can think of this circuit as a bunch of
wires connected to boolean gates like $\&, \oplus$, etc. A
more formal definition would model this circuit as a _graph_.
The nodes would be the inputs or gates of the circuit, and the edges
would be the wires connecting gates together.

![](../Images/634cb3e7ee10256b05ee8870cfd6248a5a6f5f9bc364af99a5a06973f67d8ffd.png)

I think the most useful representation for this post is related
to the idea of graphs, but not exactly the same. I like
to think of a circuit as a collection of labeled wires. Each
wire either comes from an input value, or from the output
of another gate, like in this example:

![](../Images/c5c15c03d706577848126140396370e487ff3a90974e8e66c9e399874a568074.png)

You can also model this idea as a little programming language,
involving variables, reading input, and boolean operators:

```txt
let a = input(0)
let b = input(1)
let c = a & b
let d = c | b
return (c, d)
```

But models are less important than what you do with them, so let's
mosey on and have a look at that.

# Walking on Wires

The Garbled Circuits protocol is _asymmetric_: each of the two
parties does something different. One of the parties is
what I'll call the _garbler_: their job is to obfuscate
the circuit and the input values, and hand that mess over
to the other party. I'll call this other party the _evaluator_:
their job is to take this garbled circuit, and evaluate it,
producing the final result. They then share this result
with the garbler, and everybody is happy.

## A single gate

To illustrate the essentials, let's consider the case
where the parties have secret bits $x_0$ and $x_1$, respectively,
and want to compute a boolean function $f(x_0, x_1)$ on these inputs.

We can think of this function as a lookup table:

$$
F := \begin{vmatrix}
f(0, 0) & f(0, 1) \cr
f(1, 0) & f(1, 1) \cr
\end{vmatrix}
$$

Now, if you had the inputs $x_0$ and $x_1$, then you could evaluate
$f(x_0, x_1)$ by simply looking up the entry $F[x_0, x_1]$.
Of course, each party only has one of the inputs, so this doesn't work.

Now, this next idea is a bit of a reach, so bear with me.
The garbler will generate 4 encryption keys $k^a_0, k^a_1, k^b_0, k^b_1$,
one for each wire, and each of the two possible values that wire can have.
Then, they create an encrypted version of the table $F$:

$$
F' := \begin{vmatrix}
\text{Enc}((k^a_0, k^b_0), f(0, 0)) & \text{Enc}((k^a_0, k^b_1), f(0, 1)) \cr
\text{Enc}((k^a_1, k^b_0), f(1, 0)) & \text{Enc}((k^a_1, k^b_1), f(1, 1)) \cr
\end{vmatrix}
$$

> [!note] **Note:**
> I assume the existence of a randomized encryption scheme which
> encrypts and decrypts messages using two keys. A simple way
> to do this is encrypting once with each key. Another cooler,
> and more efficient way is to xor the keys together. Proving
> that this is secure is left as an exercise to the reader.

Now, if you were to magically have the keys $k^a_{x_0}$ and $k^b_{x_1}$,
then those keys wouldn't tell you any information
about $x_0$ and $x_1$, since they look as random as any other pair
of keys, but they would let you evaluate $f(x_0, x_1)$, using $F'$.

You would use your pair of keys to try and decrypt each entry.
Eventually, you would hit the entry encrypted with $k^a_{x_0}$
and $k^b_{x_1}$, and would thus read out $f(x_0, x_1)$.

Now, one problem is that since the layout of $F'$ is the same
as that of $F$, we know which input we've decrypted simply
by observing where our decryption is successful. To get around
this, we can simply shuffle the table around. The easiest way
to do this is to randomly swap both rows, and randomly
swap both columns.

In order to avoid having to try and decrypt all 4 entries, we can
also attach a pointer bit to our keys, which indicates where we should look.
For example, we might receive $(k^a, 1)$, and $(k^b, 0)$, which
tells us to look at the entry $F[1, 0]$ to use these keys.
But, we don't know that $(k^a, 1)$ actually corresponds to
$(k^a_1, 1)$, because it's possible that we decided to flip
the two rows in the table, and we actually have $(k^a_0, 1)$.

![](../Images/8401d872070181f0d5fcedef665f5165322bb96bd938f8c816068a06965b96ba.png)

Thus, if we can somehow deliver the
garbled table $F'$ along with $k^a_{x_0}$ and $k^b_{x_1}$
to the evaluator, then they'll be able to tell us the result,
all without them learning the garbler's input $x_0$.

Now, preparing and sending the table $F'$ isn't very difficult.

The same goes for the garbler's input key $k^a_{x_0}$.
All they have to do is just send it along. $k^a_0$ isn't any
more recognizable than $k^a_1$, and our shuffling and pointer
bit flipping help make that the case.

Now, for $k^b_{x_1}$, we're in a bit of a pickle. The garbler knows
$k^b_0$ and $k^b_1$, and the evaluator knows $x_1$. We'd like
for the evaluator to somehow learn $k^b_{x_1}$, without learning
the other key, and without the garbler learning $x_1$.
It seems we're at a bit of an impasse, at least without a
neat little tool.

## Detour: Oblivious Transfer

The tool we need is something called [Oblivious Transfer](https://www.wikiwand.com/en/Oblivious_transfer). The idea is that a
sender has two messages $m_0$ and $m_1$, the receiver has a bit $b$,
and the two run an Oblivious Transfer protocol so that:

- The receiver learns $m_b$, but not the other message
- The sender learns nothing

Like many protocols in Cryptography, you can think of this
ideal protocol as a magical box with a trusted third party,
such as a friendly gnome, inside:

![](../Images/34450b231c7859d515ba116c564d12c0cabf9ad2e7aedcc03e99efa6a106d7b4.png)

For our purposes, all you really need to know is that you can instantiate
this protocol without any magic. The details don't really matter
for Garbled Circuits. If you're curious, I'd recommend
taking a gander at [The Simplest Protocol for Oblivious Transfer](https://eprint.iacr.org/2015/267.pdf), which is one way, among many, of
instantiating this construction.

## Wrapping up the simple case

Now, notice that we can directly use the Oblivious Transfer protocol
for our previous dilemma. The garbler has $k^b_{0}$ and $k^b_1$
as their two messages, and the evaluator has $x_1$, and would
like to end up with just $k^b_{x_1}$. This is the exact
setup Oblivious Transfer was designed to solve.

Let's recap our scheme so far. To evaluate $f(x_0, x_1)$, with the garbler
having $x_0$, and the evaluator having $x_1$, first the garbler generates
random keys $k^a_0, k^a_1, k^b_0, k^b_1$ (including their
corresponding pointer bits), along with the encrypted table:

$$
F' := \begin{vmatrix}
\text{Enc}((k^a_0, k^b_0), f(0, 0)) & \text{Enc}((k^a_0, k^b_1), f(0, 1)) \cr
\text{Enc}((k^a_1, k^b_0), f(1, 0)) & \text{Enc}((k^a_1, k^b_1), f(1, 1)) \cr
\end{vmatrix}
$$

They then randomly flip the rows and columns of this table, and also
the corresponding pointer bits of the keys.

Then, for $k^a$, they simply send $k^a_{x_0}$ to the evaluator.
For $k^b$, they run an Oblivious Transfer using $k^b_{0}$
and $k^b_1$, with the evaluator receiving $k^b_{x_1}$.

Using $k^a_{x_0}$ and $k^b_{x_1}$, the evaluator can decrypt
the entry for $f(x_0, x_1)$, and then send the result back
to the garbler.

# Everything's Connected

Now, this protocol only works with a function $\{0, 1\}^2 \to \{0, 1\}$; in other words, a single gate. Our circuit is likely
to have more than one gate. To support this, we need a way
to chain multiple gate evaluations together.

Notice that the output of our function didn't really matter
in the single gate case. Sure, we said it was just a boolean in $\{0, 1\}$, but it could have easily been an integer, or a string.
As long as we can encrypt it, it doesn't really matter.

So, we could have the output of the function be another key,
which would then be used as the input to a different gate.

To illustrate, let's say we have two input wires $a$ and $b$,
connected to some gate $f$, producing an output wire $c$:

![](../Images/692977572e6c08a69ddb784cf855267a800f0c964cc0859ca08e8939932d94b6.png)

Like with each of the input wires, the output wire $c$ has
two keys $k^c_0$ and $k^c_1$ associated with it. Instead of
thinking of our gate $f$ as producing a boolean output, we
can instead have it produce one of these keys as its output,
giving us the following lookup table:

$$
F := \begin{vmatrix}
k^c_{f(0, 0)} & k^c_{f(0, 1)} \cr
k^c_{f(1, 0)} & k^c_{f(1, 1)} \cr
\end{vmatrix}
$$

And then we just shove this lookup table into the previous
setup we had, and everything should just work.
Given the correct inputs $k^a_{x_0}$ and $k^b_{x_1}$,
the evaluator learns $k^c_{f(x_0, x_1)}$, which they can
then use as an input to the next gate they need to evaluate.

## Bird's Eye View

We've seen all of the individual pieces, so let's take a little
step back and look at how everything fits together.
Once again, I think looking at our circuit as a collection of wires
makes the most sense.

For every wire $w$, there will be two keys, $k^w_0$ and $k^w_1$,
for each of the two possible values that wire can take. These
keys also contain a random pointer bit (with $k^w_1$ having the
opposite of $k^w_0$) which tells us which part of the encrypted lookup
table to use when using that key.

A wire obtains its value in one of only two ways:

1. It's connected to one of the inputs
2. It's connected to the output of a gate

For the first case, we have two ways of getting the key to the evaluator.
If the input $x$ for that wire $w$ belongs to the garbler,
then they can just send $k^w_x$ to the evaluator.
If the input belongs to the evaluator, then an Oblivious Transfer
needs to be conducted, using $k^w_0$, $k^w_1$
as messages, along with the evaluator's
bit $x$.

In the second case, where the wire is the output of some gate, the evaluator will have received the keys
for the two inputs to that gate, and can use the encrypted table
to look the resulting output key up.

Finally, after going through the circuit, the evaluator will
end up with a set of output keys, corresponding to the output
wires of the circuit.

To turn these keys into a concrete result, we can also use
an encrypted table, albeit with just two entries:

$$
O := \begin{vmatrix}
\text{Enc}(k^w_0, 0)\cr
\text{Enc}(k^w_1, 1)
\end{vmatrix}
$$

(shuffled appropriately, based on the pointer bit, of course).

To summarize, the garbler generates all of the encryption keys
for each wire, and then sends the correct input keys to the evaluator,
either by choosing them directly, if the garbler has the input
bit for that key, or by running an Oblivious Transfer
with the evaluator, if they're the one with the input bit. The
garbler then sends along the encrypted tables for each gate,
along with the encrypted output tables. The evaluator can
then traverse the circuit, using their encryption keys
to get the key contained in each gate table, and then eventually
the outputs contained in the output tables. They then send
the output back to the garbler, and everyone is happy.

# Conclusion

I found this scheme so compelling when I first read about
it a month or so ago that I had
to [implement it](https://github.com/cronokirby/yao-gc);
it was only natural that I'd end up writing about it too.

There are probably 100 explanations of Yao's Garbled Circuits
out there, given that it's one of the earliest MPC schemes,
and spawned an entire paradigm of protocols.
Another explanation I like is in the [Pragmatic MPC book](https://securecomputation.org/), which has a lot of great material
beyond just this scheme.

In a further post, I might explain the nitty gritty details
of how my implementation works, although it's nothing fancy.