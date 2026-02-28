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