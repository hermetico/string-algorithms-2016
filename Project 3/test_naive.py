__author__ = 'ballololz'
import time
import os

def time_naive_cpp(str="Mississippi",pat="ss"):
    cpp_file = "test2" #name of the c-executable
    cmdstring = "%s \"%s\" %s"%(cpp_file,str, pat); #the command we are timing
    #print "Command line: " + cmdstring
    #print "below is output from c++ \n"
    start = time.clock();
    os.system(cmdstring) #execute it. The result will also show up in the python terminal
    end = time.clock();
    res = end - start
    #print ("Time from python was %f\n"%res)
    return (res)

def time_naive_python(str="Mississippi",pat="ss"):
    #test.exe is old one. test2.exe times from inside cpp
    from exact_pattern_matching.exact_pattern_matching import ExactPatternMatching
    pm = ExactPatternMatching(str)
    start = time.clock()
    pm.naive_pattern_matching(pat)
    end = time.clock()
    res = end-start
    print res
    return res
if __name__ == "__main__":
    print "time naive c:"
    time_naive_cpp()
    print "time naive python:"
    time_naive_python()



