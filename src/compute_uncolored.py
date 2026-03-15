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