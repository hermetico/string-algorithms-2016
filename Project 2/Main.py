import sys
from SuffixTree.SuffixTree import SuffixTree
from tools.outputs import print_suffix_tree
from SuffixTree import dfs_preprocessor
from SuffixTree.tandem_finder import TandemFinder


def main(argv):
    filename = argv[0]

    print "Reading " + filename + ":"

    with open("Files/" + filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    preprocess = dfs_preprocessor.DFS_preprocessor()
    preprocess.dfs_init(tree=st)

    method = 'basic'
    if len(argv) > 1:
        method = argv[1]


    if method == 'basic':
        tandem_finder = TandemFinder(st,preprocess)
        tandem_repeats = tandem_finder.run(method='basic')

    elif method == 'optimized':
        tandem_finder = TandemFinder(st,preprocess)
        tandem_repeats = tandem_finder.run(method='optimized')


    output =  "%s: %i %i\n" %(filename, len(tandem_repeats['b-t-r']), len(tandem_repeats['non-b-t-r']))
    print output
    return output


"""
##leftrotation:
tandemrepeats = []
tandemrepeats.append(tandem_finder_opt.b_t_r)
for ind, length, two in tandem_finder_opt.b_t_r:
    i=1
    while content[ind-i] == content[ind+length-i]:
        tandemrepeats.append((ind-i,length,2))
        i +=1

#print "\n\n\tThe tandem repeats: " + str(tandemrepeats) ##testing output


    #print branches_finder_bas.b_t_r
    #print branches_finder_opt.b_t_r

    str = "\n\t"+filename+": %i %i"%( len(tandemrepeats[0]) , len(tandemrepeats)-1 ) ##Output that they ask for in the assignment
    print str

"""


if __name__ == "__main__":
    main(sys.argv[1:])
