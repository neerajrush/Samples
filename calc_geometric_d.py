def calc_geometric_d():
    batch = 5

    prob_producing_defective = 1/3
    prob_producing_ok = 2/3             #(1 - 1/3)

    pb_first_defect_in_5 =  (prob_producing_ok)**(batch-1) * prob_producing_defective
    print("%.3f" %(pb_first_defect_in_5))

if __name__ == "__main__":
    calc_geometric_d()
