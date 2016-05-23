from exact_pattern_matching.exact_pattern_matching import ExactPatternMatching
from tools.fibonacci_strings import FibonacciStrings
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import searcher
import time
import sys
import os
MIN = 10
MAX = 100000
STEP = 1.1

modes = ['naive-pattern-matching', 'kmp-pattern-matching', 'ba-pattern-matching']
cases = ['best-case', 'fibbonacci-case', 'worst-case']

fb_string = FibonacciStrings().generate(length=MAX)
base_string = ''.join(['a'] * MAX)

"""
#best_pattern = ''.join(['b'] * 20)
best_pattern = 'qwertyuiopsdfghjklzx'
worst_pattern = ''.join(['a'] * 20)
fb_pattern = 'abaababaabaababaabab'
"""

best_pattern = 'qwertyu'
worst_pattern = ''.join(['a'] * 7)
fb_pattern = 'abaabab'


pattern_matcher = ExactPatternMatching()


def cool_range(init=1, end=10, step=1):
    iter_ = init
    while iter_ < end:
        yield iter_
        iter_ = int(iter_ * step)


def performance(n, mode='naive-pattern-matching', case='best-case'):


    if case == 'best-case':
        string = base_string[:n]
        pattern = best_pattern

    elif case == 'fibbonacci-case':
        string = fb_string[:n]
        pattern = fb_pattern

    elif case == 'worst-case':
        string = base_string[:n]
        pattern = worst_pattern

    init = time.clock()
    for x in range(5):
        pattern_matcher.search(pattern, mode=mode, string=string)
    return (time.clock() - init) / .5



def suite(ext = '.txt'):
    results = []
    for mode in modes:
        with open('plots_outputs/' + mode + ext, 'wb') as f:
            for n in cool_range(MIN, MAX, STEP):
                line = [n]
                for case in cases:
                    spent = performance(n, mode, case)
                    line.append(spent)

                f.write("%s\n" % (' '.join([str(c) for c in line])))




def test_files():
    string_file ='chr1_10000000.txt'
    pattern_file = 'pattern%i.txt'
    pattern_sizes = [10, 20, 30, 40, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000]
    folder = os.path.join(os.path.abspath('.'), 'TestFiles')
    string = open(os.path.join(folder, string_file)).read()
    print "pattern", modes
    for size in pattern_sizes:
        pattern = open(os.path.join(folder, pattern_file % size)).read()
        line = [pattern_file % size]
        # tests the rest of them
        for mode in modes:
            init = time.clock()
            # The time spent to link libraries is also considered
            patterns_matcher = ExactPatternMatching()
            test_one(patterns_matcher, pattern, 1, {'mode': mode, 'string': string})
            end = time.clock() - init
            line.append(end)
        print("%s\n" % (' '.join([str(c) for c in line])))




def test_one(lib, pattern, times,  params):
    """
    Tests one library x times searching for pattern
    :param lib: library to use, it must have the function search
    :param pattern: pattern to search
    :param times: times to launch the search function
    :param params: extra parameters for the library, a dictionary which will be expanded as a function parameters
    :return:
    """
    for i in range(times):
        lib.search(pattern, **params)


def test_tree_and_others(ext='.txt'):
    """
    Performs a comparisson between suffix tree and naive, ab, kmp implementations
    Search into a string of length X for the pattern Y, N times.
    The time spent is appended into a file in the next order
    N   suffix-tree     naive   kmp     ba

    The string is computed using fibonacci strings, also the pattern
    :param ext:
    :return:
    """
    max_string = 1000
    max_pattern = 10
    string = FibonacciStrings().generate(length=max_string)
    pattern = FibonacciStrings().generate(length=max_pattern)

    #string = ''.join(['uiopasdfghjklmznxbcv'] * max_string)
    #pattern = 'qwertyu'

    MIN_SEARCHES = 100
    MAX_SEARCHES = 10000

    with open('plots_outputs/suffix_tree_vs_others' + ext, 'wb') as f:
        for i, n in enumerate(cool_range(MIN_SEARCHES, MAX_SEARCHES, STEP)):
            line = [n]

            # tests the suffix tree
            init = time.clock()
            # The time spent to construct the tree is also considered
            st = SuffixTree(string)
            suffix_searcher = searcher.SuffixTreeSearcher()
            # searches n times and gets the time spent
            test_one(suffix_searcher, pattern, n, {'tree': st})
            end = time.clock() - init
            line.append(end)

            # tests the rest of them
            for mode in modes:
                init = time.clock()
                # The time spent to link libraries is also considered
                patterns_matcher = ExactPatternMatching()
                test_one(patterns_matcher, pattern, n, {'mode': mode, 'string': string})
                end = time.clock() - init
                line.append(end)
            f.write("%s\n" % (' '.join([str(c) for c in line])))

            if i % 10 == 0:
                print "%i iterations, current n: %i"%(i, n)


if __name__ == "__main__":
    # tests running time over different patterns
    suite()

    # tests suffix tree over the others
    test_tree_and_others()

    # tests running time of the different files
    test_files()
