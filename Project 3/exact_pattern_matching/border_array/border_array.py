__author__ = 'ballololz'

def make_border_array(x):
    n = len(x)
    res = [None]*n
    res[0] = 0

    for i in range (0,n-1):
        b = res[i]
        while b>0 and (x[i+1]!=x[b]):
            b = res[b-1]
        if x[i+1] == x[b]:
            res[i+1] = b+1
        else:
            res[i+1] = 0
    return res

def BA_search(x, pattern):#psx_ba=None): #exact pattern matching with border arrays

    #if psx_ba==None:
    #    psx_ba = make_border_array(pattern+"$"+x)
    m = len(pattern)
    psx_ba = make_border_array(pattern+"$"+x)
    for index, val in enumerate(psx_ba):
        if val == m:
            print index-2*m

