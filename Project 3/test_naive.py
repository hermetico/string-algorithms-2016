__author__ = 'ballololz'
import time
import os

def time_naive_cpp(str="Mississippi",pat="ss"):
    cpp_file = "testtimefile" #name of the c-executable
    cmdstring = cpp_file #the command we are timing

    f = open("args", 'wb')
    f.write(str+ " "+pat+"\n")
    f.close()
    os.system(cmdstring +" >> cpp_naive_output.t") #execute it. The result will also show up in the python terminal
    #end = time.clock();
    #res = end - start
    #print ("Time from python was %f\n"%res)
    return #(res)

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
    #print "time naive c:"
    i = 10000000 #10 mil
    while(i<80000000): #80 mil
        str = "".join(['a']*i)
        pat = "".join(['a']*7)
        time_naive_cpp(str, pat)
        i= int(i*1.1)


    #print "time naive python:"
    #time_naive_python()



