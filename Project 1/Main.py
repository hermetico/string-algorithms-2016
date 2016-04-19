import sys
from TrieNode import TrieNode 
from SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree


def main(argv):
    filename = argv[0]
    search_string = argv[1]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    print "SuffixTree construction complete"
    print "looking for %s"%( search_string)
    st.search(search_string)
    # install graphviz library to print and show an image of the tree
    #print print_suffix_tree(st)
    
    

if __name__ == "__main__":
    main(sys.argv[1:])
