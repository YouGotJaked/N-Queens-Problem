class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def add_node(self, val):
        # if root is empty
        if (self.root is None):
            self.root = Node(val)
        else:
            self._add_node(val, self.root)

    def _add_node(self, val, node):
        if (val < node.value):
            if (node.left is not None):
                self._add_node(val, node.left)
            else:
                node.left = Node(val)
        else:
            if (node.right is not None):
                self._add_node(val, node.right)
            else:
                node.right = Node(val)

    def dfs(self):
        if self.root is None:
            return ()
        stack, vistied = [self.root], []
        while stack:
            node = stack.pop()
            visited.append(node)
            # append right first so left will pop first
            stack.extend(filter(None, [node.right, node.left]))
        return tuple(visited)

def main():
    root = Tree()
    

main()
