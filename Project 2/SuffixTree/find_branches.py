class find_branches():
    def __init__(self, st, c2d, d2c, hash_map):
        self.tree = st
        self.c2d = c2d
        self.d2c = d2c
        self.internal_nodes = hash_map #Contains <TrieNode, (Integer, Integer)> - the integers is the dpf interval of the internal node 
        # branching tandem repeats
        self.b_t_r = []

    def start_basic_algorithm(self):
        
        # 1. Select an unmarked internal node v
        #    Mark v and execute steps 2a and 2b for node v
        for value in self.internal_nodes.value():
            # 2a. Collect the leaf-list LL(v)
            leaf_list = ()
            # check: value[1] + 1, maybe. TODO
            for v in range(value[0], value[1]):
                # (1) this way will think its just a number inside ()
                # (1,) this way its a tupple with one number
                leaf_list = leaf_list + (self.d2c[v],)
            
            # 2c. For each i in LL(v), test whether the leaf j = i + D(v) is in LL(v)
            # If so, test whether S[i] != S[i + 2*D(v)]. There is a branching tandem repeat of
            # length 2*D(v) starting at position i if and only if both tests return true.
            for i in leaf_list:
                j = i + value[2] 
                if j in leaf_list:
                    if self.tree.string[i] != self.tree.string[ i + 2 * value[2] ]:
                        print "Branching tendem repeat found"
                        print "At index: ", i, " with length: ",  2 * value[2]
                        t = (i, value[3], 2)
                        self.b_t_r.append(t)
    
    
    
    def find_rest_of_tandem_occurrences(self): #Doing a series of consecutive left-rotations to find all occurrences of tandem repeats
        print "Finding rest of tandem occurences"
        