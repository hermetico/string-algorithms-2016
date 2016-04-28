class tandem_repeat_finder():
    def __init__(self, st=None):
        if st is not None:
            self.refill(st)

    def refill(self, st):
        self.tree = st
        self.root = st.root
        self.endd_key = st.end_key
        self.string = st.string
        self.end = st.end
        self.output = []
        self.d2cmap = [-1]*(len(st.string))
        self.c2dmap = [-1]*(len(st.string))


    def dfs_init(self, node=None, tree=None, depth=0):

        if tree is not None:
            self.refill(tree)

        if node is None:
            node = self.root
            self.output = []


        ##### depth first numbering and map d2c/c2d creation#####
        self.dfs_numbering(self.root,0,depth)


        self.tree.C2D = str(self.c2dmap)
        self.tree.D2C = str(self.d2cmap)
        print "c2d: " + str(self.c2dmap)
        print "d2c: " + str(self.d2cmap)


    def dfs_numbering(self, node, number, depth):

        if node.child is not None: ##we have child

            node.depth = depth ##only need depth in internal nodes
            node.interval_start = number
            number = self.dfs_numbering(node.child, number,depth+1+(node.child.last_index - node.child.first_index))

            node.interval_end = number-1
        else: ##we are leaf
            node.dfs_number = number
            self.d2cmap[number] = node.construction_number
            self.c2dmap[node.construction_number] = number
            number+=1


        if node.sibling is not None: ##we have sibling
            return self.dfs_numbering(node.sibling, number,depth-(node.last_index-node.first_index)+(node.sibling.last_index-node.sibling.first_index))
        else: #we are last sibling
            return number






    def __leaf_search__(self, node, amount):

        if node.child is not None:
            self.__leaf_search__(node.child, amount + 1 + node.last_index() - node.first_index())
        else:
            self.output.append(self.end - (amount + node.last_index() - node.first_index()))

        if node.sibling is not None:
            self.__leaf_search__(node.sibling, amount)