class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxSubtreeSum(node):
    if node is None:
        return 0

    left_sum = maxSubtreeSum(node.left)
    right_sum = maxSubtreeSum(node.right)

    return left_sum + right_sum + node.val


def findMaxSubtreeSum(root):
    if root is None:
        return None

    maxSum = float('-inf')
    maxSubtree = None

    def traverse(node):
        nonlocal maxSum, maxSubtree

        if node is None:
            return

        subtree_sum = maxSubtreeSum(node)

        if subtree_sum > maxSum:
            maxSum = subtree_sum
            maxSubtree = node

        traverse(node.left)
        traverse(node.right)

    traverse(root)

    return maxSubtree



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

max_subtree = findMaxSubtreeSum(root)


print("Maximum Sum:", maxSubtreeSum(max_subtree))
print("Root Value of Maximum Subtree:", max_subtree.val)
