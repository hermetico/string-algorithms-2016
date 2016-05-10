TRACE = False
SHOWTANDEMS = False

class TandemFinder():
    def __init__(self, st, dfs_preproces):
        self.tree = st
        self.c2d = dfs_preproces.c2dmap
        self.d2c = dfs_preproces.d2cmap
        self.internal_nodes = dfs_preproces.internal_nodes
        #Contains <TrieNode, (Integer, Integer)> - the integers is the dpf interval of the internal node
        #^^It also contains depth of node. --Martin
        self.repeats = 2
        self.reset()

    def reset(self):
        # branching tandem repeats
        self.b_t_r = []
        # non branching tandem repeats
        self.nb_t_r = []
        self.br_longer  = 0
        self.nbr_longer = 0
        self.longest_chain = {'init': 0, 'len': 0, 'end': 0}
        self.average_left_rot = 0


    def run(self, method='basic'):
        if method == 'basic':
            return self.basic()
        elif method == 'optimized':
            return self.optimized()

    def basic(self):
        """Runs the optimized algorithm and the left rotation"""
        self.reset()
        self.__start_basic_algorithm__()
        self.__left_rotation__()

        return {'b-t-r': self.b_t_r, 'non-b-t-r': self.nb_t_r}

    def optimized(self):
        """Runs the optimized algorithm and the left rotation"""
        self.reset()
        self.__start_optimized_basic_algorithm__()
        self.__left_rotation__()

        return {'b-t-r': self.b_t_r, 'non-b-t-r': self.nb_t_r}


    def __start_basic_algorithm__(self):
        
        # 1. Select an unmarked internal node v
        #    Mark v and execute steps 2a and 2b for node v
        for value in self.internal_nodes.values():
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
                    if self.tree.string[i] != self.tree.string[ i + self.repeats * value[2] ]:
                        if SHOWTANDEMS:
                            print "\tBranching tendem repeat found"
                            print "\tAt index: ", i, " with length: ", value[2]
                        ##make verbose maybe
                        #print "Branching tendem repeat found"
                        #print "At index: ", i, " with length: ", value[2]
                        t = (i, value[2], self.repeats)
                        self.b_t_r.append(t)


    def __start_optimized_basic_algorithm__(self):

        for node, value in self.internal_nodes.items():
            # 2a. Collect the leaf-list LL(v) and LL'(v)
            leaf_list = ()      # LL(v)
            total_leaf_list = ()  # LL'(v)
            max_leaf_list = ()
            
            if node.child not in self.internal_nodes:
                # here the max_leaf_list is the construction number of the first child
                # max_leaf_list = (self.d2c[node.child.construction_number],)
                maxInterval = (node.child.construction_number, node.child.construction_number)
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

                    if (potentialInterval[1] - potentialInterval[0]) > (maxInterval[1] - maxInterval[0]):
                        maxInterval = potentialInterval
                    
                    # moves to the next sibling
                    sibling = sibling.sibling

            if TRACE:
                print "\nSearching in node DFS: (%i, %i) "%(value[0] + 1, value[1] + 1)
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
             #2b.
            for i in leaf_list:
                if i + value[2] in total_leaf_list:
                    if self.tree.string[i] != self.tree.string[i + self.repeats * value[2]]:
                        if SHOWTANDEMS:
                            print "\tBranching tandem repeat found"
                            print "\tAt index: ", i, " with length: ", value[2]
                        t = (i, value[2], self.repeats)
                        self.b_t_r.append(t)
                        if value[2] >= 5:
                            self.br_longer +=1
                elif i-value[2] in max_leaf_list:
                    if self.tree.string[i-value[2] != self.tree.string[i + value[2]]]:
                        if SHOWTANDEMS:
                            print "\tBranching tendem repeat found"
                            print "\tAt index: ", i, " with length: ", value[2]
                        t = (i - value[2], value[2], self.repeats)
                        self.b_t_r.append(t)
                        if value[2] >= 5:
                            self.br_longer += 1


    def __left_rotation__(self):

        for ind, length, two in self.b_t_r:
            i = 1
            chain = 0
            while self.tree.string[ind - i] == self.tree.string[ind + length - i]:

                self.nb_t_r.append((ind - i, length, self.repeats))
                i += 1
                chain +=1
                if length >= 5:
                    self.nbr_longer += 1

            if chain >= self.longest_chain['len']:
                self.longest_chain['len'] = chain
                self.longest_chain['init'] = ind - i
                self.longest_chain['end'] = ind