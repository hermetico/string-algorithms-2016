class TrieNode:
    indexes = ""
    child = None
    sibling = None
    
    def __init__(self, indexes, child, sibling):
        self.indexes = indexes
        self.child = child
        self.sibling = sibling
        
    def change_indexes(self, indexes):
        self.indexes = indexes
        
    def change_child(self, child):
        self.child = child
        
    def change_sibling(self, sibling):
        self.sibling = sibling
        