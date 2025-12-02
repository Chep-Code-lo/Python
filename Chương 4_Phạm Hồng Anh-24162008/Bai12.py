def cos_taylor(x):
    term = 1        
    result = 1      
    n = 1           
    epsilon = 1e-10 
    while abs(term) > epsilon:
        term *= - x*x / ((2*n - 1) * (2*n)) 
        result += term
        n += 1

    return result
