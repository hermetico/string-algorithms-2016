import sys

from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import dfs_preprocessor
from SuffixTree.tandem_finder import TandemFinder


def main(argv):
    filename = argv[0]

    with open(filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    preprocess = dfs_preprocessor.DFS_preprocessor()
    preprocess.dfs_init(tree=st)

    method = 'optimized'
    if len(argv) > 1:
        method = argv[1]

    tandem_finder = TandemFinder(st,preprocess)
    tandem_repeats = tandem_finder.run(method=method)

    # branching and non branching tandem repeats
    print "1) branching: %i non-branching: %i" %(len(tandem_repeats['b-t-r']), len(tandem_repeats['non-b-t-r']))
    # number of branching and non branching longer than 5
    print "2) branching: %i non-branching: %i" % (tandem_finder.br_longer, tandem_finder.nbr_longer)
    # longest non-branching chain
    print "3) Longest chain: %(len)i, init: %(init)i, end: %(end)i" %(tandem_finder.longest_chain)

    # average of non-branching ones
    print "4) avg: %f"%( len(tandem_repeats['non-b-t-r']) / float(len(tandem_repeats['b-t-r'])))

    # double tandem repeats
    tandem_finder.repeats = 2
    double_tandem_repeats = tandem_finder.run(method=method)

    #print "5) Dobule branching: %i non-branching: %i" %(len(tandem_repeats['b-t-r']), len(tandem_repeats['non-b-t-r']))


if __name__ == "__main__":
    main(sys.argv[1:])
