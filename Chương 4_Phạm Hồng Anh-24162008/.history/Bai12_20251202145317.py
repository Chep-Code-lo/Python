def cos_taylor(x, tolerance=1e-10):
    term = 1         
    result = 1       
    n = 1             
    while abs(term) > tolerance:
        term *= -1 * x * x / ((2*n - 1) * (2*n))
        result += term
        n += 1
    return result
