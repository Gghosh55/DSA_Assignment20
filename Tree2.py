class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def constructBST(level_order):
    if not level_order:
        return None

    root = TreeNode(level_order[0])
    queue = [(root, float('-inf'), float('inf'))]
    index = 1

    while queue:
        node, min_val, max_val = queue.pop(0)

        if index < len(level_order):
            curr_val = level_order[index]
            index += 1

            if min_val < curr_val < node.val:
                new_node = TreeNode(curr_val)
                node.left = new_node
                queue.append((new_node, min_val, node.val))

        if index < len(level_order):
            curr_val = level_order[index]
            index += 1

            if node.val < curr_val < max_val:
                new_node = TreeNode(curr_val)
                node.right = new_node
                queue.append((new_node, node.val, max_val))

    return root


def inorderTraversal(node):
    if node is None:
        return []
    return inorderTraversal(node.left) + [node.val] + inorderTraversal(node.right)

level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]

root = constructBST(level_order)

inorder_result = inorderTraversal(root)
print("In-order Traversal Result:")
for val in inorder_result:
    print(val)
