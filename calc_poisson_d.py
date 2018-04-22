import math

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def calc_poisson_d():
    x = 5
    lambda_x = 2.5

    pb_for_5_event =  (lambda_x)**(x) * math.exp(-1 * lambda_x)/factorial(x)
    print("%.3f" %(pb_for_5_event))

if __name__ == "__main__":
    calc_poisson_d()
