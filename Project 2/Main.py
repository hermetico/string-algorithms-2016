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

    #print "SuffixTree construction complete"
    #print_suffix_tree(st, extra_info=tandem_finder.internal_nodes,  format='png')


    tandem_finder = tandem_repeat_finder.tandem_repeat_finder()
    tandem_finder.dfs_init(tree=st)


    branches_finder_bas = find_branches(st,
                                    tandem_finder.c2dmap,
                                    tandem_finder.d2cmap,
                                    tandem_finder.internal_nodes)
    branches_finder_bas.start_basic_algorithm()


    branches_finder_opt = find_branches(st,
                                    tandem_finder.c2dmap,
                                    tandem_finder.d2cmap,
                                    tandem_finder.internal_nodes)
    branches_finder_opt.start_optimized_basic_algorithm()


    ##leftrotation:
    tandemrepeats = []
    tandemrepeats.append(branches_finder_opt.b_t_r)
    for ind, length, two in branches_finder_opt.b_t_r:
        i=1
        while content[ind-i] == content[ind+length-i]:
            tandemrepeats.append((ind-i,length,2))
            i +=1

    #print "\n\n\tThe tandem repeats: " + str(tandemrepeats) ##testing output


    str = "\n\t"+filename+": %i %i"%( len(tandemrepeats[0]) , len(tandemrepeats)-1 ) ##Output that they ask for in the assignment
    print str

    #print branches_finder_bas.b_t_r
    #print branches_finder_opt.b_t_r


    return str

    



if __name__ == "__main__":
    main(sys.argv[1:])
