from TrieNode import TrieNode

class SuffixTree(object):
    """A fancy Suffix Tree with an amazing performance"""
    string = ""
    n = 0
    
    def __init__(self, string=None):
        self.root = None
        if string:
            self.string = string
            self.n = len(string)
            self.construct_tree(string)
        
    def construct_tree(self, string):
        self.n=len(string)
        self.root = TrieNode((0, self.n), None, None)
        for i in range (1, self.n):
            self.add_suffix(i)

            
    def add_suffix(self, start_index, node = None):
        
        #current char that we are trying to match
        c = start_index
        
        # checks if node is none, this means we are looking through the root
        if node is None:
            node = self.root
        
        # We loop through the node and its siblings to get the first 
        # node which matches the first character
        # Two things could happen:
        #   1 - There are not nodes with match the starting character -> new sibling is needed
        #   2 - There is a matching start character -> we end the wile
        #
       
        while self.string[node.indexes[0]] != self.string[c]: 
            print self.string[c]
            print self.string[node.indexes[0]+i]
            if node.sibling == None:
                node.sibling = TrieNode((c, self.n), None, None)
                return
            node = node.sibling
        
        # We loop comparing the character of the input 
        # with the character of the current node
        # we start with 1 more because we have already checked the first character
        # in the previous while
        i = 0
  
        while self.string[c] == self.string[node.indexes[0] + i]:
            print self.string[c]
            print self.string[node.indexes[0]+i]          
            # We check if this is the last character of the node
            # if that is the case, we do a recursive call with the child node
            if i == node.indexes[1] - node.indexes[0]:
                self.add_suffix(start_index + i, node.child)
                return
            i += 1
            c += 1
        
        ###################split################
        first_part = (node.indexes[0], node.indexes[0] + i-1)
        second_part = (node.indexes[0] + i, node.indexes[1])
        #third_part = (node.indexes[1] + 1, n)
        third_part = (c - 1, self.n)
        
        print str(first_part) + " " + str(second_part) + " " + str(third_part)
    
        third_node = TrieNode(third_part, None, None)
        second_node = TrieNode(second_part, node.child, third_node)
        node.indexes = first_part
        node.child = second_node
        ## here we create the new child, we modify the current node and the child, and we call suffix with the child
        
        
        

    def __str__(self):
        """Prints the suffix tree"""

        # checks if the tree is not empty
        if self.root:
            node = self.root
            output_line = [str(node.indexes)]
            while node.sibling:
                # gets the sibling
                sib = node.sibling
                # append the name to an array 
                output_line.append(str(sib.indexes))
                # gets the next sibling
                node = sib
            print '-->'.join(output_line)
                
        else:
            print "Empty tree"
        
        return ''    

if __name__ == "__main__":
    # TODO
    # create the tree and give a filename and check if everything works
    pass