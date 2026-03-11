
NEW IDEA
Only look at the orders, not the affected Kv after them
Thinking about allowed red Kx and blue Ky, so a monochromatic coloring contains a blue Kx or red Ky
Think of the whole object as starting red, each line in an order being blue
Ky then needs to have only cliques including a line in any order, with no Kx being fully colored by the ordered lines
or Ky will have a fully blue clique with no Kx being fully colored

That is :
There is a non-monochromatic coloring of v for (x,y) :
    There is no Kx fully contained in ordered lines
    Every Ky clique contains at least one ordered line
v is at or past R(x,y) :
    There is a Kx fully contained in ordered lines
    There is at least one Ky not containing an ordered line

So for R(3,4) [which is 9] :
v=8 :
1o = [(0,1),(2,3),(4,5),(6,7)]
2o = [(0,2),(4,6)]
3o = [(1,5),(3,7)]
4o = [(0,)]

The "least" characteristic for picking the next line is contained in the smallest amount of affected cliques

Does every K4 contain one ordered line?
    K4 without an ordered line:
        1,2,4,7












New Flow :
Define orders by:
First order is no shared vertices throughout [(0,1),(2,3),...]
Order 1.5 is the untouched vertex, if there, with the last to-be-paired (in second) even vertex
Second order is a vertex from two seperate first order lines. Could be any, pick evens.
Order 2.5 is :
    C1: 

Now I'm caught up with the four cases:
CASE 0: Even v, fo :
1o: [(0,1),(2,3),...]
2o: [(0,2),(4,6),...]
3o: [(1,5),(3,7),...]  #stagger them so you're picking third order lines from first order ones not already linked by second order
4o: [(0,)]

I can just do the computations on vertexes where this is the case and theoretically get a bound within four
I need to color each order and check at what point I have either one fully changed Ky, or every Ky with at least one affected line
If every Ky clique has at least one affected line and there are no fully changed Kx then I've found a legal coloring, the Ramsey number is higher


CASE 1: Even v, odd fo :
fo: [(0,1),(2,3),...]
so: [(0,2),(4,6),...]
Not in so:
v-2

CASE 2: Odd v, even fo :
fo: [(0,1),(2,3),...]  u_v=v-1
1.5 [(v-5,v-1)]
so: [(0,2),(4,6),...]
Not in fo:
v-1
Not in so:
v-3


CASE 3: Odd v,fo :
fo: [(0,1),(2,3),...]  u_v
1.5 [(v-1,u_v)]  *last fo_l represented in "so" with the u_v
so: [(0,2),(4,6),...]
Not in fo:
v-1





NOTES FOR one blue line a20c
Formula = summation from i to min(k,b) of      bCi * 2^i * sC[k-i]

v=15
fo_lines = [ (0,1), (2,3), (4,5) (6,7) (8,9), (10,11), (12,13) ]    untouched_v = 14
so_lines = [ (0,2), (4,6), (8,10), (12,14) ]
Picked line = (0,1)
exclude 2 completely ((0,1,2,..) have two+ blue lines)
safe vertices = [ 3,5,7,9,11,13 ]
unsafe blocks = [ (4,6), (8,10), (12,14) ]
    b = 3 = # unsafe blocks,     k = x-2 (x=7),     s = 6 = # safe vertices,     i = number of unsafe blocks chosen for that particular K7
    Summation from 0 to min(b,x-2)=3
                                                3Ci * 2^i * (6C[5-i])
        i=0:  3C0 * 1 * 6     This is the number of K7 with one blue line and all safe lines
        i=1:  3C1 * 2 * 15 = 90

First I'm picking a fo_l, (0,1).
Next I'm picking 

        It's 6 C (5-i)     It's 6 choose 5 for i=0 because you're picking 5 safe vertices



If I fixed (0,1 and (2,3) I wouldn't need to consider 4. Thus unsafe blocks would become 
Safe vertices = [ 5,7,9,11,13 ]
Unsafe blocks = [ (8,10), (12,14) ]
But I can't have 6 and 7 both in the safe vertices. Thus this becomes
Safe vertices = [ 5,9,11,13 ]
Unsafe blocks = [ (6,7), (8,10), (12,14)]


fo=7 vOdd=1
For v=15, x=7
One blue line, fix (0,1):
    Safe vertices = [ 3,5,7,9,11,13 ]
    Unsafe blocks = [ (4,6), (8,10), (12,14)]
Two blue lines, fix (0,1), (2,3):
    Safe vertices = [ 5,9,11,13 ]
    Unsafe blocks = [ (6,7), (8,10), (12,14)]
Three blue lines, fix (0,1), (2,3), (4,5)
    Safe vertices = [ 7,9,11,13 ]
    Unsafe blocks = [ (8,10), (12,14) ]
Four blue lines, fix (0,1), (2,3), (4,5), (6,7)
    Safe vertices = [9,13]
    Unsafe blocks = [ (10,11), (12,14) ]



fo=7 vOdd=1
For one blue line:
    s=6, b=3
For two blue lines:
    s=4, b=3
For three blue lines:
    s=4, b=2
For four blue lines:
    s=1, b=2



For v=15
First Order Lines = [(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13)] u_v=14
Second Order Lines = [(0,2),(4,6),(8,10),(12,14)]

For a fixed (0,1), with k = x-2:
    Safe vertices (no blue with 0,1 or each other) = 
        [3,5,7,9,11,13]                               cardinality is s
    Unsafe boxes (should all add one more blue line)=
        [(4,6),(8,10),(12,14)]                        cardinality is b
    I can get all Kx with a single blue line as
        summation i from 0 to b (s-iCk-i + bCi)
    
For all Kx with two blue lines you have
    (0,1,2,x,y) for x,y in safe, x,y >= 5 (excludes 3), or x is in 1 unsafe box (remove corresponding
        from safe, ie pick 4 remove 5 from s pick 6 remove 7)
    (0,1,[unsafe box],x) where x is 
        summation i from 0 to b-1 (s-2-iCk-2-i + b-1Ci)
    (0,1,fo_l,x) where fo_l is (4,5) or later
        For (0,1,4,5,x,y) relevant safe = [3,7,9,11,13]
                        relevant unsafe = [(8,10),(12,14)] =
        summation i from 0 to b-1(s-1-iC2-i + b-1Ci)




Boxes are fully blue cliques after second order coloring
WON'T WORK BECAUSE 
    Doesn't include the blues between say 3,4
Second Order Boxes for Calculations =
    [(0,1,2,3),(4,5,6,7),(8,9,10,11),(12,13,14)]
    For [(0,1,2,3)] :
        Blue : (0,1), (0,2), (2,3)
        Red : (0,3), (1,3), (1,2)
    For [(4,5,6,7)] :
        Blue : (4,5), (4,6)
        Red : 
    For [(12,13,14)]
        Blue : (12,13), (12,14)
        Red : (11,12), (11,13), (11,14), 













    def num_K_with_one_blue_line_a2oc(fo, xy, vOdd):
    #fo = line(fo_lines), vOdd = 1 if v is odd 0 if even
    ret = 0
    s = fo - 1 + vOdd     #Number of safe vertices. One per fo_l except for chosen fo_l, extra vertex if present
    b = floor((fo+vOdd) / 2)     #The number of unsaf blocks
    k = xy - 2     #These are Kxy. I fixed the first two so I need to fill the rest of the xy spaces
    for i in range(min(b,k)+1):
        ret += (nCk(b,i) * 2**i * nCk(s,k-i))
    ret *= fo
    return ret








