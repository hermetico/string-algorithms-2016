import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import dfs_preprocessor
from SuffixTree.TrieNode import TrieNode
from SuffixTree.tandem_finder import TandemFinder
import time
from tools.size import getsize


def main(argv):
    filename = argv[0]

    with open(filename) as file_object:
        content = file_object.read()

    start = time.time()
    st = SuffixTree(content)

    preprocess = dfs_preprocessor.DFS_preprocessor()
    preprocess.dfs_init(tree=st)

    method = 'optimized'
    if len(argv) > 1:
        method = argv[1]

    tandem_finder = TandemFinder(st,preprocess)
    tandem_repeats = tandem_finder.run(method=method)
    end = time.time()

    output =  "%i %i\n" %(len(tandem_repeats['b-t-r']), len(tandem_repeats['non-b-t-r']))
    print output
    print "Time needed: %f" % (end - start)
    print "String size: %i bytes" % (getsize(content))
    print "Tree size: %i bytes" % (getsize(st))
    print "Node size: %i bytes" % (getsize(TrieNode(0,0, None, None, 0, 0)))
    print "Tree per character size: %f bytes" % (getsize(st) / getsize(content))



if __name__ == "__main__":
    main(sys.argv[1:])


