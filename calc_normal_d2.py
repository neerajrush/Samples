import math

def calc_normal_d():
    mu = 70
    sd = 10
    X1 = 80
    X2 = 59.8 #60 

    # Cumulative probability distribution funtion with Normal distribution:
    # F(x) = 1/2 * (1 + erf( (X-mu) / (sd * 2**0.5)))
    #p_70 =  1/2 * (1 + math.erf( (70 - mu)/ (sd * 2**0.5)))

    p_l80 =  1/2 * (1 + math.erf( (X1 - mu)/ (sd * 2**0.5)))
    p_g80 = (1 - p_l80) * 100
    print("%0.2f" %(p_g80)) # P(X > 80)
    
    # P( a <= X <= b) == P( a < X < b) = Fx(b) - Fx(a)  a = 60, b = 70
    p_l60 = 1/2 * ( 1 + math.erf( (X2 - mu)/ (sd * 2**0.5)))
    p_g60 = (1 - p_l60) * 100
    p_l60 *= 100
    print("%0.2f" %(p_g60)) # P(X >= 60)
    print("%0.2f" %(p_l60)) # P(X < 60)

if __name__ == "__main__":
    calc_normal_d()
