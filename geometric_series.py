def termOfGP(a, b, n):
    """
    Function to find the nth term of a geometric progression (GP)
    given the first two terms a and b.

    Parameters:
    a (float): The first term of the GP.
    b (float): The second term of the GP.
    n (int): The term number to find.

    Returns:
    float: The nth term of the GP.
    """
    # Calculate the common ratio
    r = b / a
    
    # Calculate the nth term using the formula: nth_term = a * r^(n-1)
    nth_term = a * (r ** (n - 1))
    
    return nth_term

print(termOfGP(1, 2, 2))
# another way 

def termOfGP(a, b, n):
    if a == 0:
        return 0

    r = b // a
    x =pow(r, n - 1)
    return a * x

print(termOfGP(1, 2, 2))