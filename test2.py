def calc_mmm():
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

    mean = sum(arr)/len(arr)
    print("%.1f" %(mean))
    m_arr = sorted(arr)
    median = 0
    if len(arr)%2 == 0:
        mid = int(len(arr)/2)
        median = (m_arr[mid-1] + m_arr[mid])/2
    else:
        median = m_arr[int(len(arr)/2)]
        
    print("%.1f" %(median))
    x_list = {}
    max_frq = 0
    min_val = pow(10, 5) + 1
    for i in range(len(arr)):
        print(arr[i])
        if not x_list.__contains__(arr[i]):
            x_list[arr[i]] = 1
        else:
            x_list[arr[i]] += 1 
        if max_frq <= x_list[arr[i]]:
            max_frq = x_list[arr[i]]
        if min_val > arr[i]:
            min_val = arr[i]
          
    if max_frq == 1:
          print(min_val)
    else:
          frq = 0
          val = 0
          print(x_list)
          for k in x_list.keys():
              if frq < x_list[k]:
                  val = k
                  frq = x_list[k]
              elif frq == x_list[k]:
                  val = min(val, k)
          print(val)

if __name__ == "__main__":
	calc_mmm()
