from math import floor, factorial

#Say n = 10, k = 2      numer_start = 8
def nCk(n,k):
    numer_start = max(n-k,k)
    denom_fac = min(n-k,k)
    if denom_fac < 0:
        return 0
    numerator = 1
    for i in range(numer_start+1, n+1):
        numerator *= i
    denominator = factorial(denom_fac)
    return (numerator / denominator)

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

def num_K_fully_red_a2oc(fo, xy, vOdd):
    #fo = len(fo_lines), vOdd = 1 if v odd 0 if even
    #soWe is second order line containing the extra vertex
    #soWOe is second order lines not containing the extra vertex
    soWOe = floor(fo / 2)
    if vOdd == 1 and fo & 1:
        soWe = 1
    else:
        soWe = 0
    #additive portion is all Kxy formed by taking 0 or 1 vertex from each first order line, then
        #adding the Kxy that include the extra vertex
    Kxy_formed_from_first_order = (nCk(fo,xy) * 2**xy) + (vOdd * nCk(fo,xy-1) * 2**(xy-1))
    #Subtract out the Kxy that have a second order line
    #First term is all Kxy with a second order line not containing the extra vertex, second term
        #is all Kxy containing it
    Kxy_w_so_l = (soWOe * nCk(fo-2,xy-2) * 2**(xy-2)) + (soWe * nCk(fo-1,xy-2) * 2**(xy-2))
    return Kxy_formed_from_first_order - Kxy_w_so_l



def num_K_with_u_blue_lines_a2oc(fo, xy, vOdd, u):
    #fo = line(fo_lines), vOdd = 1 if v is odd 0 if even
    ret = 0
    if u & 1:     #(so u odd)
        s = fo - u
    else:
        s = int(fo - 1.5*u)
    b = floor((fo+vOdd-u) / 2)     #The number of unsafe blocks
    k = xy - u*2     #These are Kxy. I fixed the first two so I need to fill the rest of the xy spaces
    for i in range(min(b,k)+1):
        ret += (nCk(b,i) * 2**i * nCk(s,k-i))
    if u != 0:
        ret *= fo
    return ret


#a1oc = after first order coloring, a2oc = after second order coloring, etc.
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
    second_order_lines = compute_second_order_lines(first_order_lines, untouched_vertex_a1oc)
    Kx_with_u_blue_lines_a2oc = {}
    Ky_with_u_blue_lines_a2oc = {}
    for u in range(x // 2 + 1):
        Kx_with_u_blue_lines_a2oc[u] = num_K_with_u_blue_lines_a2oc(fo, x, vOdd, u)
    for u in range(y // 2 + 1):
        Ky_with_u_blue_lines_a2oc[u] = num_K_with_u_blue_lines_a2oc(fo, y, vOdd, u)


    #     a1oc metrics
    metrics['Kx_with_u_blue_lines_a1oc'] = Kx_with_u_blue_lines_a1oc
    metrics['Ky_with_u_blue_lines_a1oc'] = Ky_with_u_blue_lines_a1oc

    #     a2oc metrics
    metrics['Kx_with_u_blue_lines_a2oc'] = Kx_with_u_blue_lines_a2oc
    metrics['Ky_with_u_blue_lines_a2oc'] = Ky_with_u_blue_lines_a2oc

    return metrics