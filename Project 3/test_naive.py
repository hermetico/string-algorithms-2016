__author__ = 'ballololz'
import time
import os

def time_naive_c(str="Mississippi",pat="ss"):
    start = time.clock();
    print start
    os.system("echo SDSDSD")
    #os.system(str.format('test "%s" %s')%(str, pat))
    end = time.clock();
    res = end - start
    print (res)
    return (res)



