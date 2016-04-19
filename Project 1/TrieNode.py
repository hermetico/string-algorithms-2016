class TrieNode:
    """A suffix tree node representation"""
    def __init__(self, indexes = "", child = None, sibling = None, leaf_number=''):
        self.indexes = indexes
        self.child = child
        self.sibling = sibling
        self.leaf_number = leaf_number

    def first_index(self):
        return self.indexes[0]

    def last_index(self):
        return self.indexes[1]


