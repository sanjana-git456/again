class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# build tree:
#        3
#       / \
#      9   20
#         /  \
#        15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

def depth(root):
    if root is None:
        return 0
    leftdepth = depth(root.left)
    rightdepth = depth(root.right)
    return 1 + max(leftdepth, rightdepth)

print(depth(root))