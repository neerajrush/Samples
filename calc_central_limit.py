import math

def calc_central_limit():
    sum_xi = 9800  # Max allowed weight of all boxes Sn
    n = 49

    box_mu = 205 # per box
    box_sd = 15  # per box

    collective_mu = n * box_mu
    collective_sd = (n**0.5) * box_sd

    # P(x) = 1/2 * (1 + erf( (X - mu) / (sd * 2**0.5)))
    PXi = 1/2 * (1 + math.erf( (sum_xi - collective_mu)/(collective_sd * 2**0.5)))
    PXi *= 100
    print("%.4f" %(PXi))

def calc_central_limit_2():
    sum_xi = 250  # Max tickets left
    n = 100

    ind_mu = 2.4  # per box
    ind_sd = 2.0  # per box

    collective_mu = n * ind_mu
    collective_sd = (n**0.5) * ind_sd

    # P(x) = 1/2 * (1 + erf( (X - mu) / (sd * 2**0.5)))
    PXi = 1/2 * (1 + math.erf( (sum_xi - collective_mu)/(collective_sd * 2**0.5)))
    print("%.4f" %(PXi))

def calc_central_limit_3():
    population_mu = 500
    population_sd = 80
    sample_n = 100
    
    # In this case mean remains same but the SD will change to population_sd/sqrt(n)
    sample_mu = population_mu
    sample_sd = population_sd/(sample_n**0.5)

    z = 1.96   # 95% of SD, z = (Xi - mu)/sd

    # (Xi - mu) = z * sample_sd
    X_A = sample_mu - z * sample_sd
    X_B = sample_mu + z * sample_sd

    print("%.2f" %(X_A))
    print("%.2f" %(X_B))

if __name__ == "__main__":
    print("-- Central Theorem I")
    calc_central_limit()
    print("-- Central Theorem II")
    calc_central_limit_2()
    print("-- Central Theorem III")
    calc_central_limit_3()
