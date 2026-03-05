from itertools import combinations

def build_edges(v):
    # a1 edges: (0,1), (2,3), (4,5), ...
    a1_edges = [(i, i+1) for i in range(0, v-1, 2)]

    # a2 edges: (0,2), (4,6), (8,10), ...
    a2_edges = [(i, i+2) for i in range(0, v-2, 4)]

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