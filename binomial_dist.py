def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def choose(n, x):
    return factorial(n)/(factorial(x) * factorial(n-x))

def calc_binomial_d():
    b = 1.09
    g = 1

    prob_being_boy = 1.09/2.09
    prob_being_girl = 1/2.09

    pb = 0
    for x in range(3,7):
        print(x, choose(6, x))
        pb += choose(6, x) * (1.09/2.09)**(x) * (1/2.09)**(6-x)

    print("%.3f" %(pb))

if __name__ == "__main__":
    calc_binomial_d()
