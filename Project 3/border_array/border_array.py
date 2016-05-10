__author__ = 'ballololz'

def make_border_array(x):
    n = len(x)
    res = [None]*n
    res[0] = 0

    for i in range (0,n-1):
        b = res[i]
        while b>0 and (x[i+1]!=x[b]):
            b = res[b]
        if x[i+1] == x[b]:
            res[i+1] = b+1
        else:
            res[i+1] = 0
    return res

