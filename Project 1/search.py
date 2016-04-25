import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import searcher

def main(argv):
    filename = argv[0]
    search_string = argv[1]

    with open(filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    suffix_searcher = searcher.SuffixTreeSearcher()
    suffix_searcher.search(search_string, tree=st)


if __name__ == "__main__":
    main(sys.argv[1:])
