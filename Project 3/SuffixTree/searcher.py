
class SuffixTreeSearcher():
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

    def search(self, key, node=None, key_index=0, tree=None):
        self.__search__(key, node, key_index, tree)
        return self.output

    def __search__(self, key, node=None, key_index=0, tree=None):

        if tree is not None:
            self.refill(tree)

        if node is None:
            node = self.root
            self.output = []

        node, found = self.tree.__get_first_ch_node__(node, key[key_index])

        if not found:
            return ""  # False #whatever output means that the search failed

        suffix_index = node.first_index()
        while self.string[suffix_index] == key[key_index]:
            key_index += 1
            if key_index == len(key):
                # print suffix_index - len(key) + 2
                if node.child is not None:
                    if suffix_index != node.last_index():
                        self.__leaf_search__(node.child, len(key) + (node.last_index() - suffix_index))
                    else:
                        self.__leaf_search__(node.child, len(key))
                else:
                    self.output.append(suffix_index - len(key) + 1)

                #print ' '.join([str(x + 1) for x in sorted(self.output)])
                return

            # We check if this is the last character of the node
            # if that is the case, we do a recursive call with the child node
            if suffix_index == node.last_index():
                # we need to add 1, otherwise the index would be out of bounds of the node
                return self.search(key, node, key_index)

            # increase string_index and suffix_index to check the next character

            suffix_index += 1

        return

    def __leaf_search__(self, node, amount):

        if node.child is not None:
            self.__leaf_search__(node.child, amount + 1 + node.last_index() - node.first_index())
        else:
            self.output.append(self.end - (amount + node.last_index() - node.first_index()))

        if node.sibling is not None:
            self.__leaf_search__(node.sibling, amount)