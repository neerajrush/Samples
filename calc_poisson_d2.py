import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def calc_poisson_d2():
    lambda_A = 0.88
    lambda_B = 1.55
    # based on P(X = k) = lambda **(k) + math.exp(-1 * lambda)/k!
    # for k in range(1, inf):
    # calculated cumulative probability (X**2): lambda + lambda**2
    
    X_sq =  lambda_A + lambda_A**2 
    Y_sq =  lambda_B + lambda_B**2

    print("%.3f" %(X_sq))
    print("%.3f" %(Y_sq))

    C_A = 160 + 40 * X_sq 
    C_B = 128 + 40 * Y_sq

    print("%.3f" %(C_A))
    print("%.3f" %(C_B))

if __name__ == "__main__":
    calc_poisson_d2()
