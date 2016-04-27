import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree.TrieNode import TrieNode
from SuffixTree import searcher
import time
from tools.size import getsize


def main(argv):
    filename = argv[0]
    search_string = argv[1]
    suffix_searcher = searcher.SuffixTreeSearcher()
    with open(filename) as file_object:
        content = file_object.read()
        start = time.time()
        st = SuffixTree(content)
        suffix_searcher.search(search_string, tree=st)
        end = time.time()
        print "Time needed: %f" %(end-start)
        print "String size: %i bytes" % (getsize(content))
        print "Tree size: %i bytes" % (getsize(st))
        print "Node size: %i bytes" %(getsize(TrieNode((-1,-1))))
        print "Tree per character size: %f bytes" %(getsize(st)/getsize(content))



if __name__ == "__main__":
    main(sys.argv[1:])
