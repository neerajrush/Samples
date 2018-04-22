def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def choose(n, x):
    return factorial(n)/(factorial(x) * factorial(n-x))

def calc_binomial_d():
    rejection = 12
    batch = 10

    prob_being_rejected = 0.12
    prob_being_ok = 0.88             #(1 - 0.12)

    pb_no_more_2 = 0
    for x in range(0,3):
        pb_no_more_2 += choose(batch, x) * (prob_being_rejected)**(x) * (prob_being_ok)**(batch-x)
    print("%.3f" %(pb_no_more_2))

    pb_atleast_2 = 0
    for x in range(2, 11):
        pb_atleast_2 += choose(batch, x) * (prob_being_rejected)**(x) * (prob_being_ok)**(batch-x)
    print("%.3f" %(pb_atleast_2))

if __name__ == "__main__":
    calc_binomial_d()
