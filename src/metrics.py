from math import floor, factorial
from itertools import combinations

#Say n = 10, k = 2      numer_start = 8
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

def compute_first_order_lines(v):
    first_order_lines = []
    for i in range(0, v-1, 2):
        first_order_lines.append([i, i+1])
    return first_order_lines

def num_K_with_u_blue_lines_a1oc(fo, xy, vOdd, u):
    k = xy - 2*u     #Spots in the Kxy that need to be filled after fixing u lines
    ret = (nCk(fo-u,k) * 2**(k)) + (vOdd * nCk(fo-u,k-1) * 2**(k-1))
    ret *= nCk(fo,u)
    return ret

def compute_second_order_lines(first_order_lines, untouched_v):
    second_order_lines = []
    for i in range(0, len(first_order_lines), 2):
        second_order_lines.append([first_order_lines[i][0], first_order_lines[i+1][0]])
        if i == len(first_order_lines)-1 and untouched_v:
            second_order_lines.append([first_order_lines[i][0], untouched_v])
    return second_order_lines

def one_u_a2oc(v, xy):
    def calc(top, k, s, b, multiplier=1):
        ret = 0
        for i in range(top+1):
            ret += nCk(s+1-i, k-i) * 2**i * nCk(b-1, i)
        ret *= multiplier
        return ret
    
    fo = v // 2
    so = fo // 2
    if v & 1 and fo & 1:
        so += 1
    k = xy - 2
    b = so - 1
    if v%2==0 and fo & 1:
        b += 1
    top_base = min(b,k)
    ret = 0
    if v & 1:
        if fo & 1: #v,fo odd
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, fo) #All fo_l
            ret += calc(top, k, fo-1, b) #untouched_v so_l
            top = min(top_base,fo-2)
            ret += calc(top, k, fo-2, b, so-1) #All so_l except one with untouched_v
        else: #v odd, fo even                             Right
            top = min(top_base,fo)
            ret += calc(top, k, fo, b, fo) #All fo_l
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, so) #All so_l
    else:
        if fo & 1: #v even fo odd
            top = min(top_base,fo-2)
            ret += calc(top, k, fo-2, b, fo-1) #fo_l except last
            top = min(top_base,fo-3)
            ret += calc(top, k, fo-3, b, so) #All so_l
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b) #Last fo_l
        else: #v, fo even                                 Right
            top = min(top_base,fo-1)
            ret += calc(top, k, fo-1, b, fo) #All fo_l
            top = min(top_base,fo-2)
            ret += calc(top, k, fo-2, b, so) #All so_l
    return ret

"""
Right now for the correct one, v, fo_even I have
    ret += calc(top, k, fo-1, b, fo) #All fo_l
    ret += calc(top, k, fo-2, b, so) #All so_l

for v odd fo_even I have
    ret += calc(top, k, fo, b, fo) #All fo_l
    ret += calc(top, k, fo-1, b, so) #All so_l





"""


#a1oc = after first order coloring, a2oc = after second order coloring
def compute_metrics(v, x, y):
    metrics = {}

    #calculations for first order
    Kx_total = nCk(v,x)
    Ky_total = nCk(v,y)
    if v & 1: #if v is odd
        untouched_vertex_a1oc = [v-1, None]
        vOdd = 1
    else:
        untouched_vertex_a1oc = None
        vOdd = 0
    first_order_lines = compute_first_order_lines(v)
    fo = len(first_order_lines)
    Kx_with_u_blue_lines_a1oc = {}
    Ky_with_u_blue_lines_a1oc = {}
    for u in range(x // 2 + 1):
        Kx_with_u_blue_lines_a1oc[u] = num_K_with_u_blue_lines_a1oc(fo, x, vOdd, u)
    for u in range(y // 2 + 1):
        Ky_with_u_blue_lines_a1oc[u] = num_K_with_u_blue_lines_a1oc(fo, y, vOdd, u)

    #calculations for second order
    """
    second_order_lines = compute_second_order_lines(first_order_lines, untouched_vertex_a1oc)
    Kx_with_u_blue_lines_a2oc = {}
    Ky_with_u_blue_lines_a2oc = {}
    for u in range(x // 2 + 1):
        Kx_with_u_blue_lines_a2oc[u] = num_K_with_u_blue_lines_a2oc(fo, x, vOdd, u)
    for u in range(y // 2 + 1):
        Ky_with_u_blue_lines_a2oc[u] = num_K_with_u_blue_lines_a2oc(fo, y, vOdd, u)
    """

    Kx_with_u_blue_lines_a2oc = {}
    Ky_with_u_blue_lines_a2oc = {}
    Kx_with_u_blue_lines_a2oc[1] = one_u_a2oc(v, x)
    Ky_with_u_blue_lines_a2oc[1] = one_u_a2oc(v, y)


    #     a1oc metrics
    metrics['Kx_with_u_blue_lines_a1oc'] = Kx_with_u_blue_lines_a1oc
    metrics['Ky_with_u_blue_lines_a1oc'] = Ky_with_u_blue_lines_a1oc

    #     a2oc metrics
    metrics['Kx_with_u_blue_lines_a2oc'] = Kx_with_u_blue_lines_a2oc
    metrics['Ky_with_u_blue_lines_a2oc'] = Ky_with_u_blue_lines_a2oc

    return metrics