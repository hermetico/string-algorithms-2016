TRACE = False

class find_branches():
    def __init__(self, st, c2d, d2c, hash_map):
        self.tree = st
        self.c2d = c2d
        self.d2c = d2c
        self.internal_nodes = hash_map
        #Contains <TrieNode, (Integer, Integer)> - the integers is the dpf interval of the internal node
        #^^It also contains depth of node. --Martin

        # branching tandem repeats
        self.b_t_r = []

    def start_basic_algorithm(self):
        
        # 1. Select an unmarked internal node v
        #    Mark v and execute steps 2a and 2b for node v
        for value in self.internal_nodes.values():
            #print "TEST " + str(value)
            # 2a. Collect the leaf-list LL(v)
            leaf_list = ()
            if TRACE:
                print "\nSearching in node DFS: (%i, %i) "%(value[0] + 1, value[1] + 1)
            # check: value[1] + 1, maybe. TODO
            for v in range(value[0], value[1] +1):
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
                        print "\tBranching tendem repeat found"
                        print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], 2)
                        self.b_t_r.append(t)
    
    
    def start_optimized_basic_algorithm(self):

        for node, value in self.internal_nodes.items():
            # 2a. Collect the leaf-list LL(v) and LL'(v)
            leaf_list = ()      # LL(v)
            total_leaf_list = ()  # LL'(v)
            max_leaf_list = ()
            
            if node.child not in self.internal_nodes:
                # here the max_leaf_list is the construction number of the first child
                max_leaf_list = (self.d2c[node.child.construction_number],)

            else:
                child = node.child
                intervals = self.internal_nodes[child]
                maxInterval = (intervals[0], intervals[1])   
        

                sibling = child.sibling
                while sibling is not None :
                    # check if sibling is a leaf
                    if sibling not in self.internal_nodes:
                        # there won't be more siblings that are not 
                        # check break
                        sibling = sibling.sibling
                        continue
                    
                    sibling_intervals = self.internal_nodes[sibling]
                    potentialInterval = (sibling_intervals[0], sibling_intervals[1])
                    
                    if TRACE:
                        print "\tnext Sibling interval DFS: (%i, %i) "%(potentialInterval[0] + 1, potentialInterval[1] + 1)
                        
                    #print "maxInterval: ", maxInterval
                    #print "potentialInterval: ", potentialInterval
                        
                    if (potentialInterval[1] - potentialInterval[0]) > (maxInterval[1] - maxInterval[0]):
                        maxInterval = potentialInterval
                    
                    # moves to the next sibling
                    sibling = sibling.sibling

            if TRACE:
                print "\nSearching in node DFS: (%i, %i) "%(value[0] + 1, value[1] + 1)
            if TRACE:
                print "\tFirst sibling interval DFS: (%i, %i) "%(maxInterval[0] + 1, maxInterval[1] + 1)

            # check: value[1] + 1, maybe. TODO
            for v in range(value[0], value[1] + 1):
                # (1) this way will think its just a number inside ()
                # (1,) this way its a tupple with one number
                # we check if v is outside the interval
                if(v < maxInterval[0] or v > maxInterval[1]):
                    leaf_list += (self.d2c[v],)
                elif (maxInterval[0] == maxInterval[1]):
                    if v == value[0]:
                        max_leaf_list += (self.d2c[v],)
                    else:
                        leaf_list += (self.d2c[v],)
                else:
                    max_leaf_list += (self.d2c[v],)
                
                total_leaf_list += (self.d2c[v],)
                
            if TRACE:    
                print "\tLL'(v): ", leaf_list
                print "\tLL(v'): ", max_leaf_list
                print "\tLL(v): ", total_leaf_list
            """
            #2b.
            for i in leaf_list:
                j = i + value[2]
                if j in total_leaf_list:
                    if self.tree.string[i] != self.tree.string[ i + 2 * value[2] ]:
                        print "\tBranching tendem repeat found"
                        print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], 2)
                        self.b_t_r.append(t)
            #2c.
            for j in leaf_list:
                i = j - value[2]
                if i in max_leaf_list:
                    if self.tree.string[i] != self.tree.string[ i + 2 * value[2] ]:
                        print "\tBranching tendem repeat found"
                        print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], 2)
                        self.b_t_r.append(t)
                        
            """    
            #2b.
            for i in leaf_list:
                if i+value[2] in total_leaf_list:
                    if self.tree.string[i] != self.tree.string[i + 2 * value[2]]:
                        print "\tBranching tendem repeat found"
                        print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], 2)
                        self.b_t_r.append(t)
                elif i-value[2] in max_leaf_list:
                    if self.tree.string[i-value[2] != self.tree.string[i + value[2]]]:
                        print "\tBranching tendem repeat found"
                        print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], 2)
                        self.b_t_r.append(t)
                       
                    
            
    def find_rest_of_tandem_occurrences(self): #Doing a series of consecutive left-rotations to find all occurrences of tandem repeats
        print "Finding rest of tandem occurences"
        