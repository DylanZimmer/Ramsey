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
        a1 = check_a1oc(clq)
        a2 = check_a2oc(clq, last_even, vOdd)
        a2 += a1
        Kx_u_a1oc[a1] = Kx_u_a1oc.get(a1, 0) + 1
        Kx_u_a2oc[a2] = Kx_u_a2oc.get(a2, 0) + 1
    for clq in Ky_cliques:
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