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
        """Returns the child of the given node which matches the character provided, if non of them matches
        we return the last sibling.
        The second value returned is a boolan whether the character has been found or not"""

        node = parent.child
        if node is None: return None, False
        # We loop through the node and its siblings to get the first
        # node which matches the first character
        # Two things could happen:
        #   1 - There are not nodes which match the starting character -> we return the last sibling and False
        #   2 - There is a matching start character -> we return the node and True
        while self.string[node.first_index()] != ch:
            if node.sibling is None: return node, False
            # move to the sibling to check if the first character matches
            node = node.sibling

        return node, True

    def add_suffix(self, suffix_index, node):
        """Add a suffix into the suffix tree"""
        # We search for the node which matches the first character
        node, found = self.__get_first_ch_node__(node, self.string[suffix_index])
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

    def search(self, key, node=None, key_index=0, match_sub_index=0):
        #slow crawl
        if node is None:
            node = self.root

        node,found = self.__get_first_ch_node__(node, key[key_index])

        if not found:
            return ""#False #whatever output means that the search failed


        suffix_index = node.first_index()
        while self.string[suffix_index] == key[key_index]:
            key_index += 1
            if key_index == len(key):
                print suffix_index - len(key) + 2
                return self.search(key, node, match_sub_index, match_sub_index)


            # We check if this is the last character of the node
            # if that is the case, we do a recursive call with the child node
            if suffix_index == node.last_index():
                # we need to add 1, otherwise the index would be out of bounds of the node
                ####CHECK THIS PART WHEN IT FAILS IN A MOMENT
                return self.search(key, node, key_index, key_index)


            # increase string_index and suffix_index to check the next character

            suffix_index += 1

        return


        


if __name__ == "__main__":
    # TODO
    # create the tree and give a filename and check if everything works
    pass