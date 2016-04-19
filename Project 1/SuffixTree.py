from TrieNode import TrieNode

class SuffixTree(object):
    """A fancy Suffix Tree with an amazing performance"""

    def __init__(self, string=None, end_key='$'):
        self.root = TrieNode((-1, -1), None, None)
        self.end_key = end_key
        self.string = ''
        self.end = 0

        if string:
            self.construct_tree(string)


        
    def construct_tree(self, string):

        self.string = string + self.end_key
        self.end = len(self.string) - 1

        # starts with an empty root, which first child will be the whole string
        # (week:1 slide:81)
        self.root.child = TrieNode((0, self.end), None, None)
        for i in range (1, self.end + 1):
            self.add_suffix(i, self.root)


    def __get_first_ch_node__(self, parent, ch):
        node = parent.child
        # We loop through the node and its siblings to get the first
        # node which matches the first character
        # Two things could happen:
        #   1 - There are not nodes which match the starting character -> new sibling is needed
        #       and return from the function
        #   2 - There is a matching start character -> we end the while
        while self.string[node.first_index()] != ch:
            if node.sibling is None: return node, False
            # move to the sibling to check if the first character matches
            node = node.sibling

        return node, True

    def add_suffix(self, start_index, node):
        
        # current char that we are trying to match
        suffix_index = start_index
        """
        # We loop through the node and its siblings to get the first 
        # node which matches the first character
        # Two things could happen:
        #   1 - There are not nodes which match the starting character -> new sibling is needed
        #       and return from the function
        #   2 - There is a matching start character -> we end the while
        while self.string[node.first_index()] != self.string[suffix_index]:
            if node.sibling is None:
                node.sibling = TrieNode((suffix_index, self.end), None, None)
                return

            # move to the sibling to check if the first character matches
            node = node.sibling
        """
        ########
        node, found = self.__get_first_ch_node__(node, self.string[start_index])
        if not found:
            node.sibling = TrieNode((suffix_index, self.end), None, None)
            return


        
        # We loop comparing the characters of the input
        # with the characters of the current node
        string_index = node.first_index()
        while self.string[suffix_index] == self.string[string_index]:

            # We check if this is the last character of the node
            # if that is the case, we do a recursive call with the child node
            if string_index == node.last_index():
                # we need to add 1, otherwise the index would be out of bounds of the node
                self.add_suffix(suffix_index + 1, node)
                return
            # increase string_index and suffix_index to check the next character
            string_index += 1
            suffix_index += 1

        # Expands the current node
        node = self.expand_node(node, string_index)

        # Now, we create the third node, which will be the sibling of the child of the current node
        new_sibling = TrieNode((suffix_index, self.end), None, None)
        node.child.sibling = new_sibling

        """
        The old way to check and compare

        ###################split################
        first_part = (node.first_index(), node.first_index() + i-1)
        second_part = (node.first_index() + i, node.last_index())
        third_part = (start_index + i, self.end)
        
        
        #print "C: " + str(c) + " I: " + str(i)
        #print str(first_part) + " " + str(second_part) + " " + str(third_part)
    
        third_node = TrieNode(third_part, None, None)
        second_node = TrieNode(second_part, node.child, third_node)
        node.indexes = first_part
        node.child = second_node
        ## here we create the new child, we modify the current node and the child, and we call suffix with the child
        """

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

        main_node_indexes = (node.first_index(), split_index - 1)
        new_node_indexes = (split_index, node.last_index())


        new_node = TrieNode(new_node_indexes, node.child)
        node.indexes = main_node_indexes
        node.child = new_node

        return node

        


if __name__ == "__main__":
    # TODO
    # create the tree and give a filename and check if everything works
    pass