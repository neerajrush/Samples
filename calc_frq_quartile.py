def calc_frq_quartile():
    arr_len = int(input())
    arr_vals = input()
    arr_frqs = input()
    arr_v = [0] * arr_len
    arr_f = [0] * arr_len
    idx = 0
    for val in arr_vals.split(" "):
        arr_v[idx] = int(val)
        idx += 1
        if (idx == arr_len):
            break
    if idx != arr_len:
        print("Incomplete input.", arr_vals)
        return

    idx = 0
    for frq in arr_frqs.split(" "):
        arr_f[idx] = int(frq)
        idx += 1
        if (idx == arr_len):
            break
    if idx != arr_len:
        print("Incomplete input.", arr_frqs)
        return

    idx = 0
    arr_full = []
    for i in range(arr_len):
        for f in range(arr_f[i]):
            arr_full.append(arr_v[i])

    arr_fx = sorted(arr_full)
    arr_fx_len = len(arr_fx)
    n = int(arr_fx_len/2)
    
    """ Quartile Q2 """
    q2 = 0 
    if arr_fx_len%2 == 1 or n == 0:
        q2 = arr_fx[n]
    else:
            q2 = (arr_fx[n-1] + arr_fx[n])/2
    
    """ Quartile Q2 """
    q1 = 0
    arr_l = []
    nl = 0
    
    if n > 0:
        if arr_fx_len%2 == 1:
            arr_l = arr_fx[0:n]
            nl = int(n/2)
        else:
            arr_l = arr_fx[0:n]
            nl = int(n/2)
        
    if len(arr_l)%2 == 1:
        q1 = arr_fx[nl]
    elif nl > 0:
        q1 = (arr_fx[nl-1] + arr_fx[nl])/2
    
    """ Quartile R Q3  """
    q3 = 0
    arr_r = []
    nr = 0
    if n > 0:
        if arr_fx_len%2 == 1:
            arr_r = arr_fx[n+1:]
            nr = int(len(arr_r)/2)
        else:
            arr_r = arr_fx[n:]
            nr = int(len(arr_r)/2)
        
    if (len(arr_r)%2 == 1 or nr == 0) and len(arr_r) > 0:
        q3 = arr_r[nr]
    elif nr > 0:
        q3 = (arr_r[nr-1] + arr_r[nr])/2
    
    #print(q1)
    #print(q2)
    #print(q3)

    print("%.1f" %(q3 - q1))
    
if __name__ == "__main__":
    calc_frq_quartile()
