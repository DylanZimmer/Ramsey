from math import comb, floor, factorial

#Check to make sure all similarities are subtracted in all coloring combinations     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Say n = 10, k = 2      numer_start = 8
def nChoosek(n,k):
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
    first_line = nChoosek(v-2, newXY)
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

"""
Do x=5 v=7
fo_lines = [ (0,1), (2,3), (4,5) ]    untouched_v = 6
so_lines = [ (0,2), (4,6) ]
0,2:
    (0,1,2,x,y), (0,2,3,x,y), (0,2,4,5,x)
4,6:
    (0,1,4,6,x), (2,3,4,6,x), (4,5,6,x,y)
Duplicates:
    (0,1,2,4,6), (0,2,3,4,6), (0,2,4,5,6)        nChoosek(v-4, xy-4)
"""
def num_K_with_two_blue_lines_a2oc(v, xy, fo_lines, so_lines, untouched_v):
    ret = 0
    if untouched_v:
        fo_lines.append(untouched_v)
    matching_vertex = nChoosek(v-3,xy-3)  #so_l[0]=0, fo_l[0]=0, K5 double colored is (0,1,2,x,y)
    no_matching_vertices = nChoosek(v-4,xy-4)  #(0,2) (4,5) K5 double colored is (0,2,4,5,x)
    for so_l in so_lines:
        for fo_l in fo_lines:
            if so_l[0] == fo_l[0] or so_l[1] == fo_l[0]:
                ret += matching_vertex
            else:
                ret += no_matching_vertices
    ret -= no_matching_vertices     #Remove duplicates
    return ret


"""
Total red lines =
    For x=5 v=7
    (0,3,4,)
    (0,3,5,6)
"""
# THE Kxy CONTAINING ONLY RED AT THIS POINT DON'T HAVE A FIRST OR SECOND ORDER LINE,
    #



"""
Do x=5 v=7
fo_lines = [ (0,1), (2,3), (4,5) ]    untouched_v = 6
so_lines = [ (0,2), (4,6) ]
0,2:
    (0,1,2,x,y), (0,2,3,x,y), (0,2,4,5,x)
4,6:
    (0,1,4,6,x), (2,3,4,6,x), (4,5,6,x,y)
K5 with one blue line from 0,2:
    (0,2,)
"""
def num_K_with_one_blue_line_a2oc():
    #It's the total number that each so_line flips, minus the number that it adds the second blue line to
    # nChoosek(v-2,xy-2)  This is the number that each line flips
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
        ret += nChoosek(v-)
    # (0,2,)


    return 1



#a1oc = after first order coloring, a2oc = after second order coloring, etc.
def compute_metrics(v, x, y):
    metrics = {}

    #calculations for first order
    Kx_total = nChoosek(v,x)
    Ky_total = nChoosek(v,y)
    if v & 1: #bitwise operator to check if last digit is odd
        untouched_vertex_a1oc = [v-1, None]
    else:
        untouched_vertex_a1oc = None
    first_order_lines = compute_first_order_lines(v)
    nKyW1b_a1oc = num_K_with_one_blue_line_a1oc(v, y, len(first_order_lines))
    nKxW1b_a1oc = num_K_with_one_blue_line_a1oc(v, x, len(first_order_lines))

    #calculations for second order
    second_order_lines = compute_second_order_lines(first_order_lines, untouched_vertex_a1oc)
    nKyW2b_a2oc = num_K_with_two_blue_lines_a2oc(v, y, first_order_lines, second_order_lines, untouched_vertex_a1oc)
    nKxW2b_a2oc = num_K_with_two_blue_lines_a2oc(v, x, first_order_lines, second_order_lines, untouched_vertex_a1oc)


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
    metrics['num_Ky_still_fully_red_a2oc'] = v
    metrics['num_Kx_with_two_blue_lines_a2oc'] = nKxW2b_a2oc
    metrics['num_Kx_with_one_blue_line_a2oc'] = v
    metrics['num_Kx_still_fully_red_a2oc'] = v
    metrics['untouched_vertex_a2oc'] = v


    return metrics