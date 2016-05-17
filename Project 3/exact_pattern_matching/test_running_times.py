__author__ = 'ballololz'
import time
from exact_pattern_matching import ExactPatternMatching

if __name__ == '__main__':
    i = 3
    f = open('runningtimes', 'w')
    while(i<300):
        str = "".join(['a'] * (20+i))


        epm = ExactPatternMatching(str)
        pat = "".join(['a']*i)
        start = time.clock()
        #os.system(cmdstring) #execute it. The result will also show up in the python terminal
        epm.search(pat)
        end = time.clock()
        res = end - start
        #print ("Time from python was %f\n"%res)


        f.write("%i\t%f\n"%(i, res))
        i+=1
        i = int(i)


    f.close()