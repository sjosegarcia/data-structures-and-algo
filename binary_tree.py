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


b_tree = BinaryTree(Node(1))
b_tree.root.left = Node(2)
b_tree.root.right = Node(3)
b_tree.root.left.left = Node(4)
b_tree.root.left.right = Node(5)
b_tree.root.right.left = Node(6)
b_tree.root.left.right = Node(7)

b_tree.print_orders()
