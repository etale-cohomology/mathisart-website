<!-- py miatex2html.py algebra01.md  # Output html file (same name)! -->

<!-- ------------------------------------------------------------------------------------------ -->
<!-- 
\title_page Lagrange's theorem
\title_article Lagrange's theorem and the RSA theorem
\category0 Algebra
\category1 Groups
\category2 Finite groups
\category3 Lagrange's theorem
-->

<!-- ------------------------------------------------------------------------------------------ -->
\section{Four theorems}

**Lagrange's theorem.** The order of every **subgroup** of a finite **group** $G$ divides the order of the group $G$.

Lagrange's theorem doesn't seem too impressive.
It doesn't say anything about {\it how many} subgroups of each size there are (only that there {\it could} be).
But I just learned of a beautiful application:
using Lagrange's theorem, it's easy to prove {\bf Fermat's little theorem} {\it and} {\bf Euler's theorem}.
As a kicker, these two are relevant to understanding {\bf RSA encryption}.

\vskip8pt
{\bf Fermat's little theorem.} In every {\bf field} $\Z / p\Z$, if $a$ is nonzero then $a^{p-1} =_p 1$.

\vskip8pt
{\bf Euler's theorem}. In every {\bf ring} $\Z / n\Z$, if $a$ is nonzero then $a^{\phi[n]} =_n 1$.

\vskip8pt
Using these two results, we can prove what I like to call "the RSA theorem".

\vskip8pt
{\bf The RSA theorem}. Let $d, e \in \Z$, let $\phi: \Z \to \Z^+$ be {\bf Euler's totient function}. If $d \cdot e =_{\phi[n]} 1$, then $m^{d \cdot e} =_n m$.

\vskip8pt
Here, we've written $x =_n y$ what is usually written $x \equiv y \pmod n$.
The latter is read "$x$ is {\bf congruent} to $y$ {\bf modulo} $n$", and
it means that $x$ and $y$ are {\it equal} in the {\bf quotient ring} $\Z / n\Z$
(they {\it represent} the same {\bf equivalence class} if you prefer the language of {\bf equivalence relations}, or
they {\it belong} to the same {\bf coset} of $n\Z$ if you prefer the language of cosets);
it also means that $x$ and $y$ leave the same {\bf remainder} when {\bf divided} by $n$
if the computations are carried out in the parent ring $\Z$.
The notation $x =_n y$ means the {\it same thing}, but you may read it as "$x$ is $n$-equal to $y$" or
"$x$ is equal to $y$ over $\Z / n\Z$".

\vskip8pt
The notation $\Z / n\Z$ is read
"the {\bf quotient ring} of the ring $\Z$ by the ideal $n\Z$", or
"the {\bf quotient ring} of the ring $\Z$ modulo the ideal $n\Z$".
Here, $n$ is taken to be a {\it fixed}, but arbitrary integer.
The set $\Z$ is simply the set

$$\Z := \{\ldots, -3, -2, -1, 0, 1, 2, 3, \ldots\}$$

of all {\bf integers}.

\vskip8pt
For a fixed integer $n$, the set $n\Z$ is the set

$$n\Z := \{\ldots, -3 \cdot n, -2 \cdot n, -1 \cdot n, 0 \cdot n, 1 \cdot n, 2 \cdot n, 3 \cdot n, \ldots\}$$

of all {\bf integer multiples} of $n$.

\vskip8pt
For a fixed integer $n$, the quotient ring $\Z / n\Z$ arises by
{\bf gluing} the ring $\Z$ "through" the ideal $n\Z$.
The operationg of {\bf gluing} is realized through the idea of {\bf equivalence relations} and {\bf equivalence classes}, and
it amounts to {\it relaxing} the notion of {\bf equality} by considering to be
{\bf equal} in the quotient ring $\Z / n\Z$
elements that were {\it not} equal in the parent ring $\Z$.

\vskip8pt
The fact that you can fix two arbitrary elements $x$ and $y$ of the ring $\Z$ and
consider them over multiple quotient rings of $\Z$ is, in my opinion, quite deep.
For example, take $5$ and $13$. They represent {\it different elements} over $\Z$, but
they represent {\it the same element} over the quotient ring $\Z / 4\Z$.
In the language of arithmetic in $\Z$, $5$ and $13$ are equal over $\Z / 4\Z$ because
their difference is {\bf divisible} by $4$ (their difference is $-8$), and
also because over $\Z$ they leave the same {\bf remainder} when {\bf divided} by $4$ (the remainder is $1$).
In the language of rings, $5$ and $13$ are equal over $\Z / 4\Z$ because
they belong to the same {\bf coset} of the {\bf ideal} $4\Z$;
namely, they belong to the coset $4\Z + 1$.

\vskip8pt
For each positive integer $n$ you can consider the {\bf reduction} of $\Z$ modulo $n$,
which amounts to taking the quotient ring of $\Z$ by the ideal $n\Z$.
The ring $\Z$ is related to its quotient rings $\Z / n\Z$ by something called {\bf canonical epimorphisms}.
These canonical epimorphisms allow us to take an element of $\Z$, say $5$, and
consider $5$ over multiple quotient rings of $\Z$.
In order to go from $5$ as an element of $\Z$ to $5$ as an element of, say, $\Z / 4\Z$,
we apply the canonical epimorphism

$$\phi_4 : \Z \to \Z / 4\Z$$

to $5$, which maps $5 \in \Z$ to $5 \in \Z / 4\Z$.

\vskip8pt
Reduction modulo $n$ is particularly important when $n$ is a {\bf prime}, in which case we call it $p$.
Reduction modulo a {\bf prime ideal} yields a {\bf field}, and every field arises as the {\bf quotient} of some ring by some prime ideal.
The {\bf localization} of a {\bf commutative ring} at a {\bf prime ideal} $P$ yields something called a {\bf local ring} $R^*$
(which is a ring with a unique {\bf maximal ideal}), and
the {\bf maximal ideal} of the local ring $R^*$ is the ideal {\bf generated} by $P$ inside of $R^*$.

\vskip8pt
At every ring $R$, the {\bf prime ideals} of $R$ form a weird space called the {\bf prime spectrum} of $R$, denoted ${\rm Spec}[R]$.
In the ring $\Z$, each prime ideal is generated by a single prime $p$ (but, in general, prime ideals need more than one generator),
and so the prime spectrum of $\Z$ arises from the prime numbers.
I call ${\rm Spec}[R]$ "weird" because its topology deviates substantially from the topology of more familiar spaces
like $3$-dimensional Euclidean space ${\mathbb R}^3$: ${\rm Spec}[R]$ is almost never {\bf Hausdorff}!
Non-Hausdorf spaces are rarely studied in analysis, even in topology itself, but they seem quite common in algebraic geometry.
Moreover, the {\bf topology} that comes with ${\rm Spec}[R]$, called the {\bf Zariski topology},
is riddled with technical deficiencies
(I often read that it "doesn't have enough {\bf open sets}", but I don't know what this means).
What you can do to get around the weakness of the Zariski topology is replace it with a much more powerful notion of topology:
a {\bf Grothendieck topology} called the {\bf étale topology}.
Under the étale topology, the set of all prime ideals of $R$ becomes the {\bf étale spectrum} of $R$.

\vskip8pt
Understanding a bit about rings, ideals, and quotient rings is important because it's a segway into deeper mathematics,
and also because it provides a more abstract, general, and ultimately simpler language to talk about results in number theory,
like Fermat's little theorem and Euler's theorem.

\vskip8pt
Euler's theorem is a generalization of Fermat's little theorem:
every field $\Z / p\Z$ is also a ring $\Z / n\Z$,
because $n$ stands for an arbitrary integer, and every prime $p$ is an integer.
Both results are important in {\bf cryptography}, specifically for RSA encryption.

<!-- ------------------------------------------------------------------------------------------ -->
\section{What is a coset?}

In group theory, {\bf cosets} are some of the most important objects.
A {\bf coset} is a special {\bf subset} of a group that {\it arises} from a {\bf subgroup}.
To every subgroup $H$ of a group we can associate {\bf the set of all cosets} of $H$.
You can think of the cosets of the subgroup $H$ as "logically attached" to $H$.
That is: every time you think of a particular group $G$, you can immediately think of the subgroups of $G$;
and every time you think of a particular subgroup $H$, you can immediately think of the cosets of $H$.

\vskip8pt
If you see the word {\bf coset} in the wild, you need 3 pieces of data to specify the coset:
$1)$ a {\bf group} $G$, a {\bf subgroup} $H$, and an {\bf element} $g$ of $G$.
Then, the coset that these data specify is written as $gH$.
Every element $g$ of $G$ yields one coset $gH$, but not all of these cosets will be different!
If each element $g$ of $G$ were to generate a different coset $gH$,
then every subgroup $H$ would have as many cosets as $G$ has elements (one for each element of $g$), but this is not the case.

\vskip8pt
{\bf Example.} For $G$ take the additive group of integers $\Z$. [...]

\vskip8pt
In symbols, we can denote {\bf the set of all cosets} of a subgroup $H$ as ${\rm Cosets}[H]$,
and we can write the set of all cosets of $H$ as

\vskip8pt
$${\rm Cosets}[H] := \{ gH\ |\ g \in G\}$$

\vskip8pt
which reads "${\rm Cosets}[H]$ is {\bf defined} as the set of all sets of the form $gH$, as $g$ ranges over $G$".
We can also build the set of all cosets of all subgroups of $G$, but let's not get too carried away.

\vskip8pt
Sometimes ${\rm Cosets}[H]$ will form a {\bf group} under the operation it inherits from the parent group $G$,
in which case the group ${\rm Cosets}[H]$ is written $G / H$, which reads "$G$ modulo $H$".
The group $G / H$ is then called "the quotient group of $G$ by $H$", or the "quotient group of $G$ modulo $H$".
Whether ${\rm Cosets}[H]$ is a group or not hinges on a particular property that $H$ must satisfy.

<!-- ------------------------------------------------------------------------------------------ -->
\section{Three lemmas}

So, how do we prove Lagrange's theorem? We'll be using a few technical lemmas.

\vskip8pt
{\bf First Fundamental Lemma of Cosets.} Let $G$ be a group, let $H \subset G$ be a subgroup.
The cosets of $H$ form a {\bf partition} of $G$.

\vskip8pt
{\bf Second Fundamental Lemma of Cosets.} Let $G$ be a group, let $H \subset G$ be a subgroup, let $g \in G$.
If $g \notin H$, then $H$ is {\bf disjoint} from the coset $gH$.


\vskip8pt

\vskip8pt
What is... a {\bf group}?

\vskip8pt
What is... a {\bf field}?

\vskip8pt
What is... a {\bf ring}?

\vskip8pt
What is... a {\bf proof}?
