import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree.TrieNode import TrieNode
from SuffixTree import dfs_preprocessor as searcher

def main(argv):
    filename = argv[0]
    search_tandem = argv[1]
    tandem_finder = searcher.tandem_repeat_finder()
    with open(filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

        # search for the tandem


if __name__ == "__main__":
    main(sys.argv[1:])
