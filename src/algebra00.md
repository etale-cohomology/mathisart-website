<!-- py miatex2html.py algebra00.md  # Output html file (same name)! -->

<!-- ------------------------------------------------------------------------------------------ -->
<!-- 
\title_page Equivalence relations
\title_article Equivalence relations, a tool for gluing stuff (with itself)
\category0 Algebra
\category1 Relations
\category2 Equivalence relations
\category3 
-->

<!-- ------------------------------------------------------------------------------------------ -->
Despite being a difficult
[philosophical][https://plato.stanford.edu/entries/identity-indiscernible/] and
[mathematical][http://www.math.harvard.edu/~mazur/preprints/when_is_one.pdf] topic,
**equality** is one of the most important ideas in mathematics.
**Equivalence relations** *generalize* the idea of equality.
Equivalence relations allow us to consider to be "equal" (or *equivalent*) things that weren't equal before;
they allow us to say two things are "equal" under a *particular lens* (or a particular point of view).
Equivalence relations can be used to build *quotient objects*. Two elements are **equal** in the quotient object *iff* they're **equivalent** under the equivalence relation.
Quotient objects (like
[quotient sets][https://ncatlab.org/nlab/show/quotient+set],
[quotient groups][https://en.wikipedia.org/wiki/Quotient_group],
[quotient rings][https://en.wikipedia.org/wiki/Quotient_ring],
[quotient topological spaces][https://en.wikipedia.org/wiki/Quotient_space_(topology)],
[quotient vector spaces][https://en.wikipedia.org/wiki/Quotient_space_(linear_algebra)], etc.) are ubiquitous in math.

The first example of an equivalence relation is *equality* itself, denoted by the symbol $=$.

An **equivalence relation** on a set $X$ is a
[binary relation][https://en.wikipedia.org/wiki/Binary_relation] on the set $X$ that satisfies three properties. \lf
A **binary relation** relation on a set $X$ is just a subset of the Cartesian product $X \times X$ of $X$ with itself. Any subset of $X \times X$ will do!

\definition A
[**binary relation**][https://en.wikipedia.org/wiki/Binary_relation] on a
[set][https://en.wikipedia.org/wiki/Set_(mathematics)] $X$ is a **subset** of the 2-fold Cartesian product $X \times X$ of $X$ with itself.

\proposition Let $X$ be a set. The *smallest* binary relation on $X$ is the empty set $\{\}$. \lf
\remark The empty set $\{\}$ is also denoted $\emptyset$.

$\tab$ *Proof*. In
[ZF set theory][https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory],
*the (unique) smallest subset* of an arbitrary set $S$ is the empty set $\{\}$ because: \lf
  $\tab\tab1)$ $\{\}$ is a subset of *every* set (reason: if $S$ is an arbitrary set, then every element of $\{\}$ is also an element of $S$), \lf
  $\tab\tab2)$ the size of $\{\}$ is exactly *zero* and there's *no* set of size smaller than zero (reason: I don't know), and \lf
  $\tab\tab3)$ $\{\}$ is the *unique* set of size zero
(reason: two sets are equal *iff* they have exactly the same elements, and any two empty sets have the same elements, so they're equal).

Since $X$ is a set, then $X \times X$ is also a set (because Cartesian products exist).
Since $X \times X$ is a set, then the unique smallest subset of $X \times X$ is the empty set $\{\}$.
But a subset of $X \times X$ is precisely a (binary) relation on $X$, so $\{\}$ is the unique smallest (binary) relation on $X$. \lf
$\tab$ $\square$

\proposition Let $X$ be a set. The *largest* binary relation on $X$ is the whole Cartesian product $X \times X$.

$\tab$ *Proof*. In
[ZF set theory][https://en.wikipedia.org/wiki/Zermelo%E2%80%93Fraenkel_set_theory],
*the (unique) largest subset* of an arbitrary set $S$ is $S$ itself because: \lf
  $\tab\tab1)$ $S$ is a subset of itself
  (reason: if $S$ is an arbitrary set, then every element of $S$ is also an element of $S$), \lf
  $\tab\tab2)$ there's *no* subset of $S$ that is larger than $S$
  (reason: if there were a subset of $S$ larger than $S$, then that set would have at least one element that $S$ doesn't have,
  in which case it'd no longer be a subset of $S$), and \lf
  $\tab\tab3)$ $S$ is the unique subset of $S$ with this property
  (reason: any other subset of $S$ either has the same element as $S$, in which case it's $S$ itself, or
  it has less elements, in which case it's no longer the largest subset of $S$).

Since $X$ is a set, then $X \times X$ is also a set (because Cartesian products exist).
Since $X \times X$ is a set, then the unique largest subset of $X \times X$ is $X \times X$ itself.
But a subset of $X \times X$ is precisely a (binary) relation on $X$, so $\{\}$ is the unique largest (binary) relation on $X$. \lf
$\tab$ $\square$

<!-- ------------------------------------------------------------------------------------------ -->
\section{Every equivalence relation yields a partition, and every partition yields an equivalence relation}

[Partitions][https://en.wikipedia.org/wiki/Partition_of_a_set]
formalize the idea of "splitting" something into pieces that share nothing in common.
We can think of a partition as taking a pizza and cutting it in slices, and then stuffing the slices into a bag.
A bit more precisely, if the pizza itself is a *set*, then a slice of pizza is a *subset* of that set, and the bag is a *set*, and
we can think of a partition of the pizza as cutting the pizza in slices and stuffing all the slices into a bag;
now the *bag* is the *partition*. Every different way of slicing the pizza results in a different partition of the pizza.
Notice that the slices are *not* the partition, but the partition is the *bag* containing the slices.
The slices (by themselves) are just subsets of the pizza floating around in space,
and it's not until we collect the slices and stuff them into a bag that the slices form a *partition*, and the *bag* becomes that partition.

A **partition** of a set $X$ is a certain subset of the power set $\Po X$ of $X$.
This means a partition of $X$ is a certain $2$-set over $X$, or a certain set of subsets of $X$, or
a certain element of the power set of the power set of $X$.

$\tab$ *Example*. If $X$ is the set
$$\{a, b, c\},$$
then the set
$$\{\{a, b\}, \{c\}\}$$
is a partition $P$ of $X$. Notice that the partition $P$ is a **subset** of the power set $\Po X$ of $X$, because the power set $\Po X$ is the set
$$\{\{\}, \{a\}, \{b\}, \{c\}, \{a, b\}, \{a, c\}, \{b, c\}, \{a, b, c\}\},$$
and every element of $P$ is an element of $\Po X$.
The partition $P$ is also an **element** of $\Po\Po X$, which I won't write down because it has $256$ elements.
However, not every element of $\Po\Po X$ is a partition of $X$.

\definition Let $X$ be a set. The following are equivalent. \lf
  $\tab\tab1)$ $P$ is a **partition** of $X$ \lf
  $\tab\tab2)$ $P$ is a set of (nonempty) subsets of $X$, and any two elements $A,B \in P$ of $P$ either share everything in common or nothing in common \lf
  $\tab\tab3)$ $P$ is a set of (nonempty) subsets of $X$, and the union of $P$ is $X$ (meaning $\cup P = X$, and the intersection of any two elements of $P$ is \lf
  $\tab\tab4)$ $P$ is a **cover** of $X$ and the elements of $P$ are pairwise disjoint \lf

$\tab$ **Theorem (the fundamental theorem of equivalence relations)**. Let $X$ be a set. \lf
Every equivalence relation on $X$ yields a partition of $X$, and every partition of $X$ yields an equivalence relation $X$.

$\tab$ *Proof*.

<!-- ------------------------------------------------------------------------------------------ -->
\section{Congruence modulo $n$ is an equivalence relation}

**Congruence modulo $n$** is a very important equivalence relation on the set $\Z$ of
[integers][https://en.wikipedia.org/wiki/Integer]; it yields the finite cyclic groups $(\Z / n\Z, +)$ and the finite rings $(\Z / n\Z, +, \cdot)$.

\vskip8pt
$\tab$ **Theorem**. Fix $n \in \Z^+$. Congruence modulo $n$ is an **equivalence relation**.

$\tab$ *Proof*. To show congruence modulo $n$ is an equivalence relation, we must show it *satisfies the properties* of an equivalence relation.
So, we must show congruence modulo $n$ is 1) **reflexive**, 2) **symmetric**, and 3) **transitive**.
More precisely, we must show that:
congruence modulo $1$ is an equivalence relation, and
congruence modulo $2$ is an equivalence relation, and
congruence modulo $3$ is an equivalence relation, and so on, for every possible positive integer $n \in \Z^+$.

So, throughout the proof, let $n \in \Z^+$ be an arbitrary (but fixed) positive integer.

**1)** To show reflexivity, we must show that: any element of $\Z$ leaves the same remainder (when divided by $n$) as itself (when divided by $n$).
In symbols, we must show that

$$a \rem n \hskip8pt=\hskip8pt a \rem n$$

is true for every integer $a \in \Z$.

For example, specifying $a$, we must show that: \lf
if $a$ is set to $-9$, then $-9$ leaves the same remainder (when divided by $n$) as $-9$ (when divided by $n$), and \lf
if $a$ is set to $45$, then $45$ leaves the same remainder (when divided by $n$) as $45$ (when divided by $n$), and \lf
so on, for every integer $a \in \Z$ and every positive integer $n \in \Z^+$.

For example, specifying $a$ and $n$, we must show that: \lf
if $a$ is set to $-9$ and $n$ is set to $5$, then $-9$ leaves the same remainder (when divided by $5$) as $9$ (when divided by $5$), and \lf
if $a$ is set to $45$ and $n$ is set to $7$, then $45$ leaves the same remainder (when divided by $7$) as $45$ (when divided by $7$), and \lf
so on, for every integer $a \in \Z$ and every positive integer $n \in \Z^+$.

This is true when $a$ is set to $-9$ and $n$ is set to $5$, because $-9$ leaves a remainder of $-1$ (when divided by $5$) and $-9$ leaves a remainder of $-1$ (when divided by $5$), and these two remainders are the same (because $-1$ equals $-1$). \lf
This is true when $a$ is set to $45$ and $n$ is set to $7$, because $45$ leaves a remainder of $3$ (when divided by $7$) and $45$ leaves a remainder of $3$ (when divided by $7$), and these two remainders are the same (because $3$ equals $3$).

To prove the general case, let $a \in \Z$ be an arbitrary (but fixed) integer.
Now $a$ divided by $n$ leaves some remainder, and this remainder is the same as the remainder that $a$ leaves when divided by $n$.
This shows $a$ is congruent to itself modulo $n$, and so congruence modulo $n$ is a **reflexive** relation.

But we have to be careful, because this doesn't mean that every integer leaves the same remainder as every other integer when divided by any integer.
Rather, it means that, if we *fix* an arbitrary positive integer $n \in \Z^+$ and we *fix* an arbitrary integer $a \in \Z$, then it is indeed true that

$$a \rem n \hskip8pt = \hskip8pt a \rem n.$$

**2)** To show symmetry, we must show that: if an element of $\Z$ leaves the same remainder (when divided by $n$)

<!-- ------------------------------------------------------------------------------------------ -->
\section{Congruence modulo $n$ is an equivalence relation, part 2}

$\tab$ **Theorem**. Let $a,b \in \Z$ be integers, let $n \in \Z^+$ be a positive integer. The following are equivalent. \lf
$\tab\tab$ $1)$ $a$ is congruent to $b$ modulo $n$ \lf
$\tab\tab$ $2)$ $a$ and $b$ leaves the same remainder when divided by $n$ \lf
$\tab\tab$ $3)$ $n$ divides $a-b$ \lf

$\tab$ *Proof*. The equivalence of $1)$ and $2)$ is simply the definition of congruence modulo $n$.

$\tab$ **Corollary**. Let $a,b \in \Z$ be integers, let $n \in \Z^+$ be a positive integer. The following are equivalent. \lf
$\tab\tab$ $1)$ $n$ divides $a-b$
$\tab\tab$ $2)$ $n$ divides $b-a$

$\tab$ *Proof 1*. The equivalence of $1)$ and $2)$ is simply the definition of congruence modulo $n$.
But "$b$ is congruent to $a$ modulo $n$" means that $n$ divides $b-a$ (by the previous theorem). \lf
$\tab$ $\square$

$\tab$ *Proof 2*. *(Only if)* Assume $n$ divides $a-b$. \lf
$\tab$ $\square$

<!-- ------------------------------------------------------------------------------------------ -->
\section{Prime numbers are the best divisors (or the best factors) in the ring $\Z$ of integers}

**Prime numbers** are the *best* **divisors** (or the *best* **factors**) in the ring $\Z$ of integers.
The **prime divisors** (or the **prime factors**) of an integer $n \in \Z$ are the *best* divisors (or the *best* factors) of $n$ in the sense that,
if a prime number $p$ divides an integer $n \in \Z$, then $p$ divides *some* factor in *every* factorization of $n$.

*Example*. Take the integer $20$, which is *not* prime. Now $20$ divides $80$, meaning $20 | 80$.
Since $20$ is *not* prime, then *there exists* a factorization of $80$ where $20$ divides *no* factor. \lf
For instance, $40 \cdot 2$ is a factorization of $80$ (because $40 \cdot 2$ equals $80$); now $20$ divides *some* factor in this factorization because $20$ divides $40$. \lf
For instance, $10 \cdot 8$ is a factorization of $80$ (because $10 \cdot 8$ equals $80$); now $20$ divides *no* factor in this factorization because $20$ doesn't divide $10$ and $20$ doesn't divide $8$. \lf
And so we've found a factorization $a \cdot b$ of $80$ where $20$ divides no factor, because $20$ is *not* prime. \lf
In general, if an integer $n \in \Z$ is *not* prime and $n$ divides an integer $c \in \Z$,
then *there exists* some factorization $a \cdot b$ of $c$ (meaning $a \cdot b$ equals $c$) where $n$ does *not* divide neither factor $a$ nor factor $b$ (even if $n$ *does* happen to divide *some* factors in *some* factorizations of $c$). \lf
In other words, a **non-prime** integer $n$ can divide some factors in some factorizations some of the time,
but it can't divide some factors in all factorizations all of the time,

*Example*. Take the integer $5$, which is prime. Now $5$ divides $80$, meaning $5 | 80$.
Since $5$ is prime, then $5$ also divides *asome* factor in *every* factorization of $80$. \lf
For instance, $40 \cdot 2$ is a factorization of $80$ (because $40 \cdot 2$ equals $80$); now $5$ divides *some* factor in this factorization because $5$ divides $40$. \lf
For instance, $10 \cdot 8$ is a factorization of $80$ (because $10 \cdot 8$ equals $80$); now $5$ divides *no* factor in this factorization. \lf
And we can go on and find *every* factorization $a \cdot b$ of $80$, but $5$ will always divide some factor in any factorization of $80$, because $5$ is prime. \lf
In general, if integer $p \in \Z$ *is* prime and $p$ divides an integer $c \in \Z$,
then in *every* factorization $a \cdot b$ of $c$ (meaning $a \cdot b$ equals $c$) we have that $p$ divides factor $a$ or factor $b$. \lf
In other words, a **prime** integer $p$ can divide some factors in all factorizations all of the time,
and it can divide all factors in all factorizations some of the time,
but it can't divide all factors in all factorizations all of the time. \lf
(There are special numbers which *can* divide everything all of the time; these are called
[**units**][https://en.wikipedia.org/wiki/Unit_(ring_theory)].
The units in $\Z$ are $1$ and $-1$).

So, if a prime number divides an integer $n$, then that prime number divides *some* factor in *every* factorization of $n$.
This is not to say that prime numbers are "magical" or "special" by accident, but by *design*.
That is, prime numbers are not the best divisors of integers because they're lucky, but
because they're *defined* be the best divisors of integers.
(What *could* be seen as an accident, though, is the fact that prime numbers *exist*, because
we can always define really powerful objects with really nice properties, but sometimes these objects will not exist and there's nothing we can do about it.)


\definition An integer $p \in \Z$ is **prime** *iff* it satisfies any of the following equivalent conditions:

$\tab\tab$ **1)** if $p$ divides a product $a \cdot b$, then $p$ divides factor $a$ or factor $b$, for any $a,b \in \Z$ \lf
$\tab\tab$ **2)** if $p | (a \cdot b)$, then $p|a$ or $p|b$, for any $a,b \in \Z$ \lf
$\tab\tab$ **3)** $\forall a,b \in \Z \hskip4pt \langle p | (a \cdot b) \then p|a \text{ or } p|b \rangle$ \lf
$\tab\tab$ **4)** \lf
$\hskip8pt$ $\forall a,b \hskip4pt \langle$ \lf
$\hskip8pt$ $\hskip8pt a,b \in \Z \then \langle$ \lf
$\hskip8pt$ $\hskip32pt p | (a \cdot b) \then p|a \text{ or } p|b$ \lf
$\hskip8pt$ $\hskip8pt \rangle$ \lf
$\hskip8pt$ $\rangle$


The prime numbers in $\Z$ are generalized in
[ring theory][https://en.wikipedia.org/wiki/Ring_theory] to
[prime ideals][https://en.wikipedia.org/wiki/Prime_ideal], and there's lots to learn from a
[commutative ring][https://en.wikipedia.org/wiki/Commutative_ring] by studying its prime ideals.

<!-- ------------------------------------------------------------------------------------------ -->
\section{The integers $\Z$ are a quotient space of $\N \times \N^\times$}

**Theorem**.

*Proof*.

<!-- ------------------------------------------------------------------------------------------ -->
\section{The rational numbers $\Q$ are a quotient space of $\Z \times \Z^\times$}

**Theorem**.

*Proof*.

This means the rational numbers $\Q$ can be constructed as a quotient space of the set $\Z \times \Z^\times$.
The rational numbers $\Q$ have a special relationship with the integers $\Z$:
$\Q$ is the
[*field of fractions*][https://en.wikipedia.org/wiki/Field_of_fractions] of $\Z$.
This means that $\Q$ is the smallest set we can possibly get if you want every element of $\Z$ to have a *multiplicative inverse*.

Similarly, the real numbers $\R$ can be constructed as a quotient space of the
[power set][https://en.wikipedia.org/wiki/Power_set] $\mathcal P \Q$ of the rational numbers $\Q$.

In algebra, the
[complex numbers][https://en.wikipedia.org/wiki/Complex_number] $\C$ can be constructed as a quotient space of the set $\R[x]$,
which is the set of all polynomials (of one variable) with coefficients in $\R$.

In topology, the
[circle][https://en.wikipedia.org/wiki/Circle]
$\S_1$ (aka. the $1$-dimensional sphere) can be constructed as a quotient space of the real numbers $\R$.

<!-- ------------------------------------------------------------------------------------------ -->
\section{What is a coset?}

In
[**group theory**][https://en.wikipedia.org/wiki/Group_theory], **cosets** are some of the most important objects.
A **coset** is a special **subset** of a group that *arises* from a **subgroup**.
To every subgroup $H$ of a group $G$ we can associate **the set of all cosets** of $H$ in $G$.
We can think of the cosets of the subgroup $H$ as "logically attached" to $H$.
That is: every time you think of a particular group $G$, we can immediately think of the subgroups of $G$;
and every time you think of a particular subgroup $H$, we can immediately think of the cosets of $H$.

\vskip8pt
If you see the word **coset** in the wild, you need 3 pieces of data to specify the coset:
$1)$ a **group** $G$, a **subgroup** $H$, and an **element** $g$ of $G$.
Then, the coset that these data specify is written as $gH$.
Every element $g$ of $G$ yields one coset $gH$, but not all of these cosets will be different!
If each element $g$ of $G$ were to generate a different coset $gH$,
then every subgroup $H$ would have as many cosets as $G$ has elements (one for each element of $g$), but this is not (typically) the case.

<!-- ------------------------------------------------------------------------------------------ -->
\section{Example. The (additive) cosets of $3\Z$ in $\Z$}

For $G$ take the additive group of integers $(\Z, +)$,
for $H \subset G$ take the subgroup $3\Z$.
The subgroup $3\Z$ of $\Z$ is defined as

$$3\Z \defined \{\ldots, -12, -9, -6, -3, 0, 3, 6, 9, 9, \ldots\}.$$

It can also be written as

$$3\Z \defined \{ 3n \in \Z \hskip4pt|\hskip4pt n \in \Z \},$$

which reads "the set of all $3n \in \Z$, as $n$ ranges over all elements of $\Z$".
The set $3\Z$ is just the set of all integer multiples of $3 \in \Z$.
Now, each element of $\Z$ yields a coset of $3\Z$ in $\Z$. For instance: \par
- the element $1 \in \Z$ yields the coset $3\Z + 1$, which is defined as $3\Z + 1 := \{\ldots, , \ldots\}$ \par
- the element $2 \in \Z$ yields the coset $3\Z + 2$, which is defined as $3\Z + 2 := \{\ldots, , \ldots\}$ \par
- the element $3 \in \Z$ yields the coset $3\Z + 3$, which is defined as $3\Z + 3 := \{\ldots, , \ldots\}$ \par
- the element $99 \in \Z$ yields the coset $3\Z + 99$, which is defined as $3\Z + 99 := \{\ldots, , \ldots\}$

\vskip8pt
In symbols, we can denote **the set of all cosets** of a subgroup $H$ as ${\rm Cosets}[H]$,
and we can write the set of all cosets of $H$ as

\vskip8pt
$${\rm Cosets}[H] := \{ gH\ |\ g \in G\}$$

\vskip8pt
which reads "${\rm Cosets}[H]$ is **defined** as the set of all sets of the form $gH$, as $g$ ranges over $G$".
We can also build the set of all cosets of all subgroups of $G$, but let's not get too carried away.

<!-- ------------------------------------------------------------------------------------------ -->
\section{Left and right cosets}

So far, we've ignored an important detail about cosets.
If $g \in G$ is an element of $G$ and $H \subset$ is a subgroup of $G$,
then the coset $gH$ is not the same as the coset $Hg$.


These are the **left cosets** and the **right cosets**.

<!-- ------------------------------------------------------------------------------------------ -->
\section{When left and right is the same}

\vskip8pt
Sometimes ${\rm Cosets}[H]$ will form a **group** under the operation it inherits from the parent group $G$,
in which case the group ${\rm Cosets}[H]$ is written $G / H$, which reads "$G$ modulo $H$".
The group $G / H$ is then called "the quotient group of $G$ by $H$", or the "quotient group of $G$ modulo $H$".
Whether ${\rm Cosets}[H]$ is a group or not hinges on a particular property that $H$ must satisfy.

<!-- ------------------------------------------------------------------------------------------ -->
\section{Three lemmas}

So, how do we prove Lagrange's theorem? We'll be using a few technical lemmas.

\vskip8pt
**First Fundamental Lemma of Cosets**. Let $G$ be a group, let $H \subset G$ be a subgroup.
The cosets of $H$ form a **partition** of $G$.

\vskip8pt
**Second Fundamental Lemma of Cosets**. Let $G$ be a group, let $H \subset G$ be a subgroup, let $g \in G$.
If $g \notin H$, then $H$ is **disjoint** from the coset $gH$.
