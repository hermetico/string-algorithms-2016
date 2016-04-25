import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import searcher
import time

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
        print end-start


if __name__ == "__main__":
    main(sys.argv[1:])
