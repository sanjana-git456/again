class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(7)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

def invert(root):
    if root is None:
        return 0
    invert(root.left)
    invert(root.right)
    root.left, root.right = root.right, root.left
    return root
print(invert(root))