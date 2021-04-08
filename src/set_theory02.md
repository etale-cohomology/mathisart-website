<!-- py miatex2html.py set_theory02.md  # Output html file (same name)! -->

---------------------------------------------------------------------------------------------------
<!--
\title_page Images and preimages
\title_article The preimage function is a morphism of Boolean algebras
\category0 Set theory
\category1 Zermelo-Fraenkel with Choice
\category2 Functions
\category3 Images and preimages
-->

---------------------------------------------------------------------------------------------------
Functions are some of the most important objects in math. So they're studied all over the place. \lf
In calculus,                               you study differentiable functions. \lf
In topology,                               you study functions that preserve *topological structure* (continuous functions). \lf
In group theory,                           you study functions that preserve *group structure* (group morphisms). \lf
In ring theory,                            you study functions that preserve *ring structure* (ring morphisms). \lf
In complex analysis,                       you study functions that preserve *complex structure* (holomorphic functions). \lf
In the theory of topological    manifolds, you study continuous     functions between topological manifolds. \lf
In the theory of differentiable manifolds, you study differentiable functions between differentiable manifolds. \lf
In the theory of smooth         manifolds, you study smooth         functions between smooth manifolds. \lf
And so on.

For sets, the functions that preserve *set structure* are simply...
[**functions**][https://en.wikipedia.org/wiki/Function_(mathematics)]. (Sets don't have a lot of structure.)
The *core idea* of functions is very simple:

$\tab\tab$ *associate one object to every object*.

But there's a ton of important stuff that can be deduced from this idea without building too much technical machinery.
For example, every function $f: A \to B$ between **sets** gives rise to a function $f^*: \Po B \to \Po A$ between their
[**power sets**][https://en.wikipedia.org/wiki/Power_set],
going in the *opposite direction*.
The function $f^*: \Po B \to \Po A$ can be called the **preimage function** of $f$, or the **contravariant subset function** of $f$,
and it has very nice properties.
For starters, $f^*: \Po B \to \Po A$ preserves **unions**, **intersections**, **complements**, and **inclusions**.
The power set of a set is always a
[**Boolean algebra**][https://ncatlab.org/nlab/show/Boolean+algebra]
(under unions, intersections, complements, and inclusions), and
the preimage function $f^*: \Po B \to \Po A$ preserves its Boolean algebra structure:
$f^*: \Po B \to \Po A$ is a Boolean algebra morphism, or a morphism of Boolean algebras.
There's a **dual** function function $f^*: \Po B \to \Po A$, which we denote $f_*: \Po A \to \Po B$ and which we can call
the **image function** of $f$, or the **covariant subset function** of $f$.
The function $f_*: \Po A \to \Po B$ goes in the *same direction* as $f: A \to B$
  (that is, if $f$ goes from $A$ to $B$, then $f_*$ goes from $\Po A$ to $\Po B$).
The function $f_*: \Po A \to \Po B$ doesn't behave as nicely as is dual function $f^*: \Po B \to \Po A$, but it still warrants attention.

---------------------------------------------------------------------------------------------------
\section{The image function and the preimage function. A first look}

Let $f: \{0, 1, 2\} \to \{5, 6\}$ be a map from the set $\{0, 1, 2\}$ to the set $\{5, 6\}$,
and let $f: \{0, 1, 2\} \to \{5, 6\}$ be defined by \lf
  $\tab\tab$ $f:0 \mapsto 5$ \lf
  $\tab\tab$ $f:1 \mapsto 6$ \lf
  $\tab\tab$ $f:2 \mapsto 5$. \lf

First, take the **element** $1 \in \{0, 1, 2\}$ of $\{0, 1, 2\}$. \lf
Consider the *(unique!)* **image** of $1$ under $f$. \lf
The **image** of $1 \in \{0, 1, 2\}$ under $f$ is denoted $f[1]$, or $f(1)$, and
it's the *sole* **element** of $\{5, 6\}$ that $1$ is $f$-associated to. \lf
By the definition of $f$, the image $f[1]$ of $1$ under $f$ is the element $6 \in \{5, 6\}$. \lf
Notice that $1$ is an *element* of $\{0, 1, 2\}$, and $f[1]$ is an *element* of $\{5, 6\}$.

Second, take the **subset** $\{0, 2\} \subset \{0, 1, 2\}$ of $\{0, 1, 2\}$. \lf
Consider the *(unique!)* **image** of *each* element of $\{0, 2\}$ under $f$. \lf
The **image** of $0 \in \{0, 2\}$ under $f$ is denoted $f[0]$, or $f(0)$, and
it's the *sole* element of $\{5, 6\}$ that $0$ is $f$-associated to. \lf
The **image** of $2 \in \{0, 2\}$ under $f$ is denoted $f[2]$, or $f(2)$, and
it's the *sole* element of $\{5, 6\}$ that $2$ is $f$-associated to. \lf
By the definition of $f$, the image $f[0]$ of $0$ under $f$ is the element $5 \in \{5, 6\}$. \lf
By the definition of $f$, the image $f[2]$ of $2$ under $f$ is the element $5 \in \{5, 6\}$. \lf
Now, the **image** of $\{0, 2\}$ under $f$ is defined as the set $\{f[0], f[2]\}$,
which can also be written as the set $\{5, 5\}$ (using the definition of $f$), which is also the set $\{5\}$ (sets don't allow repetitions). \lf
The **image** of $\{0, 2\}$ under $f$ is denoted $f_*[\{0, 2\}]$, or simply $f(\{0, 2\})$, and
it's the *sole* **subset** of $\{5, 6\}$ that $\{0, 2\}$ if $f$-associated to. \lf
Notice that $\{0, 2\}$ is a *subset* of $\{0, 1, 2\}$, and $f_*[\{0, 2\}]$ is a\ *subset* of $\{5, 6\}$.

Third, take the **subset** $\{5\} \subset \{5, 6\}$ of $\{5, 6\}$. \lf
Consider the *elements* of $\{0, 1, 2\}$ that have some element of $\{5, 6\}$ as their image under $f$. \lf
The **preimage** of $\{5\}$ under $f$ is defined as the set of all such *elements*, and
it's denoted $f^*[\{5\}]$, or $f^{-1}[\{5\}]$ (not to be confused with the *inverse function* of $f$, which doesn't always exist!).

In general, the **image** of a subset $A' \subset A$ under $f$ is denoted $f_*[A']$, or simply $f(A')$, and in symbols you can write it down as \lf
  $\tab\tab$ $f_*[A'] \defined \{f[a] \in B \pipe a \in A'\}$, \lf
and you can read this as *"the set of all $f[a]$ in $B$ as $a$ ranges over $A'$"*.

In general, the **preimage** of a subset $B' \subset B$ under $f$ is denoted $f^*[B']$, or also $f^{-1}(B')$, and in symbols you can write it down as \lf
  $\tab\tab$ $f^*[B'] \defined \{a \in A \pipe f[a] \in B'\}$, \lf
and you can read this as *"the set of all $a$ in $A$ whose image $f[a]$ is in $B'$"*.

<!-- Now let's increase the level of abstraction.

Let $f: A \to B$ be a function from a set $A$ to a set $B$. \lf

First, take an *element* $a \in A$ of $A$, and consider its *(unique!)* **image** under $f$;
the **image** of $a \in A$ under $f$ is denoted $f[a]$, or $f(a)$, and it's the *sole* element of $B$ that $a$ is $f$-associated to.

Second, take a *subset* $A' \subset A$ of $A$, and, for *each* $a$ in $A'$, consider its **image** $f[a]$.

Now gather all these images $f[a]$ into a *set*, and call this *set* the **image** of $A' \subset A$ under $f$;
 -->

Notice that \lf
  $\tab\tab1)$ if $f: A \to B$ is a function from $A$ to $B$ and $a \in A$ is an *element* of $A$, then $f[a]$ is an *element* of $B$ \lf
  $\tab\tab2)$ if $f: A \to B$ is a function from $A$ to $B$ and $A' \subset A$ is a *subset* of $A$, then $f_*[A']$ is a *subset* of $B$ \lf
  $\tab\tab3)$ if $f: A \to B$ is a function from $A$ to $B$ and $B' \subset B$ is a *subset* of $B$, then $f^*[B']$ is a *subset* of $A$. \lf

Every function $f: A \to B$ from a set $A$ to a set $B$ gives rise to a pair $(f_*: \Po A \to \Po B, f^*: \Po B \to \Po A)$ of functions: \lf
  $\tab\tab1)$ a function $f_*: \Po A \to \Po B$ from the power set $\Po A$ of $A$ to the power set $\Po B$ of $B$ \lf
  $\tab\tab2)$ a function $f^*: \Po B \to \Po A$ from the power set $\Po B$ of $B$ to the power set $\Po A$ of $A$. \lf

In other words, the function $f_*: \Po A \to \Po B$ maps subsets of $A$ to subsets of $B$, and
the function $f^*: \Po B \to \Po A$ maps subsets of $B$ to subsets of $A$.
The functions $f_*: \Po A \to \Po B$ and $f^*: \Po B \to \Po A$ are closely related to the function $f: A \to B$, and
they *depend* on $f: A \to B$, which is why they have the symbol $f$ in their name.

In this page, we intend to prove that, for any subsets $A',A1,A2 \subset A$ and for any $B',B1,B2 \subset B$, the following hold: \lf
  $\tab\tab1)$ $A' \subset f^*[f_*[A']]$ \lf
  $\tab\tab2)$ $f_*[f^*[B']] \subset B'$ \lf
  $\tab\tab3)$ $f^*: B1 \cup B2 \hskip6pt\mapsto\hskip6pt f^*[B1] \cup f^*[B1]$ \lf
  $\tab\tab4)$ $f^*: B1 \cap B2 \hskip6pt\mapsto\hskip6pt f^*[B1] \cap f^*[B2]$ \lf
  $\tab\tab5)$ $f^*: B \setminus B1 \hskip6pt\mapsto\hskip6pt A \setminus f^*[B1]$ \lf
  $\tab\tab6)$ $B1 \subset B2 \hskip6pt\then\hskip6pt f^*[B1] \subset f^*[B2]$ \lf
  $\tab\tab7)$ $f^*: \{\} \hskip6pt\mapsto\hskip6pt \{\}$ \lf
  $\tab\tab8)$ $f^*: B \hskip6pt\mapsto\hskip6pt A$ \lf

In particular, this means that the preimage function $f^*: \Po B \to \Po A$ is a morphism of the Boolean algebras $\Po B$ and $\Po A$.
(More on this later!)

---------------------------------------------------------------------------------------------------
\section{The image function and the preimage function. Example}

\example Let $A$ be the set $\{0, 1, 2\}$, let $B$ be the set $\{5, 6\}$, let $f: A \to B$ be the function given by \lf
  $\tab\tab$ $f:0 \mapsto 5$ \lf
  $\tab\tab$ $f:1 \mapsto 6$ \lf
  $\tab\tab$ $f:2 \mapsto 5$. \lf
Equivalently, the data for the function $f: A \to B$ could be given using the **graph** of $f: A \to B$,
which is a subset of the Cartesian product $A \times B$.
We can denote the **graph** of the function $f: A \to B$ using the letter $f$, and then specify the **graph** $f$ of the function $f: A \to B$ as \lf
  $\tab\tab$ $f \defined \{(0, 5), (1, 6), (2, 5)\}$. \lf
Notice $f: A \to B$ is indeed a function: it maps *each* element of $A$ to *exactly one* element of $B$. \lf
Now, what do the functions $f_*: \Po A \to \Po B$ and $f^*: \Po A \to \Po B$ look like?
First, let's construct the **powersets** $\Po A$ and $\Po B$. \lf
Since $A$ is the set $\{0, 1, 2\}$, then $\Po A$ is the set $\{\{\}, \{0\}, \{1\}, \{2\}, \{0, 1\}, \{0, 2\}, \{1, 2\}, \{0, 1, 2\}\}$. \lf
Since $B$ is the set $\{5, 6\}$, then $\Po B$ is the set $\{\{\}, \{5\}, \{6\}, \{5, 6\}\}$. \lf
Now, from the data for the function $f: A \to B$, we can derive the data for the **image function** $f_*: \Po A \to \Po B$.
More explicitly, from the data for the function \lf
  $\tab\tab$ $f: \{0, 1, 2\} \to \{5, 6\}$, \lf
we can derive the data for the **image function** \lf
  $\tab\tab$ $f_*: \{\{\}, \{0\}, \{1\}, \{2\}, \{0, 1\}, \{0, 2\}, \{1, 2\}, \{0, 1, 2\}\} \to \{\{\}, \{5\}, \{6\}, \{5, 6\}\}$. \lf
This yields \lf
  $\tab\tab$ $f_*:\{\} \mapsto \{\}$ \lf
  $\tab\tab$ $f_*:\{0\} \mapsto \{5\}$ \lf
  $\tab\tab$ $f_*:\{1\} \mapsto \{6\}$ \lf
  $\tab\tab$ $f_*:\{2\} \mapsto \{5\}$ \lf
  $\tab\tab$ $f_*:\{0, 1\} \mapsto \{5, 6\}$ \lf
  $\tab\tab$ $f_*:\{0, 2\} \mapsto \{5\}$ \lf
  $\tab\tab$ $f_*:\{1, 2\} \mapsto \{5, 6\}$ \lf
  $\tab\tab$ $f_*:\{0, 1, 2\} \mapsto \{5, 6\}$. \lf
And, from the data for the function $f: A \to B$, we can derive the data for the **preimage function** $f^*: \Po B \to \Po A$.
More explicitly, from the data for the function \lf
  $\tab\tab$ $f: \{0, 1, 2\} \to \{5, 6\}$, \lf
we can derive the data for the **preimage function** \lf
  $\tab\tab$ $f^*: \{\{\}, \{5\}, \{6\}, \{5, 6\}\} \to \{\{\}, \{0\}, \{1\}, \{2\}, \{0, 1\}, \{0, 2\}, \{1, 2\}, \{0, 1, 2\}\}$. \lf
This yields \lf
  $\tab\tab$ $f^*:\{\} \mapsto \{\}$ \lf
  $\tab\tab$ $f^*:\{5\} \mapsto \{0, 2\}$ \lf
  $\tab\tab$ $f^*:\{6\} \mapsto \{1\}$ \lf
  $\tab\tab$ $f^*:\{5, 6\} \mapsto \{0, 1, 2\}$. \lf
And we're done. \lf
\qed

Having seen an example, we can look at the definitions.

---------------------------------------------------------------------------------------------------
\section{The image function of a function. Definition}

Every function from a set $A$ to a set $B$ gives rise to a function from the power set of $A$ to the power set of $B$. \lf
That is, every function $f: A \to B$ gives rise to a function $f_*: \Po A \to \Po B$. \lf
That is, if $f: A \to B$ maps elements of $A$ to elements of $B$, then $f_*: \Po A \to \Po B$ maps subsets of $A$ to subsets of $B$. \lf
The function $f_*: \Po A \to \Po B$ is not too special, and it doesn't have too many properties.
We call $f_*$ the **image function** of $f$, or the **covariant subset function** of $f$.

\definition Let $f: A \to B$ be a function between sets, let $A' \subset A$ be a subset of $A$. \lf
The **image of $A'$ under $f$**, denoted $f_*[A']$, is the set of all elements of the form $f[a]$ as $a$ ranges over $A'$. \lf
Equivalently, $f_*[A']$ is the set of all elements of $B$ that are the image of *at least one* element of $A'$. \lf
In symbols, the **image** $f_*[A']$ of $A'$ under $f$ can be defined in any of the following equivalent ways: \lf
  $\tab\tab1)$ $f_*[A'] \defined \{f[a] \in B \pipe a \in A'\}$ \lf
  $\tab\tab2)$ $f_*[A'] \defined \{b \in B \pipe \exists a \in A' \hskip4pt \langle f[a] = b \rangle\}$ \lf

Even though these two definitions yield the same set, they have different "flavors".
You can think about them in terms of how an "algorithm" would "compute" the image $f_*[A']$ of $A'$ under $f$ using each definition.

An algorithm to compute the image $f_*[A']$ of $A'$ under $f$ using definition $1)$ would do the following.
Loop through each element $a$ of $A'$, apply $f$ to each element $a$ of $A'$, and gather *all* the results inside a set;
this set is your desired image $f[A']$.

An algorithm to compute the image $f_*[A']$ of $A'$ under $f$ using definition $2)$ would do the following.
Loop through each element $b$ of $B$ and, for *each* element $b$ of $B$,
it would loop through *all* elements $a$ of $A'$ and apply $f$ to $a$
until the image $f[a]$ of $a$ lands in $b$ (in which case it stores this $b$ somewhere safe) or
until it has traversed through all of $A'$ and $f[a]$ never lands in $b$ (in which case it discards this $b$).
The set of all $b$'s that the algorithm didn't discard in the desired image $f[A']$.

Using the definition of the image $f_*[A']$

Notice that $f: A \to B$ and $f_*: \Po A \to \Po B$ can't be the same function because they don't have the same domain or the same codomain.
In the literature people drop the notational distinction between $f: A \to B$ and $f_*: \Po A \to \Po B$,
calling them both $f$.

<!-- The **image function** $f_*$ of the function $f$ is not as well behaved as her sister,
the **preimage function** $f^*$ of the function $f$.
The image function $f_*$ is a morphism of **upper-semilattices**, but the preimage function $f^*$ satisfies a stronger property:
$f^*$ is a morphism of **Boolean algebras**.
 -->

---------------------------------------------------------------------------------------------------
\section{The preimage function of a function. Definition}

Every function from a set $A$ to a set $B$ gives rise to a function from the power set of $B$ to the power set of $A$. \lf
That is, every function $f: A \to B$ gives rise to a function $f^*: \Po B \to \Po A$. \lf
That is, if $f: A \to B$ maps elements of $A$ to elements of $B$, then $f^*: \Po B \to \Po A$ maps subsets of $B$ to subsets of $A$. \lf
The function $f^*: \Po B \to \Po A$ is very special, and it has very nice properties.
We call $f^*$ the **contravariant subset function** of $f$, or the **preimage function** of $f$.

\definition Let $f: A \to B$ be a function between sets, let $B' \subset B$ be a subset of $B$. \lf
The **preimage of $B'$ under $f$**, denoted $f^*[B']$, is the set of all $a$ in $A$ whose image $f[a]$ is in $B'$. \lf
Equivalently, $f_*[B']$ is the set of all elements of $A$ whose image is *at least one* element of $B'$. \lf
In symbols, the **preimage** $f^*[B']$ of $B'$ under $f$ can be defined in any of the following equivalent ways: \lf
  $\tab\tab1)$ $f^*[B'] \defined \{a \in A \pipe f[a] \in B'\}$ \lf
  $\tab\tab2)$ $f^*[B'] \defined \{a \in A \pipe \exists b \in B' \hskip4pt \langle f[a] = b \rangle\}$ \lf

Even though these two definitions yield the same set, they have different "flavors".

<!-- We list some of the properties of $f^*$ here. Then, we'll explain them and prove them. \lf
  $\tab\tab1)$ Let $f: A \to B$, let $B1$ and $B2$ be subsets of $B$. Now $f^*$ maps $B1 \cup B2$ (which is a subset of $B$) to $f^*[B1] \cup f^*[B2]$ (which is a subset of $A$). \lf
  $\tab\tab2)$ Let $f: A \to B$, let $B1$ and $B2$ be subsets of $B$. Now $f^*$ maps $B1 \cap B2$ (which is a subset of $B$) to $f^*[B1] \cap f^*[B2]$ (which is a subset of $A$). \lf
  $\tab\tab3)$ Let $f: A \to B$, let $B'$ be a subset of $B$. Now $f^*$ maps $B \setminus B'$ to $A \setminus f^*[B']$. \lf
  $\tab\tab4)$ Let $f: A \to B$, let $B1$ and $B2$ be subsets of $B$. Now $B1 \subset B2$ implies $f^*[B1] \subset f^*[B2]$. \lf
  $\tab\tab5)$ Let $f: A \to B$. Now $f^*$ maps $\{\}$ (which is a subset of $B$)  to $\{\}$ (which is a subset of $A$). \lf
  $\tab\tab6)$ Let $f: A \to B$. Now $f^*$ maps $B$ (which is a subset of $B$) to $A$ (which is a subset of $A$). \lf

In other words, we prove that the function $f^*: \Po B \to \Po A$ is a
[**morphism**][https://en.wikipedia.org/wiki/Morphism]
of [**Boolean algebras**][https://en.wikipedia.org/wiki/Boolean_algebra_(structure)#Homomorphisms_and_isomorphisms].
 -->

<!-- Notice $f^{-1}$ and $f^*$ aren't the same function because they don't have the same domain or the same codomain.
In fact, if $f$ is a function, then $f^*$ always exists, while $f^{-1}$ exists only rarely!
In the literature people drop the notational distinction between $f^{-1}$ and $f^*$,
calling them both $f^{-1}$. -->

---------------------------------------------------------------------------------------------------
\section{The domain is a subset of the preimage of the image}

\theorem Let $f: A \to B$ be a function from set $A$ to set $B$, let $A' \subset A$ be a subset of $A$. Now \lf
  $\tab\tab1)$ $A'$ is a subset of the preimage of the image of $A'$ \lf
  $\tab\tab2)$ $A'$ is a subset of the preimage (under $f$) of the image (under $f$) of $A'$ \lf
  $\tab\tab3)$ $A'$ is a subset of $f^* \compose f_*[A']$ \lf
  $\tab\tab4)$ $A' \subset f^* \compose f_*[A']$ \lf
  $\tab\tab5)$ $A' \subset f^*[f_*[A']]$ \lf
  $\tab\tab6)$ for every $a$ in $A'$, $a$ is in $f^*[f_*[A']]$ \lf
  $\tab\tab7)$ $\forall a \in A' \hskip4pt \langle\hskip4pt a \in f^*[f_*[A']] \hskip4pt\rangle$ \lf
  $\tab\tab8)$ for every $a$, if $a$ is in $A'$, then $a$ is in $f^*[f_*[A']]$ \lf
  $\tab\tab9)$ $\forall a \hskip4pt \langle\hskip4pt a \in A' \then a \in f^*[f_*[A']] \hskip4pt\rangle$ \lf

\proof TODO
<!-- \proof Statements $1)$ through $9)$ are all the same statement written in different (but equivalent) ways. -->

---------------------------------------------------------------------------------------------------
\section{The image of the preimage is a subset of the codomain}

\theorem Let $f: A \to B$ be a function from set $A$ to set $B$, let $B' \subset B$ be a subset of $B$. Now \lf
  $\tab\tab1)$ the image of the preimage of $B'$ is a subset of $B'$ \lf
  $\tab\tab2)$ the image (under $f$) of the preimage (under $f$) of $B'$ is a subset of $B'$ \lf
  $\tab\tab3)$ $f_* \compose f^*[B']$ is a subset of $B'$ \lf
  $\tab\tab4)$ $f_* \compose f^*[B'] \subset B'$ \lf
  $\tab\tab5)$ $f_*[f^*[B']] \subset B'$ \lf
  $\tab\tab6)$ for every $b$ in $f_*[f^*[B']]$, $b$ is in $B'$ \lf
  $\tab\tab7)$ $\forall b \in f_*[f^*[B']] \hskip4pt \langle\hskip4pt b \in B' \hskip4pt\rangle$ \lf
  $\tab\tab8)$ for every $b$, if $b$ is in $f_*[f^*[B']]$, then $b$ is in $B'$ \lf
  $\tab\tab9)$ $\forall b \hskip4pt \langle\hskip4pt b \in f_*[f^*[B']] \then b \in B' \hskip4pt\rangle$ \lf

\proof Statements $1)$ through $9)$ are all the same statement written in different (but equivalent) ways.
We want to prove that \lf

  $$f_*[f^*[B']] \subset B'.$$

To do this, take an arbitrary element $b \in f_*[f^*[B']]$. We don't know much about the element $b$, except that it belongs to $f_*[f^*[B']]$. \lf
From the definition of $f_*: \Po A \to \Po B$, we can immediately deduce that *there exists* an element $a \in f^*[B']$ that *goes to* $b$ (under $f$),
meaning $f: a \mapsto b$. \lf
That is, the very definition of $f_*: \Po A \to \Po B$ guarantees the *existence* of a particular element $a \in f^*[B']$ whose image $f[a]$ under $f$ is $b$
(remember that $b \in f_*[f^*[B']]$ is the original element we started with).

This element $a \in f^*[B']$ will be the key to everything. \lf
One thing to notice about $a \in f^*[B']$ is that it's *not* arbitrary.
I mean, the element $b \in f_*[f^*[B']]$ *is* arbitrary, but, after we "lock in" our choice of $b \in f_*[f^*[B']]$,
we find that our realm of possibilities for $a$ is *not* arbitrary. That is, this element $a \in f^*[B']$,
whose existence is guaranteed by the very definition of $f_*: \Po A \to \Po B$, *depends* the specific $b \in f_*[f^*[B']]$ that we take. \lf
Another thing to notice about $a \in f^*[B']$ is that it *need not be unique*!
The hypothesis that $f$ is a **function** is perfectly fine with this fact:
indeed, there can exist *multiple* elements of $f^*[B']$ whose image (under $f$) is $b$.
The important thing is that we're guaranteed the **existence** of *at least one*.

So, to recap. \lf
Assume $b$ is in $f_*[f^*[B']]$. \lf
It follows that there exists *at least one* element $a$ of $f^*[B']$ whose image $f[a]$ is $b$, meaning $f: a \mapsto b$.

Now let's look at the definition of $f^*[B']$. What does it mean to be an element of $f^*[B']$?
What does it mean that $a$ is an element of $f^*[B']$?
What membership criteria must $a$ fulfill in order to be an element of $f^*[B']$?
Given the knowledge that $a$ is in $f^*[B']$, what can we deduce about $a$? What can we deduce about $f[a]$? \lf
One crucial thing the membership of $a$ to $f^*[B']$ allows us to deduce is the existence of *some* element of $B'$ that $a$ *goes to* (under $f$).
This element is important, so let's give it a name: call it $b'$. So, $b'$ is an element of $B'$. \lf
Let's state this again. Given the fact that $a$ is in $f^*[B']$, we're guaranteed the existence of an element $b'$ in $B'$ that $a$ *goes to* (under $f$),
meaning $f: a \mapsto b'$.

Now we stop, and look back. \lf
We started with the hypothesis that $b$ is in $f_*[f^*[B']]$. \lf
Then, we deduced the existence of an element $a \in A$ with the property that $f: a \mapsto b$. \lf
And now we've deduced the existence of an element $b' \in B'$ with the property that $f: a \mapsto b'$. \lf
So we simultaneously have that $f: a \mapsto b$ and that $f: a \mapsto b'$. \lf
What does this mean? Can we deduce anything from this? The really important question is: are $b$ and $b'$ **distinct** elements,
or are they secretly the same element written in two different (but equivalent) ways?

The hypothesis that $f: A \to B$ is a *function* contradicts the possibility that $b$ and $b'$ are *distinct*.
We can't have that $f: A \to B$ is a function *and* also that $b$ and $b'$ are distinct.
If we assume that $b$ and $b'$ are distinct, then $f: A \to B$ is not a function.
But, if we do insist that $f: A \to B$ is a function (and we do; this is one of our hypotheses),
then we must necessarily arrive at the conclusion that $b$ is equal to $b'$, meaning $b = b'$.
And recall that $b'$ is in $B'$. Since $b'$ was actually $b$ all along, it follows that $b$ is in $B'$. \lf

So, we started with the hypothesis that $b$ is in $f_*[f^*[B']]$, and we've arrived at the conclusion that $b$ is in $B'$.
This argument proves that, if $b$ is in $f_*[f^*[B']]$, then $b$ is in $B'$, which, by definition, means that $f_*[f^*[B']]$ is a subset of $B'$,
meaning $f_*[f^*[B']] \subset B'$, which is our goal. \lf

But there's one subtlety left. What if $f_*[f^*[B']]$ is the empty set $\{\}$? That is, what if $f_*[f^*[B']]$ has *no* elements?
Then we couldn't possibly have that $b$ is in $f_*[f^*[B']]$ to start with.
In this case, the statement that $b$ is in $f_*[f^*[B']]$ is a **false statement**, and so the **implication**
"if $b$ is in $f_*[f^*[B']]$, then $b$ is in $B'$" is (vacuously) **true**, by the definition of
[**implication**][https://en.wikipedia.org/wiki/Material_conditional]. \lf
\qed

A proof of $f_*[f^*[B']] \subset B'$ that outlines the steps, but doesn't explain any of the reasoning, goes as follows.

\proof Let $b \in f_*[f^*[B']]$.
Then there exists $a \in f^*[B']$ such that $f[a] = b$.
Since $a \in f^*[B']$, then $f[a] \in B'$.
It follows that $b \in B'$. \lf
\qed

---------------------------------------------------------------------------------------------------
<!-- \section{The image function is a morphism of upper-semilattices} -->

---------------------------------------------------------------------------------------------------
\section{The preimage function is a morphism of Boolean algebras}

\theorem Let $f: A \to B$ be a map from set $A$ to set $B$. \lf
Now the **preimage function** $f^*: \Po B \to \Po A$ induced by map $f$ is a morphism of Boolean algebras. \lf
In symbols, the **preimage function** $f^*: \Po B \to \Po A$ satisfies the following, *for all* subsets $B1,B2 \subset B$: \lf
  $\tab\tab1)$ $f^*: B1 \cup B2 \hskip6pt\mapsto\hskip6pt f^*[B1] \cup f^*[B1]$ \lf
  $\tab\tab2)$ $f^*: B1 \cap B2 \hskip6pt\mapsto\hskip6pt f^*[B1] \cap f^*[B2]$ \lf
  $\tab\tab3)$ $f^*: B \setminus B1 \hskip6pt\mapsto\hskip6pt A \setminus f^*[B1]$ \lf
  $\tab\tab4)$ $B1 \subset B2 \hskip6pt\then\hskip6pt f^*[B1] \subset f^*[B2]$ \lf
  $\tab\tab5)$ $f^*: \{\} \hskip6pt\mapsto\hskip6pt \{\}$ \lf
  $\tab\tab6)$ $f^*: B \hskip6pt\mapsto\hskip6pt A$ \lf

\proof To prove that $f^*: \Po B \to \Po A$ is a morphism of Boolean algebras, we must prove that,
in passing from the Boolean algebra $\Po B$ to the Boolean algebra $\Po A$, the map $f^*$ preserves the Boolean algebra structure.
The Boolean algebra structure has four components: unions, intersections, complements, inclusions, the least element, and the greatest element.
So, we must prove that \lf
  $\tab\tab1)$ $f^*: \Po B \to \Po A$ preserves unions \lf
  $\tab\tab2)$ $f^*: \Po B \to \Po A$ preserves intersections \lf
  $\tab\tab3)$ $f^*: \Po B \to \Po A$ preserves complements \lf
  $\tab\tab4)$ $f^*: \Po B \to \Po A$ preserves inclusions \lf
  $\tab\tab5)$ $f^*: \Po B \to \Po A$ preserves the least element \lf
  $\tab\tab6)$ $f^*: \Po B \to \Po A$ preserves the greatest element. \lf

To prove $1)$, let $B1$ and $B2$ be subsets of $B$.

To prove $2)$, let $B1$ and $B2$ be subsets of $B$.

To prove $5)$, recall that the Boolean-least element of $\Po B$ is the empty set $\{\}$ and the Boolean-least element of $\Po A$ is the empty set $\{\}$.
Now, what is the image of $\{\}$ under $f^*$? That is, what is the preimage $f^*[\{\}]$ of the empty set under the map $f$?
Well, recall the definition of preimage.
If $B1$ is a subset of $B$, then $f^*[B1]$ is defined as the set of all elements of $A$ that are mapped to an element of $B1$. This means

$$f^*[B1] \defined \{a \in A \pipe f[a] \in B1\}.$$

Now, the empty set $\{\}$ is a subset of $B$, so $f^*[\{\}]$ is defined as
the set of all elements of $A$ that are mapped to an element of the empty set $\{\}$. This means

$$f^*[\{\}] \defined \{a \in A \pipe f[a] \in \{\}\}.$$

But there's something very wrong with the expression: $f[a] \in \{\}$.
Namely, $f[a]$ can't be an element of $\{\}$ because $\{\}$ *has no elements*.
So, there can't be any element of $A$ that gets mapped (by $f$) an element of $\{\}$.
This means that the set of all such elements is also empty.
This shows that the *preimage* (under $f$) of the empty set is also empty,
meaning that the *image* (under $f^*$) of the empty set is the empty set,
meaning that $f^*[\{\}]$ is $\{\}$.
And this is the desired result: the preimage function $f^*$ maps to Boolean-least element of $\Po B$ to the Boolean-least element of $\Po A$.

To prove $6)$, let $B1$ and $B2$ be subsets of $B$.

---------------------------------------------------------------------------------------------------
<!-- \section{There's a unique function from the empty set to an arbitrary set} -->

---------------------------------------------------------------------------------------------------
<!-- \section{There's a unique function from an arbitrary set to the singleton set} -->

---------------------------------------------------------------------------------------------------
<!-- \section{Injections, surjections, and bijections}

A function that can be "*undone from the left*" is called an **injection**. \lf
A function that can be "*undone from the right*" is called a **surjection**. \lf
A function that can be undone both "*from the left*" and "*from the right*" is called a **bijection**. \lf
Bijections are the **isomorphisms** of sets, meaning they allow us to consider different sets to be "alike",
even though they're not *absolutely* the same.
Isomorphisms are like "perfect transformations": they don't destroy structure, they can be undone at will.
If two objects are isomorphic, you know they have a lot in common, even though they may not be *absolutely* the same
(whatever "*absolutely the same*" means). -->
