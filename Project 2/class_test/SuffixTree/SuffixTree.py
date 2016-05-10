from TrieNode import TrieNode

class SuffixTree(object):
    """A fancy Suffix Tree with an amazing performance"""

    def __init__(self, string=None, end_key='$'):
        self.root = TrieNode(-1, -1)
        self.end_key = end_key
        self.string = ''
        self.end = 0
        self.output = []
        self.leaves = 0

        if string:
            self.construct_tree(string)


        
    def construct_tree(self, string):

        self.string = string + self.end_key
        self.end = len(self.string) - 1

        # starts with an empty root, which first child will be the whole string
        # (week:1 slide:81)
        self.root.child = TrieNode(0, self.end, construction_number=self.leaves)
        for i in range (1, self.end + 1):
            self.add_suffix(i, self.root)


    def __get_first_ch_node__(self, parent, ch):
        """Returns the child of the given node which matches the character provided, if none of them matches
        we return the last sibling.
        The second value returned is a boolean whether the character has been found or not"""

        node = parent.child
        # We loop through the node and its siblings to get the first
        # node which matches the first character
        # Two things could happen:
        #   1 - There are not nodes which match the starting character -> we return the last sibling and False
        #   2 - There is a matching start character -> we return the node and True
        while self.string[node.first_index] != ch:
            if node.sibling is None: return node, False
            # move to the sibling to check if the first character matches
            node = node.sibling

        return node, True

    def add_suffix(self, suffix_index, node):
        """Add a suffix into the suffix tree"""
        # We search for the node which matches the first character
        node, found = self.__get_first_ch_node__(node, self.string[suffix_index])
        if not found:
            self.leaves += 1
            node.sibling = TrieNode(suffix_index, self.end, construction_number=self.leaves)
            return

        # We loop comparing the characters of the input
        # with the characters of the current node
        string_index = node.first_index
        while self.string[suffix_index] == self.string[string_index]:

            # We check if this is the last character of the node
            # if that is the case, we do a recursive call with the child node
            if string_index == node.last_index:
                # we need to add 1, otherwise the index would be out of bounds of the node
                self.add_suffix(suffix_index + 1, node)
                return
            # increase string_index and suffix_index to check the next character
            string_index += 1
            suffix_index += 1

        # Expands the current node
        node = self.expand_node(node, string_index)

        # Now, we create the third node, which will be the sibling of the child of the current node
        self.leaves += 1
        new_sibling = TrieNode(suffix_index, self.end, construction_number=self.leaves)
        node.child.sibling = new_sibling



    def expand_node(self, node, split_index):
        """Expands the input node
        The expansion method works this way:
            1 - We have the main node, which contains two indexes (x, y), and we also recieve the split_point, which is at the
                point in which the main node is split
            2 - The main node is split in two:
                1: node -> (x, split_index - 1)
                2: new_node -> (split_index, y)
            3 - The new node will now be the child of the main node
            4 - If the main node previously had a child, this now will be the child of the new node

            M->CH  :  M->N->CH
            Where M is main_node, CH is child_node and N is new_node
        """
        # creates indexes for the nodes
        main_node_first = node.first_index
        main_node_last = split_index - 1

        new_node_first = split_index
        new_node_last = node.last_index

        # creates new node
        new_node = TrieNode(new_node_first, new_node_last, node.child,
                            construction_number=node.construction_number)

        # applyes indexes
        node.first_index = main_node_first
        node.last_index = main_node_last
        node.child = new_node
        node.construction_number = None

        return node



if __name__ == "__main__":
    # TODO
    # create the tree and give a filename and check if everything works
    pass