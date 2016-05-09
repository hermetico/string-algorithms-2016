import sys
from SuffixTree.SuffixTree import SuffixTree
from SuffixTree import dfs_preprocessor
from SuffixTree.tandem_finder import TandemFinder


def main(argv):
    filename = argv[0]

    with open(filename) as file_object:
        content = file_object.read()
        st = SuffixTree(content)

    preprocess = dfs_preprocessor.DFS_preprocessor()
    preprocess.dfs_init(tree=st)

    method = 'optimized'
    if len(argv) > 1:
        method = argv[1]

    tandem_finder = TandemFinder(st,preprocess)
    tandem_repeats = tandem_finder.run(method=method)


    output =  "%i %i\n" %(len(tandem_repeats['b-t-r']), len(tandem_repeats['non-b-t-r']))
    print output



if __name__ == "__main__":
    main(sys.argv[1:])
