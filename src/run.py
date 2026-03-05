
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


def main(v, xy):
    def calc(top, k, s, b, multiplier=1):
        ret = 0
        for i in range(top+1):
            ret += nCk(s-i,k-i) * 2**i * nCk(b,i)
        ret *= multiplier
        return ret
    
    def calc2(k, s, b, multiplier=1):
        ret = 0
        min_i = max(0, k - s)   # must pick at least k-s from b if s doesn't cover k
        max_i = min(k, b)       # cannot pick more than k from b
        for i in range(min_i, max_i+1):
            ret += nCk(s, k-i) * 2**i * nCk(b, i)
        ret *= multiplier
        return ret
    
    fo = v // 2
    so = fo // 2
    if fo & 1 and v & 1:
        so += 1
    k = xy - 2
    b = so - 1
    if v%2==0 and fo & 1:
        b += 1
    top_base = min(b,k)
    ret = 0
    print(fo)
    print(so)
    print(k)
    print(b)
    if v & 1:
        if fo & 1: #v,fo odd
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, fo) #All fo_l
            ret += calc(top, k, fo-1, b) #untouched_v so_l
            top = min(top_base,fo-2)
            ret += calc(top, k, fo-2, b, so-1) #All so_l except one with untouched_v
        else: #v odd, fo even
            top = min(top_base,fo)
            ret += calc(top, k, fo, b, fo) #All fo_l
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, so) #All so_l
    else:
        if fo & 1: #v even fo odd
            top = min(top_base,fo-2)
            print(b,k,fo-2,top)
            ret += calc2(k, fo-2, b, fo-1) #fo_l except last
            ret1 = ret
            print(ret1)
            top = min(top_base,fo-3)
            print(b,k,fo-3,top)
            ret += calc2(k, fo-3, b, so) #All so_l
            ret2 = ret - ret1
            print(ret2)
            top = min(top_base,fo-1)
            print(b,k,fo-1,top)
            ret += calc2(k, fo-1, b) #Last fo_l
            ret3 = ret - ret2 - ret1
            print(ret3)
        else: #v, fo even
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, fo) #All fo_l
            top = min(top_base,fo-2)
            ret += calc(top, k, fo-2, b, so) #All so_l
    return ret

if __name__ == "__main__":
    main(14,4)