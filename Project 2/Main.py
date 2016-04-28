import sys
from SuffixTree.SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree
from SuffixTree import tandem_repeat_finder
from SuffixTree.SuffixTree import find_branches


def main(argv):
    filename = argv[0]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    print "SuffixTree construction complete"
    # install graphviz library to print and show an image of the tree

<<<<<<< HEAD
    #tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    #tandem_finder.tandem_repeat_search(tree=st)
    
    
    print "Starting to look for branching tendem repeats"
    branches = find_branches()
    
    
    print st.root.child.child.first_index
    print st.root.child.child.last_index
=======
    tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    tandem_finder.dfs_init(tree=st)

    print print_suffix_tree(st, 'png')
>>>>>>> c9397e6f52cbf841a00cd03f9a1bd6f477cd3914

if __name__ == "__main__":
    main(sys.argv[1:])
