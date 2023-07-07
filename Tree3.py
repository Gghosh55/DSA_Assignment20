def isLevelOrderBST(arr):
    if not arr:
        return True

    n = len(arr)
    index = 1

    while index < n:
        parent_index = (index - 1) // 2

        if arr[index] > arr[parent_index]:
            return False

        index += 1

    return True

level_order = [7, 4, 12, 3, 6, 8, 1, 5, 10]
print("Can Represent BST:",isLevelOrderBST(level_order))
