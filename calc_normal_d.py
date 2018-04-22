import math

def calc_normal_d():
    mu = 20
    sd = 2
    X1 = 19.5
    X2 = [20, 22]
    variance = sd**2
    # Cumulative probability distribution funtion with Normal distribution:
    # F(x) = 1/2 * (1 + erf( (X-mu) / (sd * 2**0.5)))
    p_x1 =  1/2 * ( 1 + math.erf( (X1 - mu)/ (sd * 2**0.5)))
    print("%0.3f" %(p_x1))

    p_x20 =  1/2 * ( 1 + math.erf( (20 - mu)/ (sd * 2**0.5)))
    print("%0.3f" %(p_x20))

    p_x22 =  1/2 * ( 1 + math.erf( (22 - mu)/ (sd * 2**0.5)))
    print("%0.3f" %(p_x22))

    print("%0.3f" %(p_x22 - p_x20))

if __name__ == "__main__":
    calc_normal_d()
