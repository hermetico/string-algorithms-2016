import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import dfs_preprocessor
from SuffixTree.tandem_finder import TandemFinder
from tools import fibonacci_strings
import time
import os

MIN = 10
MAX = 1000
STEP = 1.3
RANDOM_TEXT_FILE = 'some_randomness.txt'
modes = ['worst-case', 'fibonacci-case', 'random-case']

# temporal solution
#sys.setrecursionlimit(100000)

def test(st, method):

    # runs the preprocessing
    preprocess = dfs_preprocessor.DFS_preprocessor()
    preprocess.dfs_init(tree=st)
    # runs the search algorithm accordingly
    tandem_finder = TandemFinder(st, preprocess)
    tandem_repeats = tandem_finder.run(method=method)


def performance(mode='worst-case', method='basic'):

    if mode == 'worst-case':
        string = ['a'] * MAX
    elif mode == 'fibonacci-case':
        fb = fibonacci_strings.FibonacciStrings()
        string = fb.generate(length=MAX)
    elif mode == 'random-case':
        with open("Files/" + RANDOM_TEXT_FILE) as rf:
            string = rf.read(MAX)


    with open("plots/" + method + "-" + mode + ".txt", 'w') as f:
        size = MIN
        while size < MAX:
            # builds the suffix tree with a string of size=size
            st = SuffixTree(str(string[:size]))
            init = time.clock()
            test(st, mode)
            end = time.clock()
            f.write("%i %f\n"%(size, end-init))

            size = int(size * STEP)




if __name__ == "__main__":
    performance()
    performance('fibonacci-case')
    performance('random-case')
    performance(method='optimized')
    performance(mode="fibonacci-case", method='optimized')
    performance(mode="random-case", method='optimized')
