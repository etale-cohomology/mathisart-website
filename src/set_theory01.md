<!-- py miatex2html.py set_theory01.md  # Output html file (same name)! -->

---------------------------------------------------------------------------------------------------
<!--
\title_page Fundamental theorem of equivalence relations
\title_article The fundamental theorem of equivalence relations
\category0 Set theory
\category1 Zermelo-Fraenkel with Choice
\category2 Relations
\category3 Equivalence relations
-->

---------------------------------------------------------------------------------------------------
[**Equivalence relations**][https://en.wikipedia.org/wiki/Equivalence_relation]
are "essentially the same" as
[**partitions**][https://en.wikipedia.org/wiki/Partition_of_a_set].
More precisely, every equivalence relation on a set $X$ yields a partition of $X$, and every partition of $X$ yields an equivalence relation on $X$.
Our goal here is to prove:

\theorem{(the fundamental theorem of equivalence relations)} Every equivalence relation yields a partition. Every partition yields an equivalence relation.

This is very surprising, particularly because the definitions of **equivalence relation** and **partition** are nothing alike.

\definition An **equivalence relation** on a set $X$ is a relation on $X$ that is **reflexive**, **symmetric**, and **transitive**.

\definition A **partition** of a set $X$ is a **pairwise-disjoint** **cover** of $X$.

What all of this means, we explain in the sequel.

---------------------------------------------------------------------------------------------------
\section{Every equivalence relation yields a partition. Example}

Every equivalence relation $(R, X, X)$ on an arbitrary set $X$ gives rise a partition of $X$, and
that partition is the quotient set $X/R$ of all equivalence classes of $R$.
This means the **cells** of the partition are the **equivalence classes** of $R$.

\example Let $X$ be the set

$$X \defined \{0, 1, 2, 3, 4\},$$

let $(R, X, X)$ be the **equivalence relation** on $X$ whose **graph** $R$ is given by

$$R \defined \{(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 3), (3, 4), (4, 3), (4, 4)\}.$$

We'll show that $R$ gives rise to a specific partition of $X$ that is intimately related to $R$.
But first, it's not clear that $R$ is an equivalence relation, so let's prove that $R$ satisfies the properties of an equivalence relation.
For $R$ to satisfy the properties of an equivalence relation, $R$ must be:
$1)$ reflexive, $2)$ symmetric, and $3)$ transitive. \lf
For $R$ be to be **reflexive**,  the following statement must hold: $a$ is $R$-related to $a$ (for arbitrary $a \in X$). \lf
For $R$ be to be **symmetric**,  the following statement must hold: if $a$ is $R$-related to $b$, then $b$ is $R$-related to $a$ (for arbitrary $a,b \in X$). \lf
For $R$ be to be **transitive**, the following statement must hold: if $a$ is $R$-related to $b$ and $b$ is $R$-related to $c$, then $a$ is $R$-related to $c$ (for arbitrary $a,b,c \in X$). \lf

The equivalence relation $(R, X, X)$ gives rise to *two* **equivalence classes**, meaning $X/R$ has *two* elements.
And the equivalence classes of $R$, which are precisely the elements of $X/R$, are the following: $\{0, 1, 2\}$ and $\{3, 4\}$.
So, $X/R$ is the set

$$X/R \defined \{\{0, 1, 2\}, \{3, 4\}\}.$$

Why are the equivalence classes of $R$ the subsets $\{0, 1, 2\} \subset X$ and $\{3, 4\} \subset X$?
To answer this, we can compute the equivalence class $a/R$ of *each* element $a$ of $X$,
also denoted $[a]_R$ or $[a]$, and see that the only results are $\{0, 1, 2\}$ or $\{3, 4\}$. \lf

The equivalence class $0/R$ of $0$ under $R$ is the set of all elements of $X$ that $0$ is $R$-related to.
Looking at the definition of $R$, we see that \lf
$0$ is $R$-related to $0$ because $(0, 0) \in R$, and \lf
$0$ is $R$-related to $1$ because $(0, 1) \in R$, and \lf
$0$ is $R$-related to $2$ because $(0, 2) \in R$, and \lf
$0$ is *not* $R$-related to $3$ because $(0, 3) \notin R$, and \lf
$0$ is *not* $R$-related to $4$ because $(0, 4) \notin R$. \lf
So, the equivalence class $0/R$ of $0$ under $R$ is the set $\{0, 1, 2\}$, meaning $0/R = \{0, 1, 2\}$. \lf

The equivalence class $1/R$ of $1$ under $R$ is the set of all elements of $X$ that $1$ is $R$-related to.
Looking at the definition of $R$, we see that \lf
$1$ is $R$-related to $0$ because $(1, 0) \in R$, and \lf
$1$ is $R$-related to $1$ because $(1, 1) \in R$, and \lf
$1$ is $R$-related to $2$ because $(1, 2) \in R$, and \lf
$1$ is *not* $R$-related to $3$ because $(1, 3) \notin R$, and \lf
$1$ is *not* $R$-related to $4$ because $(1, 4) \notin R$. \lf
So, the equivalence class $1/R$ of $1$ under $R$ is the set $\{0, 1, 2\}$, meaning $1/R = \{0, 1, 2\}$. \lf

The equivalence class $2/R$ of $2$ under $R$ is the set of all elements of $X$ that $2$ is $R$-related to.
Looking at the definition of $R$, we see that \lf
$2$ is $R$-related to $0$ because $(2, 0) \in R$, and \lf
$2$ is $R$-related to $1$ because $(2, 1) \in R$, and \lf
$2$ is $R$-related to $2$ because $(2, 2) \in R$, and \lf
$2$ is *not* $R$-related to $3$ because $(2, 3) \notin R$, and \lf
$2$ is *not* $R$-related to $4$ because $(2, 4) \notin R$. \lf
So, the equivalence class $2/R$ of $2$ under $R$ is the set $\{0, 1, 2\}$, meaning $2/R = \{0, 1, 2\}$. \lf

The equivalence class $3/R$ of $3$ under $R$ is the set of all elements of $X$ that $3$ is $R$-related to.
Looking at the definition of $R$, we see that \lf
$3$ is *not* $R$-related to $0$ because $(3, 0) \notin R$, and \lf
$3$ is *not* $R$-related to $1$ because $(3, 1) \notin R$, and \lf
$3$ is *not* $R$-related to $2$ because $(3, 2) \notin R$, and \lf
$3$ is $R$-related to $3$ because $(3, 3) \in R$, and \lf
$3$ is $R$-related to $4$ because $(3, 4) \in R$. \lf
So, the equivalence class $3/R$ of $3$ under $R$ is the set $\{3, 4\}$, meaning $3/R = \{3, 4\}$. \lf

The equivalence class $4/R$ of $4$ under $R$ is the set of all elements of $X$ that $4$ is $R$-related to.
Looking at the definition of $R$, we see that \lf
$4$ is *not* $R$-related to $0$ because $(3, 0) \notin R$, and \lf
$4$ is *not* $R$-related to $1$ because $(3, 1) \notin R$, and \lf
$4$ is *not* $R$-related to $2$ because $(3, 2) \notin R$, and \lf
$4$ is $R$-related to $3$ because $(3, 3) \in R$, and \lf
$4$ is $R$-related to $4$ because $(3, 4) \in R$. \lf
So, the equivalence class $4/R$ of $4$ under $R$ is the set $\{3, 4\}$, meaning $4/R = \{3, 4\}$. \lf

This sums up the situation: \lf
$\tab\tab$ $0/R \equals \{0, 1, 2\}$ \lf
$\tab\tab$ $1/R \equals \{0, 1, 2\}$ \lf
$\tab\tab$ $2/R \equals \{0, 1, 2\}$ \lf
$\tab\tab$ $3/R \equals \{3, 4\}$ \lf
$\tab\tab$ $4/R \equals \{3, 4\}$ \lf
$\tab\tab$ $X/R \equals \{0, 1, 2, 3, 4\}/R \equals \{\{0, 1, 2\}, \{3, 4\}\}.$ \lf

And here comes the punchline.
The set $\{0, 1, 2\}$ and the set $\{3, 4\}$, which are the elements of the set $X/R$, form a **partition** $P$ of $X$, so that the set

$$P \defined \{\{0, 1, 2\}, \{3, 4\}\}$$

is a partition of $X$, because the elements of $P$ are pairwise disjoint (since $\{0, 1, 2\} \cap \{3, 4\} = \{\}$), and
$\cup P$ is $X$ (since $\cup P$ is $\cup\{\{0, 1, 2\}, \{3, 4\}\}$, which is $\{0, 1, 2, 3, 4\}$, which is $X$).

So, the equivalence relation $(R, X, X)$ yields a partition of $X$, and this partition is $X/R$.
More precisely, the **cells** of the partition $\{\{0, 1, 2\}, \{3, 4\}\}$ are precisely the **equivalence classes** of $R$,
so that the **partition** $\{\{0, 1, 2\}, \{3, 4\}\}$ is equal to the **quotient set** $X/R$, which is the set of all equivalence classes of $R$,
which is also the set $\{\{0, 1, 2\}, \{3, 4\}\}$ because the equivalence classes of $R$ are $\{0, 1, 2\}$ and $\{3, 4\}$. \lf
\qed

---------------------------------------------------------------------------------------------------
\section{Every equivalence relation yields a partition. Proof}

\theorem{1} Let $R$ be an **equivalence relation** on a set $X$.
Now $R$ yields a **partition** of $X$. More precisely, the **equivalence classes** of $R$ form a partition of $X$.
In other words, if $R$ is an equivalence relation, then the **quotient set** $X/R$ is a **partition** of $X$.

\proof "If $R$ is an equivalence relation, then the quotient set $X/R$ is a partition of $X$".
This is a bold claim, so we better make sure we understand it. If $X$ is a set and $R$ is an equivalence relation, what does $X/R$ look like?
Well, $X/R$ is the set of all **equivalence classes** of $R$. So, every **element** of the set $X/R$ is a **subset** of the set $X$.
So, $X/R$ is a *set of subsets* of $X$, and so $X/R$ is a *subset of the power set* $\Po X$.
This means the set $X/R$ is a candidate to be a partition of $X$, because a partition of $X$ must be made up of subsets of $X$.
But there's three more requirements:

$\tab\tab1)$ the [**(unary) union**](set_theory00.html) $\bigcup X/R$ must be *all* of $X$, \lf
$\tab\tab2)$ the elements of $X/R$ must *all* be disjoint with each other (ie. pairwise disjoint), and \lf
$\tab\tab3)$ every element of $X/R$ must be nonempty. \lf

First, we'll prove two facts:

$\tab\tab1)$ Every element of $X$ is in *at least one* equivalence class of $R$. \lf
$\tab\tab2)$ Every element of $X$ is in *at most one* equivalence class of $R$.

Together, $1)$ and $2)$ imply:

$\tab\tab3)$ Every element of $X$ is in *exactly one* equivalence class of $R$.

And $3)$ implies:

$\tab\tab4)$ The equivalence classes of $R$ form a partition of $X$.

And $4)$ is the desired result.

To prove $1)$, let $a \in X$ be an (arbitrary, but fixed) element of $X$.
Since $R$ is an equivalence relation, then in particular $R$ is **reflexive**.
So $a$ is $R$-related to $a$ (by the definition of *reflexive*), or equivalently $(a, a) \in R$, or equivalently $aRa$. \lf
Recall that $[a]$ is the set of all elements of $X$ that are $R$-related to $a$.
Since $a$ is an element of $X$ that is $R$-related to $a$, then $a$ is in $[a]$, by the definition of $[a]$. \lf
So the element $a \in X$ is at least in the equivalence class $[a]$.
In particular, the element $a \in X$ is in *at least one* equivalence class.
This proves $1)$.

To prove $2)$, let $a \in X$ be an (arbitrary, but fixed) element of $X$. From $1)$ we know that $a$ is in the equivalence class $[a]$. \lf
Now comes the magic: suppose $a$ is in some other equivalence class, in addition to the equivalence class $[a]$.
This equivalence class would be the set of all elements that are $R$-related to *some* (mysterious) element;
we don't know what this (mysterious) element is, or even if it exists, but let's call it $b$.
To be specific, suppose $a$ is in the equivalence class $[b]$, which is the set of all elements of $X$ that are $R$-related to $b \in X$.
(Notice that the element $b \in X$ is not arbitrary, but it's a very specific element that depends on what $a$ we've chosen.)
By the definition of $[b]$, we know that $a$ is $R$-related to $b$, because $a$ is in $[b]$.
But $R$ is **symmetric** (because $R$ is an equivalence relation), and this implies that $b$ is also $R$-related to $a$.

Well, this *contradicts* the assumption that $a$ is in some other equivalence class, which proves that $a$ can't be in some other equivalence class.
More specifically, it proves that, if we dare to dream that $a$ is in some equivalence class $[b]$, then $b$ must actually be $a$ (meaning $b = a$),
and so $[b]$ must actually be $[a]$ (meaning $[b] = [a]$).

---------------------------------------------------------------------------------------------------
\section{Every partition yields an equivalence relation. Example}
\example Let $X$ be the set $\{0, 1, 2, 3, 4\}$,
let $P$ be the **partition** of $X$ given by $P \defined \{\{0, 1, 2\}, \{3, 4\}\}$.

This was an example of a general theorem that applies to all sets and all partitions of sets:
every partition $P$ of an arbitrary set $X$ gives rise to an equivalence relation on $X$,
and the equivalence classes of that equivalence relation are the cells of the partition $P$.

---------------------------------------------------------------------------------------------------
\section{Every partition yields an equivalence relation. Proof}

\theorem{2} Let $P$ be a partition of a set $X$. Now the partition $P$ induces an equivalence relation on $X$.

\proof TODO

---------------------------------------------------------------------------------------------------
\section{The fundamental theorem of equivalence relations}

We can now prove:

\theorem{(the fundamental theorem of equivalence relations)} Every equivalence relation yields a partition. Every partition yields an equivalence relation.

\proof Theorem $1$ together with theorem $2$ prove this result. \lf
\qed
