NEXT STEP
1o:
Still have unnafected Kx a1oc if x < |fo|
    Because the Kx where I pick one from every first order line is unnafected. If I picked
    a next vertex it would be two from one first order pair, so that clique would be affected

2o:
Still have unnafected Kx a2oc if x < |fo|
    The Kx where I pick only odd vertices from each necessary first order pair (up to x) is unnafected

3o:
if v % 8 == 0:
    Still have unnafected Kx a3oc if x < (3/2) * |4o|            first actual change
        #Even 4o vertices then odd for the first half of 4o pairs
else:
    Still have unnafected Kx a3oc if x < 2*|4o| = |fo|
        Any Kx containing only vertices in 4o is unnafected


There was only the further specification after v%8 for 4o because that's when picking two of them could
    have violated an earlier order


4o:
If v % 8 == 0:
    Still have unnafected Kx a4oc if x < (3/2) * |5o|           *Note this doesn't cut down any more
        Pick all evens in fifth order, then odds up to half
    Still have unnafected Kx a4oc if x < 2 * |5o| = |1o|
        Any Kx containing only vertices in 5o is unnafected




PERSPECTIVE SHIFT
    I don't need to be calculating how many unnafected cliques there are post each coloring, I only
    need to be checking if there are any unnafected or fully contained cliques

    There are still unnafected if I can find 

For v=16, x=9 (there are no unnafected after third order coloring) :
First Order = [(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15)]
#Second Order = [(0,2),(4,6),(8,10),(12,14)]
#Third Order = [(1,9),(3,11),(5,13),(7,15)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15)]

WHEN WILL THE FOURTH ORDER LINES CONTAIN A THIRD ORDER LINE?
v=16
#Third Order = [(1,9),(3,11),(5,13),(7,15)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15)]
v=20
#Third Order = [(1,11),(3,13),(5,15),(7,17),(9,19)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15),(16,19)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14),(17,18)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15),(17,19)]
v=24
#Third Order = [(1,13),(3,15),(5,17),(7,19),(9,21)(11,23)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15),(16,19),(20,23)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14),(17,18),(21,22)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15),(17,19),(21,23)]
v=28
#Third Order = [(1,15),(3,17),(5,19),(7,21),(9,23)(11,25),(13,27)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15),(16,19),(20,23),(24,27)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14),(17,18),(21,22),(25,26)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15),(17,19),(21,23),(25,27)]
v=32
#Third Order = [(1,17),(3,19),(5,21),(7,23),(9,25)(11,27),(13,29),(15,31)]
#Fourth Order = [(0,3),(4,7),(8,11),(12,15),(16,19),(20,23),(24,27),(28,31)]
#Fifth Order = [(1,2),(5,6),(9,10),(13,14),(17,18),(21,22),(25,26),(29,30)]
#Sixth Order = [(1,3),(5,7),(9,11),(13,15),(17,19),(21,23),(25,27),(29,31)]


I will have third order unnafected cliques if I can choose every fourth order even vertex, then
every odd vertex that doesn't break the third order (for v=24 I will have unnafected cliques up to
x=8 because I'll have the unnafected clique (0,4,8,12,16,20,3,7,11) but any next vertex will have a blue line in the K9)



If there are odd vertices in 4o that match up to odds in 3o (v=24, not v=20)
Unnafected if x < fo 
(the clique containing all points in 4o (or less) is unnafected)


So there are still unnafected cliques after 3o if
x < |4o| 







The patterns foor checking unnafected are going to be to check the next order
NEW CONJECTURE :
    If two fourth order odd numbers are a blue line in the third order, you will not have
no unnafected lines in your Kx after third order coloring
    (Also this should be calculable just off fo)
This is because fourth order lines are the ones st


There are unnafected for v=8 because :
    O O E O
    1 2 5 6 9 10 13 14

TO CHECK IF THERE ARE STILL UNNAFECTED Kxy AFTER NEXT ORDER COLORING
Think in terms of fo_l from left to right



There are no unnafected for v=9 because fo=8 and once I pick one from each fo I'm forced
    to pick one more (trivial)


At third coloring there's a symmetry again. I can pick one path starting with 0 or 1 and if
    it doesn't work nothing will.

0, 3, 4, 7, 8, 11, 12, 14

The rule for each entry n is :
n % 4 == 0 :
    Disallow n+2
n odd :
    n < fo :
        Disallow n+fo
    n > fo :
        Disallow n-fo (If even necessary because process is left to right)

Conjecture:
The only way to fail is for the pattern outlined in the numbers above to fail on an odd entry
(Incorrect - paths diverge at 4)





NEW IDEA
Only look at the orders, not the affected Kv after them
Thinking about allowed red Kx and blue Ky, so a monochromatic coloring contains a blue Kx or red Ky
Think of the whole object as starting red, each line in an order being blue
Ky then needs to have only cliques including a line in any order, with no Kx being fully colored by the ordered lines
or Ky will have a fully blue clique with no Kx being fully colored

That is :
There is a non-monochromatic coloring of v for (x,y) :
    There is no Kx fully contained in ordered lines
    Every Ky clique contains at least one ordered line (no unnafected Ky)
v is at or past R(x,y) :
    There is a Kx fully contained in ordered lines
    There is at least one Ky not containing an ordered line (1+ unnafected Ky)

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



#First Order = [(0,1),(2,3),(4,5),(6,7),(8,9),(10,11)] 
#Second Order = [(0,2),(4,6),(8,10)] 
#Third Order = [(1,7),(3,9),(5,11)] 
#Fourth Order = [(0,3),(4,7),(8,11)] 
#Fifth Order = [(1,2),(5,6),(9,10)] 
#Sixth Order = [(1,3),(5,7),(9,11)]


At third order, I'm looking at 
b1 = [(0,2),(4,6),(8,10)]
b2 = [(1,7),(3,9),(5,11)]
(1,3), (5,7), (9,11) knock out a full pair in b1. The rest of the ways you can choose b2 knock out 1
from each vertex chosen



At fourth order I have:
b1 = [(0,2,3),(4,6,7),(8,10,11)]
Leftover = 1,5,9
1 knocks out 0,7
5 knocks out 4,11
9 knocks out 3,8
So each "safe vertex" combines with 2**2 * 3 * bCi
b2 = [(1,)]


#Fourth Order = [(0,3),(4,7),(8,11),(12,15)] 
#Fifth Order = [(1,2),(5,6),(9,10),(13,14)] 
#Sixth Order = [(1,3),(5,7),(9,11),(13,15)]

#First Order = [(0,1),(2,3),(4,5),(6,7),(8,9),(10,11),(12,13),(14,15)] 
#Second Order = [(0,2),(4,6),(8,10),(12,14)] 
#Third Order = [(1,9),(3,11),(5,13)(7,15)] 

At third order you have
b1 = [(0,2),(4,6),(8,10),(12,14)]
b2 = [(1,9),(3,11),(5,13),(7,15)]
(1,3), (5,7), (9,11), (13,15) knock out a full pair from b1. The rest of the ways you can choose b2 knock out
1 per chosen vertex

Fix '1' with x=4:
i=0:
    b1 = [(0,2),(4,6),(8,10),(12,14)]
    ret += 2**4 * 4C4
i=1:
    b1 = [(2),(4,6),(8,10),(12,14)]
    ret += 2**3 * 4C3
i=2:
    Pick 3 from (3,11)
        b1 = [(4,6),(8,10),(12,14)]
        ret += 2**3 * 3C2
    Pick 11 from (3,11), or one from a different 3o
        b1 = [(2),(4,6),(8)(12,14)]
        ret += 2**2 * 4C2
i=3:
    Pick 3 from (3,11) and any remaining option in 3o ; or (5,7) or (13,15) [pictured is choice 3,5]
        b1 = [(6),(8,10),(12,14)]
        ret += 
    Pick 11 from 3,11 ; or two choices from the remaining 3o except (5,7) or (13,15). [pictured is 5,11]
        b1 = [(2),(6),(8),(12,14)]
i=4:
    Pick 3 from (3,11)
        Take (5,7) [could be (13,15)]
            b1 = [(8,10),(12,14)]
        Take 5,15 [or 7,13]
            b1 = [(6),(8,10),(12)]
    Pick 11 from (3,11)
        Take (5,7) [could be (13,15)]
            b1 = [(2),(8),(12,14)]
        Take 5,15 [or 7,13]
            b1 = [(2),(6),(8),(12)]
        





At fourth order I have:
b1 = [(0,2,3),(4,6,7),(8,10,11)]
Leftover = 1,5,9
1 knocks out 0,7
5 knocks out 4,11
9 knocks out 3,8
So each "safe vertex" combines with 2**2 * 3 * bCi


With i as the number of b2 I'm choosing :
    for i=0,1
        No special lines
    for i=2,3
        Fix one, forces one
    for i=4,5
        Fix two, forces two

Fix '1' :
    Have 1,3 fixed
    The remaining b2 portion is choose 1 from [(5,13),(7,15)]
        b1 = b1 - 1 - i
    Have 1,9 fixed
    The remaining b2 portion is the same as above
        b1 = bi - i * 2**??
Then I can further fix the 5??






Ways to choose b2 = 2**|b2| * b2C








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








