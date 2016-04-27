import sys
from SuffixTree.SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree
from SuffixTree import tandem_repeat_finder


def main(argv):
    filename = argv[0]
    search_string = argv[1]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    print "SuffixTree construction complete"
    # install graphviz library to print and show an image of the tree
    print print_suffix_tree(st, 'png')


    tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    tandem_finder.tandem_repeat_search(tree=st)


if __name__ == "__main__":
    main(sys.argv[1:])
