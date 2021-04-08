<!-- py miatex2html.py set_theory00.md  # Output html file (same name)! -->

---------------------------------------------------------------------------------------------------
<!--
\title_page Unions and intersections
\title_article Unions and intersections
\category0 Set theory
\category1 Zermelo-Fraenkel with Choice
\category2 Unions and intersections
\category3
-->

---------------------------------------------------------------------------------------------------
**Unions** and **intersections** of sets are something I find confusing. But they're super important.
For instance, when learning
[general topology][https://en.wikipedia.org/wiki/General_topology],
we *must* become fluent with **unions**, **intersections**, and other set-theoretic stuff
(like **complements**, **powersets**, **subsets**, **functions**, **covers**, **uncountability**, etc.),
because general topology is basically just the *topology of sets*, and
all the important ideas in general topology
(like **continuous**, **compact**, **metrizable**, **second-countable**, **Hausdorff**, **paracompact**, **countably locally finite**, etc.)
are stated in the language of sets.

<!-- In this chapter we give examples of unions/intersections, then define them, and then
give examples of important objects (in topology and measure theory) that use unions/intersections in their definition:
topological spaces, sigma-algebras, and Borel sigma-algebras. -->

---------------------------------------------------------------------------------------------------
\section{Union: the elements that are in at least one element}

There's two notations to denote unions (both of which I find useful). \lf
One is $\cup A$. This is a *unary* operation. \lf
The other is $A \cup B$. This is a *binary* operation. \lf

The unary operation $\cup$ takes the set $A$ to the set $\cup A$.
The set $\cup A$ is a new set, made of the elements that are in *at least one* element of $A$. \lf
The binary operation $\cup$ takes the sets $A$ and $B$ to the set $A \cup B$.
The set $A \cup B$ is a new set, made of all the elements in $A$ and all the elements in $B$.

\example Let $A$ be the set $\{a1, a2, a3\}$. \lf
Then the set $\cup A$ is the set $\cup \{a1, a2, a3\}$, and this set can also be written as $a1 \cup a2 \cup a3$.
To pin it down explicitly we need more information. \lf
Let $a1$ be the set $\{a11, a12\}$, let $a2$ be the set $\{a21, a22\}$, let $a3$ be the set $\{a31, a32\}$. \lf
Assume that \lf
  $\tab$ $a11 \neq a21$, and $a11 \neq a22$, and $a11 \neq a31$, and $a11 \neq a32$, and \lf
  $\tab$ $a12 \neq a21$, and $a12 \neq a22$, and $a12 \neq a31$, and $a12 \neq a32$, and \lf
  $\tab$ $a21 \neq a11$, and $a21 \neq a12$, and $a21 \neq a31$, and $a21 \neq a32$, and \lf
  $\tab$ $a22 \neq a11$, and $a22 \neq a12$, and $a22 \neq a31$, and $a22 \neq a32$, and \lf
  $\tab$ $a31 \neq a11$, and $a31 \neq a12$, and $a31 \neq a21$, and $a31 \neq a22$, and \lf
  $\tab$ $a32 \neq a11$, and $a32 \neq a12$, and $a32 \neq a21$, and $a32 \neq a22$. \lf
Now the set $\cup A$ is the set $\cup \{a1, a2, a3\}$,
which is the set $\cup\{\{a11, a12\}, \{a21, a22\}, \{a31, a32\}\}$,
which is the set $\{a11, a12, a21, 22, a31, a32, b11, b12, b21, 22, b31, b32\}$, by the definition of "*the elements that are in at least one element*". \lf
Notice that the set $\cup A$ is the set $\cup \{\{a11, a12\}, \{a21, a22\}, \{a31, a32\}\}$ (in *unary notation*) and also the set $\{a11, a12\} \cup \{a21, a22\} \cup \{a31, a32\}$ (in *binary notation*).

\example Let $A$ be the set $\{a1, a2, a3\}$, let $B$ be the set $\{b1, b2, b3\}$. \lf
Then the set $A \cup B$ is the set $\{a1, a2, a3\} \cup \{b1, b2, b3\}$, and this set can also be written as $\cup\{A, B\}$, or as $\cup\{ \{a1, a2, a3\}, \{b1, b2, b3\} \}$.
To pin it down explicitly we need more information. \lf
Assume that \lf
  $\tab$ $a1 \neq b1$, and $a2 \neq b1$, and $a3 \neq b1$, and \lf
  $\tab$ $a1 \neq b2$, and $a2 \neq b2$, and $a3 \neq b2$, and \lf
  $\tab$ $a1 \neq b3$, and $a2 \neq b3$, and $a3 \neq b3$. \lf
Now the set $A \cup B$ is the set $\{a1, a2, a3\} \cup \{b1, b2, b3\}$,
which is the set $\{a1, a2, a3, b1, b2, b3\}$, by the definition of "*all the elements in $A$ and all the elements of $B$*". \lf
Notice that the set $A \cup B$ is the set $\cup \{\{a1, a2, a3\}, \{b1, b2, b3\}\}$ (in *unary notation*) and also the set $\{a1, a2, a3\} \cup \{b1, b2, b3\}$ (in *binary notation*).

The moral of the story is that we can take the union $\cup A$ of a *single* set $A$, but then we're seeing $A$ as a *set of sets*
(because we're focusing on the elements of its elements). \lf
And we can take the union $A \cup B$ of *two* sets $A$ and $B$, but then we're seeing $A$ and $B$ as just *sets*
(because we're focusing on their elements). \lf
But, in
[ZFC][https://www.encyclopediaofmath.org/index.php/ZFC],
a set can only contain other sets.
So the elements of a set $A$ are always sets, which actually makes $A$ a set of sets, and
the elements of the elements of $A$ are also sets, which actually makes $A$ a set of sets of sets, and ...
It's sets all the way down (until you reach the empty set).
So calling something "a set" or "a set of sets" or "a set of sets of sets of sets ... of sets" is just *relative* (to a particular level in this hierarchy).
<!-- What usually happens in practice is that people start with a set $A$ and take $A$ as made of "indivisible points", and
then consider sets of sets ... of sets of elements of $A$.
That is, in practice, there's always a "base level". -->

\definition The **union** $\cup A$ of a set $A$ is the set of all elements that are in *at least one* element of $A$.

\definition The **union** $A \cup B$ of two sets $A$ and $B$ is the set of *all* elements of $A$ and *all* elements $B$.

Axiomatically, in ZFC we form the union $\cup A$ of the set $A$ using the
[**axiom of union**][https://en.wikipedia.org/wiki/Axiom_of_union]. \lf
And we form the union $A \cup B$ of the sets $A$ and $B$ using the
[**axiom of pair**][https://ncatlab.org/nlab/show/axiom+of+pairing]
and the axiom of union.
The axiom of pair yields the **pair** $\{A, B\}$, and the axiom of union yields the **union** $\cup\{A, B\}$.
Then we can define the set $A \cup B$ as the set $\cup\{A, B\}$ (which is confusing because we're using the same symbol $\cup$ for two different operations:
one unary operation and one binary operation).

---------------------------------------------------------------------------------------------------
\section{Intersection: the elements that are in every element}

There's two notations to denote intersections. \lf
One is $\cap A$. This is a *unary* operation. \lf
The other is $A \cap B$. This is a *binary* operation. \lf

The unary operation $\cap$ takes the set $A$ to the set $\cap A$.
The set $\cap A$ is a new set, made of the elements that are in *every* element of $A$. \lf
The binary operation $\cap$ takes the sets $A$ and $B$ to the set $A \cap B$.
The set $A \cap B$ is a new set, made of the elements that $A$ and $B$ have in common.

\example Let $A$ be the set $\{a1, a2, a3\}$. \lf
Then the set $\cap A$ is the set $\cap\{a1, a2, a3\}$, and this set can also be written as $a1 \cap a2 \cap a3$.
To pin it down explicitly we need more information. \lf
Let $a1$ be the set $\{a11, a12\}$, let $a2$ be the set $\{a21, a22\}$, let $a3$ be the set $\{a31, a32\}$. \lf
Assume that \lf
  $\tab$ $a11 \neq a21$, and $a11 \neq a22$, and $a11 \neq a31$, and $a11 \neq a32$, and \lf
  $\tab$ $a12 \neq a21$, and $a12 \neq a22$, and $a12 \neq a31$, and $a12 \neq a32$, and \lf
  $\tab$ $a21 \neq a11$, and $a21 \neq a12$, and $a21 \neq a31$, and $a21 \neq a32$, and \lf
  $\tab$ $a22 \neq a11$, and $a22 \neq a12$, and $a22 \neq a31$, and $a22 \neq a32$, and \lf
  $\tab$ $a31 \neq a11$, and $a31 \neq a12$, and $a31 \neq a21$, and $a31 \neq a22$, and \lf
  $\tab$ $a32 \neq a11$, and $a32 \neq a12$, and $a32 \neq a21$, and $a32 \neq a22$. \lf
Now the set $\cap A$ is the set $\cap \{a1, a2, a3\}$,
which is the set $\cap\{\{a11, a12\}, \{a21, a22\}, \{a31, a32\}\}$,
which is the set $\{\}$, by the definition of "*the elements that are in every element*". \lf
Notice that the set $\cap A$ is the set $\cap \{\{a11, a12\}, \{a21, a22\}, \{a31, a32\}\}$ (in *unary notation*) and also the set $\{a11, a12\} \cap \{a21, a22\} \cap \{a31, a32\}$ (in *binary notation*).

\example Let $A$ be the set $\{a1, a2, a3\}$, let $B$ be the set $\{b1, b2, b3\}$. \lf
Then the set $A \cap B$ is the set $\{a1, a2, a3\} \cap \{b1, b2, b3\}$, and
this set can also be written as $\cap{A, B}$, or as $\cap\{\{a1, a2, a3\}, \{b1, b2, b3\}\}$.
To pin it down explicitly we need more information.
Assume that \lf
  $\tab$ $a1 \neq b1$, and $a2 \neq b1$, and $a3 \neq b1$, and \lf
  $\tab$ $a1 \neq b2$, and $a2 \neq b2$, and $a3 \neq b2$, and \lf
  $\tab$ $a1 \neq b3$, and $a2 \neq b3$, and $a3 \neq b3$. \lf
Now the set $A \cap B$ is the set $\{a1, a2, a3\} \cap \{b1, b2, b3\}$,
which is the set $\{\}$, by the definition of "*all the elements that $A$ and $B$ have in common*". \lf
Notice that the set $A \cap B$ is the set $\cap \{\{a1, a2, a3\}, \{b1, b2, b3\}\}$ (in *unary notation*) and also the set $\{a1, a2, a3\} \cap \{b1, b2, b3\}$ (in *binary notation*).

\definition The **intersection** $\cap A$ of a set $A$ is the set of all elements that are in *every* element of $A$.

\definition The **intersection** $A \cap B$ of two sets $A$ and $B$ is the set of all elements that $A$ and $B$ have *in common*.

---------------------------------------------------------------------------------------------------
\section{The fundamental theorem of unions and intersections: de Morgan's laws}

After understanding what union and intersections *do* (to sets), the next thing is to understand that they're the same.
Well, they're not *actually* the same, but they're two sides of the same coin: unions are
[**dual**][https://en.wikipedia.org/wiki/Dual_(category_theory)]
to intersections. In
[category-theoretic][https://ncatlab.org/nlab/show/category+theory]
language, **unions** are
[**coproducts**][https://en.wikipedia.org/wiki/Coproduct]
and **intersections** are
[**products**][https://en.wikipedia.org/wiki/Product_(category_theory)].
Also, unions are defined using logical
[**disjunction**][https://en.wikipedia.org/wiki/Logical_disjunction]
(ie. logical **or**), and
intersections are defined using logical
[**conjunction**][https://en.wikipedia.org/wiki/Logical_conjunction]
(ie. logical **and**).
Disjunctions are products and conjunctions are coproducts, so disjunctions are dual to conjunctions.
The duality between unions and intersections is known as
[**de Morgan's theorem**][https://en.wikipedia.org/wiki/De_Morgan%27s_laws]
(or de Morgan's laws, or de Morgan duality).

Before stating the fundamental theorem of unions and intersecions (aka. de Morgan's laws),
we need a new operation: **complement** (aka. **set complement** or **set-theoretic complement**).

\example Let $A$ be the set $\{a1, a2, a3, a4, a5\}$, let $A' \subset A$ be the set $\{a2, a4, a5\}$.
The **complement** $\overline{A'}$ of $A'$ (in $A$), also denoted $A \setminus A'$, is the set $\{a1, a3\}$, meaning \lf
  $\tab\tab1)$ $\overline{A'}$ equals $\{a1, a3\}$ \lf
  $\tab\tab2)$ $A \setminus A'$ equals $\{a1, a3\}$. \lf

\definition Let $A$ be a set, and let $A' \subset A$ be a subset of $A$. \lf
The **complement** $\overline{A'}$ of $A'$ (in $A$), also denoted $A \setminus A'$, is the set of all elements of $A$ that are *not* elements of $A'$.
In symbols, \lf
  $\tab\tab1)$ $\overline{A'} \defined \{a \in A \pipe a \notin A' \}$ \lf
  $\tab\tab2)$ $A \setminus A' \defined \{a \in A \pipe a \notin A' \}$. \lf

We're ready to state

\theorem{(de Morgan's theorem)} Let $A$ be a set, let $A1$ and $A2$ be subsets of $A$. Now, \lf
  $\tab\tab1)$ $\overline{A1 \cup A2} \equals \overline{A1} \cap \overline{A2}$ \lf
  $\tab\tab2)$ $\overline{A1 \cap A2} \equals \overline{A1} \cup \overline{A2}$. \lf
Equivalently, \lf
  $\tab\tab1')$ $A \setminus (A1 \cup A2) \equals (A \setminus A1) \hskip4pt\cap\hskip4pt (A \setminus A2)$ \lf
  $\tab\tab2')$ $A \setminus (A1 \cap A2) \equals (A \setminus A1) \hskip4pt\cup\hskip4pt (A \setminus A2)$. \lf

\proof TODO

---------------------------------------------------------------------------------------------------
<!-- \section{Unions and intersections of families of subsets}

Things get real fun when we encounter **families of subsets**, aka. **collections of subsets** (which is common in **topology** and **measure theory**). \\
If $X$ is a set, then a family of subsets of $X$ is just a **set of subsets of $X$**, aka. a $2$-set over $X$. \\
If $A$ is a set of subsets of $X$, then $A$ is usually denoted $\{U_i | i \in I\}$ with the proviso that each $U_i$ is a subset of $X$. -->

---------------------------------------------------------------------------------------------------
<!-- \section{Topological spaces through unions and intersections} -->

---------------------------------------------------------------------------------------------------
<!-- \section{Sigma-algebras through unions and intersections} -->

---------------------------------------------------------------------------------------------------
<!-- \section{Borel sigma-algebras through unions and intersections} -->

---------------------------------------------------------------------------------------------------
<!-- \section{Functions as a special case of relations}
We've talked about a **relation** being determined by three pieces of data: \lf
  $\tab\tab1)$ a set $A$ called the **domain** of the relation, \lf
  $\tab\tab2)$ a set $B$ called the **codomain** of the relation, \lf
  $\tab\tab2)$ a set $R \subset A \times B$ called the **graph** of the relation, \lf
which is why we denote a relation from $A$ to $B$ as an *ordered triple* $(R, A, B)$.

Since $A \times B$ is a set of ordered pairs and $R$ (as given above) is a subset of $A \times B$, then
the $R$ is also a set of ordered pairs.
Many authors simply use this set of ordered pairs to *define* what a relation is.
So, to many, a **relation** is just *a set of ordered pairs*.
This introduces a technical problem when talking about *equality* of relations, and this problem carries over to functions. -->

---------------------------------------------------------------------------------------------------
<!-- \section{Partial orders}

\definition Let $P$ be a set. \lf
A **partial order** $\leq_P$ on $P$ is a relation from $P$ to $P$ that is **reflexive**, **antisymmetric**, and **transitive**.
\hrule

\definition Let $P$ be a set, let $\leq_P$ be a partial order on $P$. \lf
A **poset** $\mathcal P$ is a pair $\mathcal P := (P, \leq_P)$. \lf
So, a **poset** (aka. a **partially ordered set**) is a set $P$ together with a partial order $\leq_P$ on $P$.
\hrule

\definition A **lattice** is a poset $(L, \leq_L)$ is a set 
\hrule

\example Here's a **partial order** that is not a lattice.
\hrule -->

---------------------------------------------------------------------------------------------------
<!-- \section{Appendix. ZFC axioms}
A minimal list of ZFC axioms is: \lf
$\tab\tab1)$ extension: two sets are equal *iff* they have the same elements \lf
$\tab\tab2)$ union: every set has a union \lf
$\tab\tab3)$ powerset: every set has a power set \lf
$\tab\tab4)$ infinity: there exists an infinite set \lf
$\tab\tab5)$ *schema* of replacement: the image of every function is a set \lf
$\tab\tab6)$ regularity: no set can be an element of itself \lf
$\tab\tab7)$ choice: every Cartesian product of nonempty sets is nonempty \lf

This list of axioms is minimal in the sense that all the axioms in it are independent of each other (ie. *pairwise* independent).
However, people often list more axioms for ZFC, and these can be derived from the previous ones (although I don't know how):

$\tab\tab1)$ empty set: there exists an empty set \lf
$\tab\tab2)$ pair: we can always stuff two sets into a set: the pair \lf
$\tab\tab3)$ *schema* of separation: we can always take subsets \lf

**First-order logic** (aka. predicate logic) is **complete**, **compact**, and **undecidable**.
Every **first-order theory** is **incomplete**.

A **complete logic** is a **logic** where satisfiability is equivalent to provability [every theory has a model, every model has a theory?]. An incomplete logic is a logic that is not complete.
A **complete theory** is a **theory** where every **formula** or its negation is provable. An incomplete theory is a theory that is not complete. 

What do you call a (consistent) theory that can prove its own consistency?
Eg. ZFC (Zermelo-Frenkel with Choince) can't prove its own consistency (unless ZFC is inconsistent, in which case it can prove anything).
Eg. PA (Peano arithmetic) can't prove its own consistency (unless PA is inconsistent, in which case it can prove anything).

ZF is not finitely axiomatizable, which means we can't axiomatized it using finitely many axioms, so we must axiomatize it with infinitely many axioms.
In order to produce infinitely many axioms, we can use an **axiom schema**, which is a template for producing infinitely many axioms.

An **intentional definition** gives *necessary* and *sufficient* conditions for belonging to a set.
An **extensional definition** simply lists all the element of the set.

Sets are determined **up to isomorphism** by their number of elements.
Sets are determined **up to equality** by their elements. -->

---------------------------------------------------------------------------------------------------
<!-- \section{MathJax fonts}

$ABCDEFGHIJKLMNOPQRSTUVWXYZ$ none \lf
$\mathit{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathit \lf
$\mathrm{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathrm \lf
$\mathcal{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathcal \lf
$\mathscr{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathscr \lf
$\mathbb{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathbb \lf
$\mathfrak{ABCDEFGHIJKLMNOPQRSTUVWXYZ}$ \\mathfrak \lf -->
