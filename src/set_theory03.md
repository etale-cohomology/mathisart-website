<!-- py miatex2html.py set_theory03.md  # Output html file (same name)! -->

---------------------------------------------------------------------------------------------------
<!--
\title_page The singleton set is unique
\title_article The singleton set is unique up to unique set-isomorphism
\category0 Set theory
\category1 Zermelo-Fraenkel with Choice
\category2 Functions
\category3 Bijections
-->

---------------------------------------------------------------------------------------------------
A **singleton set** (or just a **singleton**) is a set with *exactly one* element. There is "essentially just one" singleton set.
This a very different situation than that for the **empty set**, where we know there's *exactly one* empty set.
Why does this happen? How does this happen? We try to explain this.

---------------------------------------------------------------------------------------------------
\section{Any two singleton sets are "essentially the same"}

\definition A **set-isomorphism** is a
[**bijection**][https://en.wikipedia.org/wiki/Bijection,_injection_and_surjection]
between sets.

\theorem There exists a unique set-isomorphism between any two singleton sets.
There's "exactly one" singleton set, not necessarily because any two singleton sets have the same elements
(which is how **equality** of sets is defined),
but because, given any two singleton sets, there's exactly one set-isomorphism (ie. a bijection) between the two.
This allows us to say there's "exactly one" singleton set even when there *really* isn't exactly one singleton set.
In other words, this allows us to say there's a *unique* singleton set,
provided we're willing to consider two singletons sets "the same" whenever there exists a unique set-isomorphism between the two.
The jargon for this is: there's a unique singleton set,
[up to][https://en.wikipedia.org/wiki/Up_to]
unique set-isomorphism.

\proof Why do we talk about "the" singleton set? Is there *only one* singleton set?
For instance, using the
[**axiom of extension**][https://en.wikipedia.org/wiki/Axiom_of_extensionality]
(aka. the axiom of extensionality), we can prove that there's only one empty set.
This is because the axiom of extension says that *equality of sets* is
[**materially equivalent**][https://en.wikipedia.org/wiki/If_and_only_if]
to *equality of their elements*. More precisely, two sets are equal
[**IFF**][https://en.wikipedia.org/wiki/Logical_biconditional]
they have exactly the same elements.
If there were two empty sets, then for them to be not equal they'd have to differ by (at least) one element:
one of the two empty sets would have to have an element that is not in the other.
But this can't happen because an empty set has, by definition, no elements.

So, what about singleton sets? There's certainly more than one,
because, for instance, the singleton set $\{0\}$ is not the same as the singleton set $\{1\}$:
the set $\{0\}$ has the one element $0$, and the set $\{1\}$ has the one element $1$;
and $0$ is *not* equal to $1$, under *most* reasonable interpretations of the symbol $0$ and the symbol $1$
(for example, in the
[zero ring][https://ncatlab.org/nlab/show/trivial+ring],
$0$ *does* equal $1$).

But these two sets are **set-isomorphic**: there exists a **set-isomorphism** (ie. a **bijection**) between the two.
What does a bijection between $\{0\}$ and $\{1\}$ look like?
Well, for starters, what does a **function** between $\{0\}$ and $\{1\}$ look like?
Consider a function $f: \{0\} \to \{1\}$ from $\{0\}$ to $\{1\}$.
By definition, the function $f$ must map each element of $\{0\}$ to exactly one element of $\{1\}$.
But $\{0\}$ has exactly one element, namely $0$, so all we need to decide is: what is the image of $0$ under $f$?
In other words, what is $f[0]$? Well, how many choices do we have?
For each element of $\{1\}$ we have one choice, and each choice leads to a different function.
But $\{1\}$ only has one elements, namely $1$, so there's only one choice:
the only possible answer is that $f$ must map $0$ to $1$, meaning $f: 0 \mapsto 1$ or equivalently $f[0] = 1$.

So, there's only one function from $\{0\}$ to $\{1\}$. And this function $f$ is very special: it's a *bijection*.
Why is $f$ a bijection? Because $f$ is an **injection** (distinct elements of $\{0\}$ go to distinct elements of $\{1\}$),
and because $f$ is a **surjection** (every element of $\{1\}$ is the image of at least one element of $\{0\}$).
So, $f$ is an **isomorphism of sets**.

And, since there's *only one* function from $\{0\}$ to $\{1\}$, this bijection/set-isomorphism is *unique*.
This is very important, so let's say it again: *there's a unique set-isomorphism from $\{0\}$ to $\{1\}$*.
But when arguing this way we never used any specific properties of $0$ or of $1$.
All we used was the fact that the sets $\{0\}$ and $\{1\}$ have *exactly one* element.
So, the same argument applies to any two sets with exactly one element (any two **singleton** sets). How?

Well, let $A$ be an arbitrary (but fixed) singleton set, and let $B$ be an arbitrary (but fixed) singleton set. \lf
Since $A$ is a singleton set, we can write $A$ as $\{a\}$, where the symbol $a$ is an arbitrary label for whatever element the singleton set $A$ happens to contain. \lf
Since $B$ is a singleton set, we can write $B$ as $\{b\}$, where the symbol $b$ is an arbitrary label for whatever element the singleton set $B$ happens to contain. \lf

If it happens that $a$ equals $b$, then $\{a\}$ and $\{b\}$ have exactly the same elements, and
it follows that $\{a\}$ equals $\{b\}$ (by the **axiom of extension**).

If it happens that $a$ does *not* equal $b$, then $\{a\}$ and $\{b\}$ don't have exactly the same elements,
and it follows that $\{a\}$ does *not* equal $\{b\}$ (by the **axiom of extension**).
Still, we claim there's a unique set-isomorphism between $\{a\}$ and $\{b\}$.
To see this, let $f: \{a\} \to \{b\}$ be a **function** from $\{a\}$ to $\{b\}$.
By the definition of function, $f$ must map each element of $\{a\}$ to exactly one element of $\{b\}$.
But $\{a\}$ has exactly one element (namely, $a$) and $\{b\}$ has exactly one element (namely, $b$), so the only possible function is $f : a \mapsto b$,
which is the function that maps $a$ to $b$.
This function is both an **injection** (distinct elements of $\{a\}$ go to distinct elements of $\{b\}$) and
a **surjection** (every element of $\{b\}$ is the image of at least one element of $\{a\}$).
So, it turns out that $f: a \mapsto b$ is a **bijection**.
Single $f$ is the only possible function from $\{a\}$ to $\{b\}$, this bijection is *unique*.
But a bijection is, by definition, a **set-isomorphism** (aka. an isomorphism of sets).
So, *there's a unique set-isomorphism* from $\{a\}$ to $\{b\}$.
Since $\{a\}$ and $\{b\}$ are arbitrary singleton sets, it follows that there's a unique set-isomorphism between any two singleton sets. \lf
\qed
