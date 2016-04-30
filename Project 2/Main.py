import sys
from SuffixTree.SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree
from SuffixTree import tandem_repeat_finder
from SuffixTree.find_branches import find_branches


def main(argv):
    filename = argv[0]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    print "SuffixTree construction complete"
    tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    tandem_finder.dfs_init(tree=st)

    """
    branches_finder = find_branches(st,
                                    tandem_finder.c2dmap,
                                    tandem_finder.d2cmap,
                                    tandem_finder.internal_nodes)
    branches_finder.start_basic_algorithm()
    """
    print print_suffix_tree(st, extra_info=tandem_finder.internal_nodes,  format='png')


if __name__ == "__main__":
    main(sys.argv[1:])
