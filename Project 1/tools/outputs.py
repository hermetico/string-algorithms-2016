


def printSuffixTree(tree, format="png"):
    from graphviz import Digraph
    root = tree.root
    string = tree.string
    dot = Digraph('SufixTree', format=format)
    
    visited = dict()
    queue = [root]
    parent_of = dict()
    node_name = 0
   
    # main process: basically this is a bfs
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited[node] = str(node_name)
            dot.node(str(node_name))
            if node.sibling is not None:
                parent = parent_of[node]
                sib = node.sibling
                while sib is not None:
                    queue.append(sib)
                    if sib not in parent_of:
                        parent_of[sib] = parent
                    sib = sib.sibling
            if node.child is not None:
                queue.append(node.child)
                parent_of[node.child] = node

            node_name += 1

    # post process: add labels and edges to te graph
    for node, parent in parent_of.items():
        label = str((node.first_index() + 1, node.last_index()+1)) + ''
        label += ''.join([string[x] for x in range(node.indexes[0], node.indexes[1] + 1)])
        dot.edge(visited[parent], visited[node], label.replace("\n", "\\n"))

    dot.body.append('label = "\\n\\n' + tree.string.replace("\n", "\\n") + '\\n"')
    # shows the graph in a picture (i do not think this works within the c9 ide, use pycharm or something)
    dot.render('graphs/suffix-tree', view=True)

    # returns the structure on console in case you wish to print it
    return dot.source


