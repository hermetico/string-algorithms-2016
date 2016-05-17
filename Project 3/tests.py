from exact_pattern_matching.exact_pattern_matching import ExactPatternMatching
from tools.fibonacci_strings import FibonacciStrings
import time
import sys
MIN = 10
MAX = 100000
STEP = 1.1

modes = ['naive-pattern-matching', 'kmp-pattern-matching', 'ba-pattern-matching']
cases = ['best-case', 'fibbonacci-case', 'worst-case']

fb_string = FibonacciStrings().generate(length=MAX)
other_string = ''.join(['a'] * MAX)

#best_pattern = ''.join(['b'] * 20)
best_pattern = 'qwertyuiopsdfghjklzx'
worst_pattern = ''.join(['a'] * 20)
fb_pattern = 'abaababaabaababaabab'
"""
best_pattern = ''.join(['b'] * 7)
worst_pattern = ''.join(['a'] * 7)
fb_pattern = 'abaabab'
"""

pattern_matcher = ExactPatternMatching()


def cool_range(init=1, end=10, step=1):
    iter = init
    while iter < end:
        yield iter
        iter = int(iter * step)


def performance(n, mode='naive-pattern-matching', case='best-case'):
    if case == 'best-case':
        pattern_matcher.search(best_pattern, mode=mode, string=other_string[:n])
    elif case == 'fibbonacci-case':
        pattern_matcher.search(fb_pattern, mode=mode, string=fb_string[:n])
    elif case == 'worst-case':
        pattern_matcher.search(worst_pattern, mode=mode, string=other_string[:n])


def suite(ext = '.txt'):
    results = []
    for mode in modes:
        with open('plots_outputs/' + mode + ext, 'wb') as f:
            for n in cool_range(MIN, MAX, STEP):
                line = [n]
                for case in cases:
                    init = time.clock()
                    # the average of 10 times
                    for x in range(5):
                        performance(n, mode, case)
                    line.append((time.clock() - init) / 5.)

                f.write("%s\n" % (' '.join([str(c) for c in line])))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        pattern = sys.argv[1]
        global fb_pattern
        fb_pattern = pattern
    suite()
