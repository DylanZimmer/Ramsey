from math import comb, floor, factorial

#Say n = 10, k = 2      numer_start = 8
def nCk(n,k):
    numer_start = max(n-k,n)
    denom_fac = min(n-k,n)
    numerator = 1
    for i in range(numer_start+1, k+1):
        numerator *= i
    denominator = factorial(denom_fac)
    return (numerator / denominator)

def compute_first_order_lines(v):
    first_order_lines = []
    for i in range(0, v, 2):
        first_order_lines.append([i, i+1])
    return first_order_lines

def num_K_with_one_blue_line_a1oc(v, xy, num_fol):
    # newXY is num spots remaining per Kx or Ky after fixing one line
    newXY = xy - 2
    first_line = nCk(v-2, newXY)
    ret = 0
    for i in range(num_fol):
        #Is it - i or is that only because I was thinking about R(3,4)?     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ret += first_line - i
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
    Kxy_formed_from_first_order = (nCk(fo,xy) * 2**xy) + (vOdd * nCk(fo,x-1) * 2**(xy-1))
    #Subtract out the Kxy that have a second order line
    #First term is all Kxy with a second order line not containing the extra vertex, second term
        #is all Kxy containing it
    Kxy_w_so_l = (soWOe * nCk(fo-2,xy-2) * 2**(xy-2)) + (soWe * nCk(fo-1,xy-2) * 2**(xy-2))
    return Kxy_formed_from_first_order - Kxy_w_so_l

def num_K_with_one_blue_line_a2oc(fo, xy, vOdd):
    #fo = line(fo_lines), vOdd = 1 if v is odd 0 if even
    #
    #All Kxy containing a blue line from first order, some with multiple because they include second order lines as well
    #This is per fo_l, say whole fo_l is in Kxy, pick 0 or 1 vertex from the rest of the fo_lines. Second term is all Kxy with
        #the fixed fo_l and the extra vertex. Will multiply by number of fo_lines after I get subtraction
    Kxy_U_from_fo_l = nCk(fo-1,xy-2) * 2**(xy-2) + (vOdd * nCk(fo-1,xy-3) * 2**(xy-3))
    #All Kxy with a blue fo_l that also contains a so_l
    #First term is so_l without a vertex in the picked fo_l, second term is with one
    U_from_fo_l_W_so_l = 


    Kxy_U_from_so_l_WOe = 
    Kxy_UFrom_so_l_We = 


    return 1




"""
fo_lines = [ (0,1), (2,3), (4,5) (6,7) (8,9), (10,11), (12,13) ]    untouched_v = 14
so_lines = [ (0,2), (4,6), (8,10), (12,14) ]

x=7 v=15:
Work it through computing by each fo_line
(0,1) is in _____ K7 with one blue line:
    (0,1,a,b,c,d,e) where a,b,c,d,e != 2 (for 0,2), and fo_l or so_l
    I need to go back to thinking about picking 0 or 1 vertices from the rest of the fo_lines        FOR 0,1 :
        (2,3): I can pick 3 but not 2 because 0,2 is a second order line
        (4,5): I can pick either
        (6.7): I can pick either for 5, only 7 for 4
        (8,9): I can pick either
        (10,11): I can pick either for 9, only 11 for 8
        (12,13): I can pick either
        14: I can pick with 13 but not 12
    FOR (2,3) :
        ()
(0,2) after is in ___ K7 with one blue line:





Below is what I added together - each so_lines K5 with each fo_line
0,2:
    (0,1,2,x,y), (0,2,3,x,y), (0,2,4,5,x), (0,2,6,7,x)    Leave off untouched_v. I can because I'm summing each individually (0,2,8,x,y)
4,6:
    (0,1,4,6,x), (2,3,4,6,x), (4,5,6,x,y), (4,6,7,x,y)    Leave off untouched_v (4,6,8,x,y)
Duplicates:
    (0,1,2,4,6), (0,2,3,4,6), (0,2,4,5,6), 
    nCk(v-4, xy-4)

I'm fine to count duplicates based on the above structures because they're what's being summed
(0,1,2,x,y) & (0,2,3,x,y) -> duplicates are (0,1,2,3,x)
()

"""

def num_K_with_two_blue_lines_a2oc(v, xy, fo_lines, so_lines, untouched_v):
    ret = 0
    if untouched_v:
        fo_lines.append(untouched_v)
    matching_vertex = nCk(v-3,xy-3)  #so_l[0]=0, fo_l[0]=0, K5 double colored is (0,1,2,x,y)
    no_matching_vertices = nCk(v-4,xy-4)  #(0,2) (4,5) K5 double colored is (0,2,4,5,x)
    for so_l in so_lines:
        for fo_l in fo_lines:
            if so_l[0] == fo_l[0] or so_l[1] == fo_l[0]:
                ret += matching_vertex
            else:
                ret += no_matching_vertices
    ret -= no_matching_vertices     #Remove duplicates
    return ret


    #It's the total number that each so_line flips, minus the number that it adds the second blue line to
    # nCk(v-2,xy-2)  This is the number that each line flips
    # Remove the shared Kxy between the so_l with one blue line, then subtract the number of Kxy with two blue lines
    """
    Which K5 containing 0,2 are double colored at this point?
    (0,1,2,x,y) (0,2,3,x,y) (0,2,4,5,x) (0,1,4,6,x) (2,3,4,6,x) (4,5,6,x,y)

    If I calculate each so_l 
    """
    matching_vertex_for_subtracting = 
    non_matching_vertex_for_subtracting = 
    ret = 0
    for so_l in so_lines:
        ret += nCk(v-)
    # (0,2,)

    return 1




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
    nKyW1b_a1oc = num_K_with_one_blue_line_a1oc(v, y, len(first_order_lines))
    nKxW1b_a1oc = num_K_with_one_blue_line_a1oc(v, x, len(first_order_lines))

    #calculations for second order
    second_order_lines = compute_second_order_lines(first_order_lines, untouched_vertex_a1oc)
    nKyW2b_a2oc = num_K_with_two_blue_lines_a2oc(v, y, first_order_lines, second_order_lines, untouched_vertex_a1oc)
    nKxW2b_a2oc = num_K_with_two_blue_lines_a2oc(v, x, first_order_lines, second_order_lines, untouched_vertex_a1oc)
    nKyW0b_a2oc = num_K_fully_red_a2oc(len(first_order_lines), y, vOdd)
    nKxW0b_a2oc = num_K_fully_red_a2oc(len(first_order_lines), x, vOdd)

    #     a1oc metrics
    metrics['num_first_order_lines'] = floor(v / 2)
    metrics['first_order_lines'] = first_order_lines
    metrics['num_Ky_with_one_blue_line_a1oc'] = nKyW1b_a1oc
    metrics['num_Ky_still_fully_red_a1oc'] = Ky_total - nKyW1b_a1oc
    metrics['num_Kx_with_one_blue_line_a1oc'] = nKxW1b_a1oc
    metrics['num_Kx_still_fully_red_a1oc'] = Kx_total - nKxW1b_a1oc
    metrics['untouched_vertex_a1oc'] = untouched_vertex_a1oc

    #     a2oc metrics
    metrics['num_second_order_lines'] = floor(len(first_order_lines) + len(untouched_vertex_a1oc) / 2)
    metrics['second_order_lines'] = second_order_lines
    metrics['num_Ky_with_two_blue_lines_a2oc'] = nKyW2b_a2oc
    metrics['num_Ky_with_one_blue_line_a2oc'] = v
    metrics['num_Ky_still_fully_red_a2oc'] = nKyW0b_a2oc
    metrics['num_Kx_with_two_blue_lines_a2oc'] = nKxW2b_a2oc
    metrics['num_Kx_with_one_blue_line_a2oc'] = v
    metrics['num_Kx_still_fully_red_a2oc'] = nKxW0b_a2oc
    metrics['untouched_vertex_a2oc'] = v


    return metrics