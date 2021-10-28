from collections import deque
class Node:
    def __init__(self, data):
        """
            Properties 
            =================================
            @param {any} data 
            @param {Node | None} l_child : Left child of the node 
            @param {Node | None} r_child : Right child of the node
        """
        self.data = data 
        self.l_child = None 
        self.r_child = None 

class BinaryTree:
    def __init__(self):
        self.root_node = None 

    def is_empty(self) -> bool:
        """ Checks if a binary tree is empty """
        return self.root_node == None

    # def _insert_node(self, data, node:Node) -> None:
    #     """ Inserts a new node into the binary tree """
    #     if data < node.data:
    #         if node.l_child is None:
    #             node.l_child = Node(data)
    #         else:
    #             self._insert_node(data, node.l_child)

    #     elif data > node.data:
    #         if node.r_child is None:
    #             node.r_child = Node(data)
    #         else:
    #             self._insert_node(data, node.r_child) 

    # def insert_node(self, data) -> None:
    #     if self.root_node == None:
    #         self.root_node = Node(data)
    #     else:
    #         self._insert_node(data, self.root_node)

    def print_tree(self, node:Node, level:int) -> None:
        if node == None:
            return
        self.print_tree(node.r_child, level+1)
        print(' '*4*(level+1), node.data)
        self.print_tree(node.l_child, level+1)

    def display(self) -> None:
        self.print_tree(self.root_node, 0)

    # Traversal in a binary tree
    # Tree nodes are not arranged linearly, they are hierarchical in nature. Hence, there are different ways of traversing 
    # tree nodes in a binary tree. 
    # Let N = Root node, L = Left child node, R = Right child node 
    # Traversal methods 
    # 1. Pre-order traversal - NLR (visit Root node -> traverse Left subtree of root in pre-order -> traverse Right subtree in pre-order)
    # 2. In-order traversal - LNR (traverse Left subtree of root in in-order -> visit Root node -> traverse right subtree of root in in-order)
    # 3. Post-order traversal - LRN (traverse Left subtree of root in post-order -> traverse Right subtree of root in post-order -> visit Root node)

    def _traverse_preorder(self, node:Node=None):
        """ Pre-order traversal of the tree recursively """
        traversed = []
        if node:
            traversed.append(node.data)
            # Traverse the left subtree recursively
            traversed.extend(self._traverse_preorder(node.l_child))
            # Traverse the right subtree recursively
            traversed.extend(self._traverse_preorder(node.r_child))
        return traversed

    def _traverse_inorder(self, node:Node=None):
        """ In-order traversal of the tree recursively """
        traversed = []
        if node:
            # Traverse the left subtree recursively
            traversed.extend(self._traverse_inorder(node.l_child))
            #Visit the root node 
            traversed.append(node.data)
            # Traverse the right subtree recursively 
            traversed.extend(self._traverse_inorder(node.r_child))
        return traversed

    def _traverse_postorder(self, node:Node=None):
        """ Post-order traversal of the tree recursively """
        traversed = []
        if node:
            # Traverse left subtree recursively 
            traversed.extend(self._traverse_postorder(node.l_child))
            # Traverse the right subtree recursively 
            traversed.extend(self._traverse_postorder(node.r_child))
            # Visit the root node 
            traversed.append(node.data)
        return traversed 

    def traverse_inorder(self):
        return self._traverse_inorder(self.root_node) 

    def traverse_preorder(self):
        return self._traverse_preorder(self.root_node)

    def traverse_postorder(self):
        return self._traverse_postorder(self.root_node)

    ## Level-order traversal involves traversing the tree from the root node, and moving level by level 
    ## The nodes are traversed from left to right in each level 
    ## Level order traversal is implemented using queues
    def traverse_levelorder(self):
        traversed = []
        if self.root_node == None:
            return traversed 

        q = deque()
        q.append(self.root_node)
        while len(q) > 0:
            temp = q.popleft()
            traversed.append(temp.data)
            if temp.l_child is not None:
                q.append(temp.l_child)
            if temp.r_child is not None:
                q.append(temp.r_child)
        return traversed 

    def _height(self, node:Node=None):
        if node is None:
            return -1 

        left_height = self._height(node.l_child)
        right_height = self._height(node.r_child)
        return max(left_height, right_height) + 1 

    def height(self):
        return self._height(self.root_node)

if __name__ == '__main__':
    b = BinaryTree()
    b.root_node = Node('A')
    b.root_node.l_child = Node('B')
    b.root_node.r_child = Node('G')
    b.root_node.l_child.l_child = Node('C')
    b.root_node.l_child.r_child = Node('D')
    b.root_node.l_child.l_child.l_child = Node('E')
    b.root_node.l_child.r_child.l_child = Node('J')
    b.root_node.l_child.r_child.r_child = Node('F')
    b.root_node.r_child.l_child = Node('H')
    b.root_node.r_child.r_child = Node('I')
    b.root_node.r_child.l_child.l_child = Node('J')
    b.root_node.r_child.r_child.l_child = Node('L')
    b.root_node.r_child.r_child.r_child = Node('K')
    b.root_node.r_child.r_child.r_child.r_child = Node('F')


    b.display()
    print(b.traverse_preorder())
    print(b.traverse_inorder())
    print(b.traverse_postorder())
    print(b.traverse_levelorder())
    print(b.height())