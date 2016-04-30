import sys
from SuffixTree.SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree
from SuffixTree import tandem_repeat_finder
#from SuffixTree.SuffixTree import find_branches


def main(argv):
    filename = argv[0]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    print "SuffixTree construction complete"
    tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    tandem_finder.dfs_init(tree=st)

    print print_suffix_tree(st, 'png')


if __name__ == "__main__":
    main(sys.argv[1:])
