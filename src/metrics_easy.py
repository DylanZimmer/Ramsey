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

#NEED TO BE ANSWERING TWO QUESTIONS
    #DO I HAVE A CLIQUE THAT'S FULLY AFFECTED
    #HAS EVERY CLIQUE HAD AT LEAST ONE LINE AFFECTED

"""
v=12
fo=[(0,1),(2,3),(4,5),(6,7),(8,9),(10,11)]
so=[(0,2),(4,6),(8,10)]
Contains one blue line is 

k=xy-2u for 2u <= min(s,b)
b=3

For u=2
nCk(s-i,k-i) * 2**i * nCk(b-u,i)


For u = 0
fix 0 lines
s = fo
b = so
k = xy
nCk(sC)

i has to go through all s, as well as all b. So it's min(s,b,k)
pick k-i s, 2**i * nCk()
"""

def compute_easy(v,x,y):
    def after_2o(v,xy):
        def calc(top, k, s, b, multiplier=1):
            ret = 0
            for i in range(top+1):
                ret += nCk(s-i, k-i) * 2**i * nCk(b, i)
            ret *= multiplier
            return ret
        
        a2oc = {}
        fo=v//2
        so=fo//2

        for u in range(xy):
            k=xy-(2*u)
            b=so-u
            top_base = min(b,k)
            top = min(top_base,fo-u)
            ret=0
            if u == 0:
                ret += calc(top, k, fo-u, so) #All fo_l   fo-u works because u==0
            elif u == 1:
                ret += calc(top, k, fo-u, so-1, multiplier=fo) #All fo_l
            elif u == 2:
                ret += calc(top, k, fo-u, so-2, multiplier=nCk(fo,2)) #calc portion is coming out as 1, then multiplying nCl(fo,2)
                print(v, " 2 fo for ", xy, "vertices  : ", ret)

            top = min(top_base,fo-2*u)

            if u == 1:
                ret += calc(top, k, fo-2*u, so-1, multiplier=so) #All so_l
            elif u == 2:
                ret += calc(top, k, fo-2*u, so-2, multiplier=nCk(so,2))
                print(v, " 2 so for ", xy, "vertices  : ", ret)
                

            if u == 2:
                #One fo with one so
                top = min(so-1,fo-3,k)
                #For s knock off one fo per fixed fo and two fo's per fixed so
                ret += calc(top, k, fo-3, so-1, multiplier=so*fo)
                print(v, " 1 each for ", xy, "vertices  : ", ret)

            a2oc[u] = ret

        return a2oc

    
    a1oc_ex = {}
    a1oc_ex[1] = 1
    metrics={}
    metrics['Kx_with_u_blue_lines_a1oc'] = a1oc_ex
    metrics['Ky_with_u_blue_lines_a1oc'] = a1oc_ex
    metrics['Kx_with_u_blue_lines_a2oc'] = after_2o(v,x)
    metrics['Ky_with_u_blue_lines_a2oc'] = after_2o(v,y)

    return metrics