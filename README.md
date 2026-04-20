A small Python project for computing combinatorial simplex metrics of complete graphs in the context of Ramsey theory.

This program computes clique counts and participation metrics using closed-form combinatorial formulas and stores the results in a SQLite database for further exploration.


This project has been temporarily abandoned, because symmetries in connected graphs that would make formulaic calculations possible were not present.

The goal was to think about K(x,y) in a v-connected graph such that fully red x-cliques and fully blue y-cliques were "illegal", and to start with a fully red v-connected graph.

Then to define orders as such (Shown with v = 8):
  First Order : Alternating perimeter edges
    [(0,1),(2,3),(4,5),(6,7)]
  Second Order : Even pairs
    [(0,2),(4,6)]
  Third Order : Odd pairs, such that the pairs don't overlap through their even first order counterparts. I.E. not (1,3)
    The way to make this systematic was to take one an odd vertex from the first half of the first order, then add it to the corresponding odd vertex from the second half
      [(1,5),(3,7)]
  Fourth Order : Pairs an even vertex with its odd first-order neighbor
    [(0,3),(4,7)]
  Fifth Order : Pairs an odd vertex with its even first-order neighbor
    [(1,2),(5,6)]
  Sixth Order : Pairs an odd vertex with its odd first-order neighbor
    [(1,3),(5,7)]

Then, order by order, to color each included line blue and calculate how many x-cliques were still illegal because they didn't include any lines contained in any of the previously colored orders, as well as how many blue lines the most blue y-clique(s) contained. The idea was, if I could clear up illegal x-cliques in this manner without causing a fully blue y-clique, I would know that I'd found a legal coloring, and the Ramsey number for x,y would be higher than v. And if I could define orders as such that these colorings caused the minimal number of blue lines, I would know that v >= R(x,y).


It should be noted that if v=9, there would be an extra vertex not touched in the first order. If v=10, first order would be odd, and if v=11 first order would be odd with an extra vertex. In an attempt to force symmetries, I only looked at cases where v is divisible by 4.

If v=12, the second and third orders will be odd, causing discrepencies in the later orders. We can examine only v divisible by 8 to resolve this.

Both of these were resolvable in restricting v, but when I started to check fourth order colorings, I noticed that the edges it contained were not "symmetric to each other", meaning that they contributed to different numbers of x-cliques getting their first blue line and y-cliques getting another. This was an unresolvable symmetry break, and I don't see how to define the orders in a way that it doesn't happen.
