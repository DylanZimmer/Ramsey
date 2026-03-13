from math import factorial

def nCk(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    numer_start = max(n-k, k)
    denom_fac = min(n-k, k)
    numerator = 1
    for i in range(numer_start+1, n+1):
        numerator *= i
    denominator = factorial(denom_fac)
    return numerator // denominator

def calc(top, k, s, b, multiplier=1):
    ret = 0
    for i in range(top+1):
        ret += nCk(s-i, k-i) * 2**i * nCk(b, i)
    ret *= multiplier
    return ret

def calc2(top, k, b1, b2):  #This is for third order (and probably beyond), two lines of unsafe boxes
    ret = 0
    for i in range(top+1):
        ret += 2**(top-i) * nCk(b1-i, k-i) * 2**i * nCk(b2, i)
    return 1


"""
There is a non-monochromatic coloring of v for (x,y) :
    There is no Kx fully contained in ordered lines
    Every Ky clique contains at least one ordered line
There is no non-monochromatic coloring of v for (x,y) [v is at or past R(x,y)] :
    There is a Kx fully contained in ordered lines
    There is at least one Ky not containing an ordered line
"""


def compute_early_untouched(v,xy):
    #Num Kxy that don't contain any lines in earlier orders
    #f
    fo = v // 2
    so = fo // 2
    untouched_Kxy_a1oc = 2**xy * nCk(fo,xy) #Don't bother forcing this into calc it's doable but not clean
                                        #These are first order lines momentarily acting like later orders will
    top = min(xy,fo,so)
    untouched_Kxy_a2oc = calc(top, xy, fo, so)
    print(v, "   ", xy, "   ", untouched_Kxy_a1oc, "   ", untouched_Kxy_a2oc)
    return 1

"""
1o = [(0,1),(2,3),(4,5),(6,7),(8,9),(10,11)]
2o = [(0,2),(4,6),(8,10)]
3o = [(1,7),(3,9),(5,11)]

Calculating amount unnafected after third order:
Pick a vertex from the third order. Say 1. Now (0,2) becomes a 1-len box (knock 0 out, it's just (2)).
If the next choice is 3, I'm going to knock 2 out, so that becomes a 0-len box, aka b1-1
If the next choice isn't 3, say 9, I'm going to knock out 8, so (8,10)->(10) and I have two 1-len boxes.

I don't know how to write that formulaically. It will happen symmetrically, so maybe I just need to treat them
as different calculations?

"""



def runThrough():
    compute_early_untouched(16,8)
    compute_early_untouched(16,9)
    compute_early_untouched(20,8)
    compute_early_untouched(20,9)
    compute_early_untouched(24,8)
    compute_early_untouched(24,9)
    return 1

if __name__ == "__main__":
    runThrough()