from itertools import combinations

def build_edges(v):
    # a1 edges: (0,1), (2,3), (4,5), ...
    a1_edges = [(i, i+1) for i in range(0, v-1, 2)]

    # a2 edges: (0,2), (4,6), (8,10), ...
    a2_edges = [(i, i+2) for i in range(0, v-2, 4)]

    # odd-v special edge
    if v % 2 == 1:
        last_even = v-1
        if last_even-2 >= 0:
            a2_edges.append((last_even-2, last_even))

    return a1_edges, a2_edges


def brute(v, x, y):
    metrics = {}

    a1_edges, a2_edges = build_edges(v)

    Kx_u_a1oc = {}
    Ky_u_a1oc = {}
    Kx_u_a2oc = {}
    Ky_u_a2oc = {}

    def count_edges(clq, edges):
        clq = set(clq)
        cnt = 0
        for u, w in edges:
            if u in clq and w in clq:
                cnt += 1
        return cnt

    for clq in combinations(range(v), x):
        a1 = count_edges(clq, a1_edges)
        a2 = a1 + count_edges(clq, a2_edges)

        Kx_u_a1oc[a1] = Kx_u_a1oc.get(a1, 0) + 1
        Kx_u_a2oc[a2] = Kx_u_a2oc.get(a2, 0) + 1

    for clq in combinations(range(v), y):
        a1 = count_edges(clq, a1_edges)
        a2 = a1 + count_edges(clq, a2_edges)

        Ky_u_a1oc[a1] = Ky_u_a1oc.get(a1, 0) + 1
        Ky_u_a2oc[a2] = Ky_u_a2oc.get(a2, 0) + 1

    metrics['Kx_with_u_blue_lines_a1oc'] = Kx_u_a1oc
    metrics['Ky_with_u_blue_lines_a1oc'] = Ky_u_a1oc
    metrics['Kx_with_u_blue_lines_a2oc'] = Kx_u_a2oc
    metrics['Ky_with_u_blue_lines_a2oc'] = Ky_u_a2oc

    return metrics




"""
from itertools import combinations

#Create the object and run through calculations brute force. The idea is to verify that I'm doing all my calculations right
def brute(v,x,y):
    metrics = {}

    Kx_cliques = list(combinations(range(v), x))
    Ky_cliques = list(combinations(range(v), y))
    vOdd = v % 2
    if vOdd == 1:
        last_even = v-1
    else:
        last_even = v

    Kx_u_a1oc = {}
    Ky_u_a1oc = {}
    Kx_u_a2oc = {}
    Ky_u_a2oc = {}
    
    def check_a1oc(clq):
        cnt = 0
        for v in clq:
            if v % 2 == 0 and v+1 in clq:
                cnt += 1
        return cnt

    def check_a2oc(clq, last_even, vOdd):
        cnt = 0
        for v in clq:
            if v % 4 == 0 and v+2 in clq:
                cnt += 1
            elif vOdd == 1 and v == last_even:
                if v+2 in clq:
                    cnt += 1
        return cnt

    for clq in Kx_cliques:
        clq = set(clq)
        a1 = check_a1oc(clq)
        a2 = check_a2oc(clq, last_even, vOdd)
        a2 += a1
        Kx_u_a1oc[a1] = Kx_u_a1oc.get(a1, 0) + 1
        Kx_u_a2oc[a2] = Kx_u_a2oc.get(a2, 0) + 1
    for clq in Ky_cliques:
        clq = set(clq)
        a1 = check_a1oc(clq)
        a2 = check_a2oc(clq, last_even, vOdd)
        a2 += a1
        Ky_u_a1oc[a1] = Ky_u_a1oc.get(a1, 0) + 1
        Ky_u_a2oc[a2] = Ky_u_a2oc.get(a2, 0) + 1

    #     a1oc metrics
    metrics['Kx_with_u_blue_lines_a1oc'] = Kx_u_a1oc
    metrics['Ky_with_u_blue_lines_a1oc'] = Ky_u_a1oc

    #     a2oc metrics
    metrics['Kx_with_u_blue_lines_a2oc'] = Kx_u_a2oc
    metrics['Ky_with_u_blue_lines_a2oc'] = Ky_u_a2oc

    return metrics
"""