class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    # Завдання 1
    def find_max(self):
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.value

    # Завдання 2
    def find_min(self):
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.value

    # Завдання 3
    def sum_tree(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return 0
        left_sum = self.sum_tree(node.left) if node.left else 0
        right_sum = self.sum_tree(node.right) if node.right else 0
        return node.value + left_sum + right_sum


bst = BST()
bst.insert(10) 
bst.insert(20)
bst.insert(5)
bst.insert(30)
bst.insert(45)
bst.insert(-70)
bst.insert(-20)

# Завдання 1
print("Max value is:", bst.find_max())

# Завдання 2
print("Min value is:", bst.find_min())

# Завдання 3
print("Sum of all values = ", bst.sum_tree())


