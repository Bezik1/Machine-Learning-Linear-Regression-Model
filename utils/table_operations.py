def get_table_mult(x, y):
    res = []
    for i in range(len(x)):
        res.append(x[i]*y[i])
    return res

def get_table_square(x):
    res = []
    for el in x:
        res.append(el**2)
    return res

def table_sum(x):
    res = 0
    for el in x:
        res += el
    return res