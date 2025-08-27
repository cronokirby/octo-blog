---
title: "Fractals on The Web"
date: "2021-02-21 16:07:08+01:00"
aliases:
  - "../posts/2021/02/fractals-on-the-web"
tags:
  - "graphics"
  - "fractals"
  - "math"
draft: "False"
katex: "True"
---

Last week, I made a little [web application](https://fractals.cronokirby.com/)
for visualizing some fractals, and I thought I'd write up a few thoughts
about how it works.

<!--more-->

I won't be going into [the code](https://github.com/cronokirby/fractals) very
much in depth, just highlighting a few interesting things I encountered.

# WebGL

I could've done all of the rendering logic in pure Javascript, using
the canvas API. This would be quite naive, since each pixel composing
a fractal image can be rendered in parallel. The GPU is the natural
piece of hardware for tackling this problem, and WebGL is the easiest
way of accessing that power.

Setting this all up requires a lot of boilerplate. We're not using
all of the capabilities of a typical WebGL program, since we don't have
any geometry to render at all. Instead we're just rendering two triangles
to fill up our canvas:

![](../Images/4fa2963fbb84586eab4ced86a6d54bd038296d3f4f5016c96e93ac27ce3482fb.png)

Our fragment shader, which has the job of coloring each pixel of these triangles,
will contain all of the logic to render our fractals instead.

There's also a bit of math, to assign to each pixel a point in the complex plane,
according to how we've dragged the current fractal, zoomed in, and the size
of the canvas.

This is all quite boring, not very fractally, and better explained by other sites,
such as [WebGL Fundamentals](https://webglfundamentals.org/).

# Fractal Formulas

The fractals that we're working with arise from the same procedure.
You have some kind of complex sequence, defined by iterating a (complex) function:

$$
z_0, \ z_1 = f(z_0), \ z_2 = f(z_1), \ \ldots
$$

The initial value $z_0$, and slight variations of $f$ depend on the point
$p$, where each pixel in our canvas ends up.

This sequence bounces around the complex plane:

![](../Images/3259eb9c36c77f8efe2a1a6a33103013cfd983850fe9431bd5b4b1c04f540fc6.png)

If this sequence converges, then our point $p$ is part of the fractal set.
Otherwise, the sequence diverges, and the point $p$ does not belong to the set.
Usually, we have a heuristic, where if the sequence grows large enough, we assume
that it will never converge, and report the point as being outside the set.
We usually limit the number of iterations we run this process for. After a certain
number of iterations, we assume convergence. This introduces false positives.
Using more iterations gives us a more precise image, but takes longer to run.

We can also look at how many iterations it takes for the sequence to diverge,
to provide more coloring information, but we'll see that later.

## Mandelbrot

For the Mandelbrot set, we have:

$$
\begin{aligned}
z_0 &:= 0 \cr
f(z) &:= z^2 + p
\end{aligned}
$$

Coloring each point in the resulting fractal in black, we
get this image:

![](../Images/3c00bb378838e5aaa4032db2812698410bbc26b2151ca44d426862dae80ea955.png)

## Julia

Julia sets are kind of dual to the mandelbrot set. We have
a parameter $c$ characterizing the set, defining the following parameters:

$$
\begin{aligned}
z_0 &:= p \cr
f(z) &:= z^2 + c
\end{aligned}
$$

This is similar to the previous formula, except now the adjustment
inside of $f$ is static, but the initialization varies across the canvas.

Here are a few examples of Julia fractals, with different values for $c$:

![](../Images/4779ec789794a1efba4758f7066f161b157420a1aad821afdfe669943e0e2096.png)
![](../Images/986757229895d261f7861acc94663f4b866934a758a9d529ed7c026d710bd432.png)
![](../Images/a8ecd3b74732fe10868520809c0dc66b8e48ff40be53ae8cd3489695f589f3a0.png)

## Variations

Both of these formulas depend on iterations of the form $f(z) = z^2 + c$.
We can imagine swapping $z^2$ for something else:

$$
\begin{aligned}
&z^2 + c \cr
&z^3 + c \cr
&z^4 + c \cr
&z \sin(z) + c
\end{aligned}
$$

Here's what the Mandelbrot set looks like under these variations:

![](../Images/3c00bb378838e5aaa4032db2812698410bbc26b2151ca44d426862dae80ea955.png)
![](../Images/a9c8fbfe4e727b3a5105ccf5909f1c06f6bab5ce2e6dc1fde6b20356a0beebea.png)
![](../Images/41cb75c0f9f5ae0dbd99c165eceec6a3f6dbe6fa9219ab6f65eb3c4c004b52ab.png)
![](../Images/e366bb3f67fe4cfc5eaa1736baa64dfaa7f0cf1e278978078378316465eb4e01.png)

And a Julia set:

![](../Images/8bca53b36121550ee2493ca9617fab8349a88e30cb44cd9193d964c50b4af6ec.png)
![](../Images/f2514f1e612a1319616cd07ec12faa3ed95d3a5439fcaf2a2e979adfc19af583.png)
![](../Images/7a450826edcd0970276c9dc493b21885eba72da15a5842396f1ffdd7906bb73d.png)
![](../Images/9e7a19f19cf2f3ea348d0aa56b8176df6c69629fbc4294a2fe9c93474ad3c5ff.png)

# Coloring

So far, the way we've colored our fractals is pretty simple. We iterate
our function a certain number of times. If we end early, because our
value grows too large, we assign one color (white, in our examples so far),
and if we reach the end of our iterations, and still haven't diverged,
we assign another color (black).

## Simple Coloring

Instead of just looking at the binary value "converges" or "doesn't converge",
we can look at how many iterations it takes for us to bail out,
say $i$, and then divide that by the total number of iterations:

$$
\frac{i}{N}
$$

This gives us a value between $0$ and $1$, which is a bit more interesting.

![](../Images/efefd68ce4f1ee0de88fc9497be845906c80ab7dae4f4a753a4c736256a7cc96.jpg)

(Note: this comes from [Something Somewhere](https://smthngsmwhr.wordpress.com/2016/10/16/mandelbrot-set-visualization/),
since my site currently uses the smooth coloring tweak I explain later, and I wanted to demonstrate banding here)

## Smooth Coloring

You can notice a nice transition now, but there's still a kind of "banding" effect. The transitions
between different colors don't happen smoothly. There's a formula to fix this, which I admittedly
don't understand that well, so I'll refer you to
[Inigo Quilez](https://www.iquilezles.org/www/articles/mset_smooth/mset_smooth.htm) for more details.

Basically, instead of:

$$
\frac{i}{N}
$$

you do:

$$
\frac{i - \log \frac{\log \frac{\log |z|^2}{\log B}}{\log k}}{N}
$$

Where $k$ is the power you're iterating with. So $2$ for the standard mandelbrot
sequence, $3$ if you're doing $z^3 + c$ each iteration, etc. $z$ is the last value
you reached, and $B$ is the threshold after which you bail out.

This gives us a smoother coloring, as we can see here in a zoomed in
Mandelbrot plot.

![](../Images/4b39cfd079cc75a6e3fcc59462d342816114204678dc810b38fb130e2d82378a.png)

## Palettes

Given a value between $0$ and $1$, we can color the fractal in a few interesting ways.
One is to simply linearly interpolate between two colors. One version I settled with
is due to Inigo Quilez, once again. Here the formula is:

$$
a + b \cdot cos(2 \pi (t \cdot c + d))
$$

Where $a, b, c, d$ are vectors, with operations done pointwise. The final result
is a vector, representing colors.

Varying $c$ lets us get more and more variation between colors:

![](../Images/e1fb2eb0e4800e89ffe26a9c8af9d5368ae303c060b2b4f0c798190a11c69d43.png)
![](../Images/90661f377180db44bc53277a77d6ba64ddab2fdc3e5600c27b5090660b6a9f69.png)
![](../Images/ad8f591cb4aaa3d5d7f0c69c34b9787243d29f03909a3a00ff7908a0acdf0ab9.png)

We can also play around with the other values, and get different color gradients:

![](../Images/7ac98a1ac30fddec0ee89b8f6703f2c71ab6b91f62316451ed59def2d5d17f6e.png)
![](../Images/cbc103c3b8f581161da570974f9872c1ded052e066f83a1ee5c54ad46479b4c1.png)
![](../Images/c730fe7f09c8da5ad5a8585155e6b4e74d2b6c5ea547395f3007453c9af26d36.png)
![](../Images/391c87132e90aff2186682e773fad1d7a72e9c83d3fc837fb7c383cdccd156bb.png)

# Orbit Traps

Instead of using the iteration count, we can instead keep track
of the minimum distance to some geometric figure.

## Circles

For example, we can use the distance to a disk of radius 1, centered at some point in the plane:

![](../Images/d42fc423da7879f783d98e2972243aa2f6c302fe5af1df806ce47773f6653fb8.png)

Clamping the distance in the range $[0, 1]$, this gives us a nice image:

![](../Images/a2ce78314fefd7f300926586e0c11619d18bd8b835504b0fddad4b66d6fcb469.png)

We can vary the center of the circle, giving us different images:

![](../Images/5646ce73075ac66d94ccd02db2caf2bd1897e2a9c21bf6e0c59f6ea0e11501af.png)
![](../Images/27c8d6e24dd5118093989888b49d81eb3f94492ec667a6fbf4ab0b2e3fd5372f.png)
![](../Images/7a34f01f33f7bfe0b75798ad99f5bc2dca9a936511a1afeb73f4e41e9696e15a.png)

We can also take the distance to a circle of a certain radius, instead of the full disk:

![](../Images/34a6b830111c6d51c3b25165ec85d0334fd99f38e74d8c0468834145634d0085.png)
![](../Images/ec69c74d3411f32f35518735176eedcee034cff556bb16c8520ca3552de1e465.png)

## Lines

We can do the same with a vertical line:

![](../Images/feee9aadffa045d24bf13c47cce68a25f202e078abc97a74b36f71773a376115.png)
![](../Images/b2edd7e53287a0d06dc8dd25535d7f3ef91c8203a9db33cb42c3ed182ae6595b.png)
![](../Images/45b34d23616ad7df624be9ae5c5b7ec3dc167cf30baf4e52d8eb2751b4f40b9c.png)

## Squares

Or even a square:

![](../Images/ccba54e0fd6d9dee6d2c4819ae6005f7070d50a386d6a6fb4a44457edd5acf03.png)
![](../Images/0a4888940fe24754f66e37bcb6c9fb4e49c9bacffe8496740a0abc1791d1b28e.png)
![](../Images/d0eca3f7359a6182c55642de9d8af5cfb504b037286ac6257aa675ce6472c02a.png)

# Conclusion

Hopefully this was interesting, and I'd welcome you to take a look
at [the code](https://github.com/cronokirby/fractals).
Inigo Quilez, like with many topics in graphics, has a great number
of articles on [fractals](https://www.iquilezles.org/www/index.htm).

# Addendum: Pretty Pictures

Now, here's just some nice pictures:

![](../Images/0d13fd8a6138bebc35f9b4d1e203f29d8ea898423390cf61df8ccb1b62905e46.png)
![](../Images/df6f29d147be8f007c5583fd644ccd9dc637ce252c2a20844ba5455f80088d18.png)
![](../Images/0bac091f8e777895d95609fde2ff62e6113c05acfda4ca59d3b1ae3ee9c05873.png)
![](../Images/c14b773318d1e900cce6e4b33f004fc0a3f273dfd57a63ee9bdf29396a971f1f.png)
![](../Images/81d5e3961052a57cfe808b1ff12aac162489aa9ab2bbf4f7241cd6c57b907671.png)
![](../Images/8a7c00396919ca2df81629924c150b584817a038de272b9b693d308149c54828.png)
![](../Images/b6fd74255fa73a4e50b8292419fee9ddc0bdbc55fbc6a3a5b134ea3c902233c4.png)
![](../Images/f48ba5c99123717eebb0d96ae0962516dc04c3defa606e10b326d6ca6525abc7.png)
![](../Images/ae9c6cbe78cf0f1ebce017d16e1c0e54d9152b746130ed0d0a05d5086eb3fbcf.png)
![](../Images/fa1ec9135bc95ee8764ea17f5062c4362a563d23a689e8826b69074182246556.png)
![](../Images/96e369abb375df1252c67f3f7c921f306e626d72254208979f90d4568acbfbcf.png)
![](../Images/380a92bd559cba48237c2237cfeb2f129e66b4aa5f032ea81bd7b116cd0805f4.png)
![](../Images/a99d2ba33286454525dc54bbce9bceafd8dbd5d8f36755aec21340727f73ca22.png)
![](../Images/a62e78692b2a53fb819b72f27d76347969783801fa5529079a90b4cbf4ec684f.png)
![](../Images/0f5c7708b159b5a0d1db3d202f55d78ae56a3e82b4a1f0796f2713be7ed39eca.png)
![](../Images/4bb22036c175eb671cc1a17da7ea00ffb74244845128d86d1c45434fcb88c80b.png)
![](../Images/938d19da4939ad1bda9360d2b9559770a3017c371a5ae463cf15dae8437b88c0.png)
![](../Images/fef3ab3128770a7b767eecf2639f77beaacd4eb8fb2c183033b515217acdb448.png)
![](../Images/38ab22349f12293376cb75ff672df0777b1e64608fe16740e21c766cc077602b.png)
![](../Images/7c0962b443b7442b940ab6cdade139026e08b10ba6c8db1f6a7b913d7f76d480.png)
![](../Images/322b019c696dbc6d57d713367b1589c80cbda23475c5c87eb752c8aad152bf61.png)
![](../Images/f42036d1e3fe978b5eb21f12ead3a3e338200afaeaba461bfd83cfa0f53db81b.png)
![](../Images/b2422f5cd4c30077994ce0cc3a0c5d2bf47ab131b75b86037777efe809126e53.png)
![](../Images/1578f5cd1d9330f98b2974faee8c2e0c41d5688a2a3a1b18abb64be6250cce54.png)
![](../Images/5d553b9250faefe1225b2812d1c69304de64a26a3a05db8020b6c6445d01341d.png)