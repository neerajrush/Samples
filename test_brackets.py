def is_open(x):
    if x == '[': 
        return 's', True
    elif x == '{': 
        return 'c', True
    elif x == '(':
        return 'p', True
    return 'x', False

def is_close(x):
    if x == ']': 
        return 's', True
    elif x == '}': 
        return 'c', True
    elif x == ')':
        return 'p', True
    return 'x', False

class p_type:
    def __init__(self, x, x_type):
        self.p = x
        self.t = x_type
        
def is_matched(expr):
    st = [] 
    for x in range(len(expr)):
        x_type, x_open = is_open(expr[x])
        if x_open:
            st.append(p_type(x, x_type))
        else:
            y_type, y_close = is_close(expr[x])
            if y_close:
                if len(st) == 0:
                    return False
                y = st.pop()
                if y.t != y_type:
                    return False
    if len(st) > 0:
        return False
    return True

def test_brackets():
    t = int(input().strip())
    for a0 in range(t):
        expression = input().strip()
        if is_matched(expression) == True:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
	test_brackets()
