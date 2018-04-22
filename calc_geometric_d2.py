def calc_geometric_d():
    n = 5

    p = 1/3
    q = 2/3             #(1 - 1/3)

    g = 0
    for x in range(1, n+1):
    	g +=  (q)**(x-1) * p
    print("%.3f" %(g))

if __name__ == "__main__":
    calc_geometric_d()
