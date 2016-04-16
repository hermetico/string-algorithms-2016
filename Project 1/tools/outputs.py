


def printSuffixTree(tree):
    from graphviz import Digraph
    root = tree.root
    string = tree.string
    dot = Digraph('SufixTree')
    visited = dict()
    queue = [root]
    parent_of = dict()
    node_name = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited[node] = str(node_name)
            dot.node(str(node_name))
            if node.sibling:
                parent = parent_of[node]
                sib = node.sibling
                while sib:
                    queue.append(sib)
                    if sib not in parent_of:
                        parent_of[sib] = parent
                    sib = sib.sibling
            if node.child:
                queue.append(node.child)
                parent_of[node.child] = node

            node_name += 1

    for node, parent in parent_of.items():
        label = ''.join([string[x] for x in range(node.indexes[0], node.indexes[1] + 1)])
        if node not in visited:
            print "node not visited", node
        if parent not in visited:
            print "parent not visited", parent
        dot.edge(visited[parent], visited[node], label)

    print dot.source
    dot.view()

