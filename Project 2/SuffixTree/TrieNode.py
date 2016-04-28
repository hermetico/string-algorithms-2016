class TrieNode(object):
    """A suffix tree node representation"""
    # we use slots to optimize the space consumption, adding each value we are going to use
    __slots__ = ('first_index', 'last_index', 'child', 'sibling', 'construction_number',
                 'dfs_number', 'marked', 'interval_start', 'interval_end')

    def __init__(self, first_index=None, last_index=None, child=None, sibling=None,
                 construction_number=None, dfs_number=None, interval_s=None, interval_e=None):
        self.last_index = last_index
        self.first_index = first_index
        self.child = child
        self.sibling = sibling
        self.interval_start = interval_s
        self.interval_end = interval_e

        self.construction_number = construction_number
        self.dfs_number = dfs_number
        self.marked = False





