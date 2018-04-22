def calc_quartile():
    arr_len = int(input())
    arr_vals = input()
    arr = [0] * arr_len
    idx = 0
    for val in arr_vals.split(" "):
        arr[idx] = int(val)
        idx += 1
        if (idx == arr_len):
            break
    if idx != arr_len:
        print("Incomplete input.", arr)
        return
    arr = sorted(arr)
    n = int(arr_len/2)
    
    """ Quartile Q2 """
    q2 = 0 
    if arr_len%2 == 1 or n == 0:
        q2 = arr[n]
    else:
            q2 = int((arr[n-1] + arr[n])/2)
    
    """ Quartile Q2 """
    q1 = 0
    arr_l = []
    nl = 0
    
    if n > 0:
        if arr_len%2 == 1:
            arr_l = arr[0:n]
            nl = int(n/2)
        else:
            arr_l = arr[0:n]
            nl = int(n/2)
        
    if len(arr_l)%2 == 1:
        q1 = arr[nl]
    elif nl > 0:
        q1 = int((arr[nl-1] + arr[nl])/2)
    
    """ Quartile R Q3  """
    q3 = 0
    arr_r = []
    nr = 0
    if n > 0:
        if arr_len%2 == 1:
            arr_r = arr[n+1:]
            nr = int(len(arr_r)/2)
        else:
            arr_r = arr[n:]
            nr = int(len(arr_r)/2)
        
    if (len(arr_r)%2 == 1 or nr == 0) and len(arr_r) > 0:
        q3 = arr_r[nr]
    elif nr > 0:
        q3 = int((arr_r[nr-1] + arr_r[nr])/2)
    
    print(q1)
    print(q2)
    print(q3)
    
if __name__ == "__main__":
    calc_quartile()
