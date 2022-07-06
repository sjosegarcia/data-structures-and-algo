class Node:

    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:

    def __init__(self, root: Node) -> None:
        self.root = root
    
    def preorder_traversal(self, node: Node, traversal: str) -> str:
        if not node:
            return traversal
        
        traversal += f'{node.value}-'
        traversal = self.preorder_traversal(node.left, traversal)
        traversal = self.preorder_traversal(node.right, traversal)
        return traversal

    def inorder_traversal(self, node: Node, traversal: str) -> str:
        if not node:
            return traversal
        
        traversal = self.inorder_traversal(node.left, traversal)
        traversal += f'{node.value}-'
        traversal = self.inorder_traversal(node.right, traversal)
        return traversal

    def postorder_traversal(self, node: Node, traversal: str) -> str:
        if not node:
            return traversal
        
        traversal = self.postorder_traversal(node.left, traversal)
        traversal = self.postorder_traversal(node.right, traversal)
        traversal += f'{node.value}-'
        return traversal

    def print_orders(self) -> None:
        print(f'preorder: {self.preorder_traversal(self.root, "")}')
        print(f'inorder: {self.inorder_traversal(self.root, "")}')
        print(f'postorder: {self.postorder_traversal(self.root, "")}')

    
    def search(self, node: Node, search: int) -> bool:
        if node.value == search:
            return True
        if node.value > search and node.left:
            return self.search(node.left, search)
        if node.value < search and node.right:
            return self.search(node.right, search)
        return False

    def insert(self, node: Node, value: int) -> None:
        if not self.root:
            self.root = node
            return
        if node.value > value:
            if not node.left:
                node.left = Node(value)
                return
            else:
                self.insert(node.left, value)
        elif node.value < value:
            if not node.right:
                node.right = Node(value)
                return
            else:
                self.insert(node.right, value)
        else:
            print('Node exist')

    def height(self, node: Node) -> int:
        if not node:
            return -1
        
        left = self.height(node.left)
        right = self.height(node.right)

        return 1 + max(left, right)

b_tree = BinaryTree(Node(1))
b_tree.root.left = Node(2)
b_tree.root.right = Node(3)
b_tree.root.left.left = Node(4)
b_tree.root.left.right = Node(5)
b_tree.root.right.left = Node(6)
b_tree.root.right.right = Node(7)

'''
            1
        /        \
       2          3
      / \        / \ 
     4   5      6   7
'''

b_tree.print_orders()

print(f'search: {b_tree.search(b_tree.root, 7)}')
print(f'insert: {b_tree.insert(b_tree.root, 8)}')
b_tree.print_orders()
print(f'height: {b_tree.height(b_tree.root)}')