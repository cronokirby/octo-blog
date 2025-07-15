---
title: "Universal Properties and Adjunctions"
date: "2020-12-27 11:23:40+01:00"
aliases:
  - "../notes/2020/12/universal-properties-and-adjunctions"
note-tags:
  - "algebra"
  - "category-theory"
  - "math"
katex: "True"
type: "note"
---

"Free" constructions are abundant in Algebra, and are actually examples
of *Adjunctions*. Specifically, we have an adjunction:

$$
\bold{Set} \xtofrom[?]{F} \bold{Alg}
$$

Where $F : \bold{Set} \to \bold{Alg}$ is the *free functor* from
the category of sets to this category of algebraic structures,
and $? : \bold{Alg} \to \bold{Set}$ is the *forgetful functor*,
which forgets the additional algebraic structure.

Usually, this universal construction is presented a bit differently,
but is equivalent to the notion of adjunction.

## Free Groups

As a concrete example, take Free Groups. Given a set $A$,
the free group $F A$ is usually defined with a universal property:

There is a group $F A$, and a set function $\eta : A \to F A$ such that for
any other group $G$ and function $g : A \to G$, there exists a unique
group homomorphism $\varphi! : F A \to G$ making the following diagram commute:

![](../Images/4fcd298056ceb2839d06a6a384bac9170108a4986e9bf5dc050b99da8d17ed87.png)

Of course, when talking about the interaction of morphisms and objects
from $\bold{Grp}$, we really mean their *images*,
under the forgetful functor $? : \bold{Grp} \to \bold{Set}$. Being explicit,
we get the following diagram:

![](../Images/0241ddf62e8f04052ed6b191a24f779a5f92db8cc1278443c18ee624f1522055.png)

We can characterize this object $F A$ as being an initial 
object in the slice category $A \downarrow ?$ (where $A : 1 \to \bold{Set}$
is the functor sending every object to $A$, and every morphism to $1_A$).

The objects consists of a choice of group $G$ and set function $A \to ?G$,
and the morphisms are group homomorphisms $G \to H$ making the following
diagram commute.

![](../Images/25744988912cc4cec774355c2da44eb50d043ca5ca6396cfeaff89764aaa3627.png)

It's clear that the initial object in this category is the free group
$F A$, along with the morphism $\eta : A \to ? F A$.

## Adjunctions

It turns out that this characterization is implied by the adjunction:

$$
F \dashv \ ?
$$

The "primal" characterization of an adjunction $L \dashv R$ is that
there exists a
special binatural isomorphism between the two functors:

$$
\mathcal{D}(L -, -) \cong \mathcal{C}(-, R -)
$$

A more convenient (and entirely equivalent) characterization
is that of two natural transformations:

$$
\begin{aligned}
\eta : 1 \Rarr R L \cr
\epsilon : L R \Rarr 1
\end{aligned}
$$

Satisfying these two relations:

![](../Images/b01e0edaec000f669d6013b733ea96613738d2bf1841578150ea0a8b6e211d44.png)

which we call the left and right "zig-zag identities".

> [!note] **Note:**
> I use the notation $\alpha_F$ to denote the natural transformation
> whose component for the object $A$ is $\alpha_{F A}$.
> 
> Similarly, $G \beta$ denotes the natural transformation whose component
> at $B$ is $G \beta_B$.

### Implying the Universal Property

With this adjunction in place, we can show
that $(L A, \eta_A)$
is the initial object in the comma category $A \downarrow R$,
for any object $A$.

This is a fun series of diagram chases.

First, we show that there is a morphism
to the other objects in the comma category.
Given $(M, f : A \to R M)$ some other object in $A \downarrow R$,
we provide a morphism $\varphi : L A \to  M$
such that this diagram commutes:

![](../Images/b7511b87ae65de2d73d9b143ff4334f0a8a17fe94a679ee79322fe420270dbd5.png)

Applying the right zig-zag identity at $M$, we get this commuting diagram:

![](../Images/e74e3c5415abd76a9a852adbfcd2263afc0c7af37fc003c0c28bab9e630631d9.png)

We can compose this with $f$ to get:

![](../Images/8ed593852b5f35abbbf85ff3ec90dfd9dc9e3e5807cf5f2acf44cf51bf3c832d.png)

But then, by naturality of $\eta$, we have:

![](../Images/ea1936588090db5e46857fd31c654992f14e417be6d7a11717da1ec52887d68c.png)

And then $L f \ggg \epsilon_M$ is our $\varphi$.
Since $R$ is a functor $RL f \ggg R \epsilon_M = R (L f \ggg \epsilon_M)$

> [!note] **Note:**
> In the specific case of a free group, $L f = F f$
> works by preserving all of the free algebraic operations
> we've created, but swapping out the "seeds" we've used.
> Then we interpret these free operations as concrete
> operations in $M$, using $\epsilon$.

Next, we show that this function is unique. In other words,
if $\phi : L A \to M$ with $\eta_A \ggg R \phi = f$, then $\phi = \varphi$.

We start with:

![](../Images/9f659bfbf2769b02f5e54b58ded78bf5b3c0c18e3bcef8000a263c574e10d14c.png)

Then, we apply the left zig-zag identity, to get:

![](../Images/0c17d54b01a4a9fdc3d8ab8c083174803b6549110134e1d7f93dfc94dc6bc02a.png)

By naturality of $\epsilon$, we get:

![](../Images/14e55c51bcab979aa2715bac0dac7e8c97e786ab41dc42eb6ed58ed17dbc6af3.png)

But, since $\eta_A \ggg R \phi = f$, we have:

![](../Images/dcbc9a2ca35fde4b13aefa65ec2f5530a79b3c9198ce81a614c8a6af57778682.png)

But, by definition $\varphi = L f \ggg \epsilon_M$, giving us:

![](../Images/dcd94ca87f4f827c8e7603daa6e6e87c1aefcb7bfba28fcc2247c141b9b4abc8.png)

In other words $\varphi = \phi$.
  
## The Dual Construction

If we take the opposite functors $L^{op} : \mathcal{C}^{op} \to \mathcal{D}^{op}$
and $R^{op} : \mathcal{D}^{op} \to \mathcal{C}^{op}$, we have:

$$
R^{op} \dashv L^{op}
$$

Using our previous result, we get that for any object $M$ in $\mathcal{D}^{op}$,
$(R^{op} M, \epsilon_M : M \leftarrow LR\ M)$
is initial in the slice category $M \downarrow L^{op}$

![](../Images/2d5934221be0049d152b269f3ca94db93d4565cc8dedd124ca285e788cbefdf9.png)

Of course, this is the same thing as saying that $(R M, \epsilon_M)$ is *terminal*
in the slice category $L \downarrow M$. In other words, for any
object $A$ in $\mathcal{C}$, with a morphism $\alpha : L A \to M$ in $\mathcal{D}$,
there exists a unique $f : A \to R M$ such that this diagram commutes:

![](../Images/70a6f2592834362e267eb23357e58cc8a8faca8b0b91681005dacfd28fdc1bca.png)

### Concretely

Back to the example of free groups, we have the following situation:

![](../Images/456de15f0d89b0ae079b2b8f3bcfc5deca8614334fbf347d96f6d752157fe14e.png)

Ultimately, this just expresses the fact that a group homomorphism
out of a free group consists first of replacing each of the seeds
with an element of $G$, and then reducing the free algebraic structure
using $\epsilon$.

# The Other Direction

We can also go in the other direction. 
Let $L : \mathcal{C} \to \mathcal{D}$, $R : \mathcal{D} \to \mathcal{C}$
be functors. If we have
parameterized functions (which we don't yet assume to be natural)
$\eta_A : A \to RL \ A$ for any object $A$ in $\mathcal{C}$,
and $\epsilon_M : LR \ M \to M$ for any object $M$ in $\mathcal{M}$,
such that $(L A, \eta_A)$ is initial in $A \downarrow R$,
and $(R M, \epsilon_M)$ is terminal in $L \downarrow M$, then
we have an adjunction:

$$
L \dashv R
$$

First, $\eta$ is natural:

![](../Images/c3f2a57bce86ebc67be15b987643f86a4ca278c88e52e6921876b5daded180cc.png)

The right and left triangles both commute, since they
make use of the unique $\varphi!$ that must exist
whenever we have a function $A \to R M$, for some $M$.

Secondly, $\epsilon$ is natural:

![](../Images/f3f0abbb5fc73c4b8408bf0f6be73c6047f364723289a30f9b582cdcc559f76a.png)

The left and right triangles both commute, making use
of the universal property of $LR \ A$. (The argument is similar
to before, of course).

Now, for the zig-zag identities.

Let's start with the right zig-zag identity, for some object $M$:

![](../Images/cd3a4d7d7ca542f1dffe143883ce5d77d0df9c1f58d05eaa03cb3f655424b01d.png)

If we take $1 : R \ M \to R \ M$, we have a unique $\varphi!$ such that:

![](../Images/e79b69b12491daa92f7ea8b65d73f82a16809de47339b0211e649d0f31025976.png)

by the universal property for $RL$.

For any $\varphi : LR \ M \to M$, we have a unique $f!$ such that:

![](../Images/d6bd8c648ed419b645cdb779fb56c0d8d47c576041105fde46c843eb75e35698.png)

by the universal property for $LR$.

Combining the first diagram, with the image under $R$ of the second,
we get:

![](../Images/970b11c6ad5953216d87427d829ec69abf7bbe58a5f7c1f9f08bad817d076a40.png)

But, $Lf! \ggg \epsilon_M$ satisfies the universal property
of $\varphi!$, which is unique. This means that $\varphi = Lf! \ggg \epsilon_M$.

We then have:

![](../Images/02ef174f781eb0a044621a4d36104ed448eb382accbc75d51fa098318074e29b.png)

But clearly, $1$ satisfies the universal property of $f!$ in this situation,
which means $f! = 1$. This gives us:

![](../Images/de41e068853e82f52b9cd4ca789b9c5356db309f188480aa57d71cdfab1075a0.png)

And so the right zig-zag property is satisfied.

For the left zig-zag property, we use the same strategy.

Given any object $A$, in $\mathcal{C}$ we want to show:

![](../Images/7f33106f455b968a3d4ca5197867141de2a6656cbd479d96b6b1a94f707610ae.png)

We have the following diagram:

![](../Images/9544d1a7720b9554714f5f9dffe7a79f830e1a475393e13af737bee9784aad24.png)

With the unique $f!$ satisfying this diagram existing
because of the universal property of $LR$.

Similarly, for *any* $f$, we have:

![](../Images/b5d3b6b1fca4016bfe7423fdfd4798a6ca4e7c2aa472dc2d3155570f93e90293.png)

because of the universal property of $RL$.

Combining both diagrams, we get:

![](../Images/bac4e4c79b85f0e9767f0802f254fde0de36ed1f5ed4897041c28ddea7bc5239.png)

A similar argument as last time shows us first that $f! = \eta \ggg R\varphi!$,
and then $\varphi! = 1$, giving us:

![](../Images/7f33106f455b968a3d4ca5197867141de2a6656cbd479d96b6b1a94f707610ae.png)

and so the left zig-zag property is satisfied.

# Conclusion

Given functors $L : \mathcal{C} \to \mathcal{D}$ and $R : \mathcal{D} \to \mathcal{C}$,
these statements are equivalent:

1. $L \dashv R$
2. $\mathcal{D}(L -, -) \cong \mathcal{C}(-, R -)$
3. There exist $\eta : 1 \Rarr RL, \ \epsilon : LR \Rarr 1$ satisfying the zig-zag identities
4. ($\forall A \in \mathcal{C}, M \in \mathcal{D}$) $(RL A, \eta_A)$ is initial in $A \downarrow R$,
   and $(LR M, \epsilon_M)$ is terminal in $L \downarrow M$.

In this post, I only proved $3 \iff 4$. $1 \iff 2$ by definition, and $2 \iff 3$ is well
known.