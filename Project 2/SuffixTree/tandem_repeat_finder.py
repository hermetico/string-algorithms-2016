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


    def tandem_repeat_search(self, node=None, tree=None):

        if tree is not None:
            self.refill(tree)

        if node is None:
            node = self.root
            self.output = []


        ##### depth first numbering #####
        self.dfs_numbering(self.root,0)#from 1 if we want


    def dfs_numbering(self, node, number):

        if node.child is not None:
            self.dfs_numbering(node.child, number)
        else: ##this is a child
            node.dfs_number = number
            number+=1

        if node.sibling is not None:
            self.dfs_numbering(node.sibling, number)



    def __leaf_search__(self, node, amount):

        if node.child is not None:
            self.__leaf_search__(node.child, amount + 1 + node.last_index() - node.first_index())
        else:
            self.output.append(self.end - (amount + node.last_index() - node.first_index()))

        if node.sibling is not None:
            self.__leaf_search__(node.sibling, amount)