class TrieNode:
    """A suffix tree node representation"""
    def __init__(self, indexes = "", child = None, sibling = None):
        self.indexes = indexes
        self.child = child
        self.sibling = sibling
        self.suffix_start = 0

    def first_index(self):
        return self.indexes[0]

    def last_index(self):
        return self.indexes[1]


