def print_suffix_tree(tree, extra_info=dict(), format="png"):
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
            label = ""
            if node.construction_number is not None:
                label = "Cons: %i" %(node.construction_number + 1)  # +1 to avoid 0's
                label += "\\nDFS: %i" %(node.dfs_number + 1)  # +1 to avoid 0's
            if node in extra_info:

                label = "DFS: (%i, %i)"%(extra_info[node][0] + 1, extra_info[node][1] + 1)
                label += "\\nDepth: %i"%(extra_info[node][2])
            dot.node(str(node_name), label=label)

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
        label = str((node.first_index + 1, node.last_index + 1)) + ''
        label += ''.join([string[x] for x in range(node.first_index, node.last_index + 1)])
        dot.edge(visited[parent], visited[node], label.replace("\n", "\\n"))

    dot.body.append(
        'label = "\\n\\n' +
        tree.string.replace("\n", "\\n") +
        '\\n C2D: ' + str([x + 1 for x in tree.C2D]) +
        '\\n D2C: ' + str([x + 1 for x in tree.D2C]) +
        ' "'
    )
    # shows the graph in a picture (i do not think this works within the c9 ide, use pycharm or something)
    dot.render('graphs/suffix-tree', view=True)

    # returns the structure on console in case you wish to print it
    return ''#dot.source

