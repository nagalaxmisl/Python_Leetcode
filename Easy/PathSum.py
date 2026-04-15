from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        if not root.left and not root.right:
            return targetSum == root.val

        remaining = targetSum - root.val

        return self.hasPathSum(root.left, remaining) or self.hasPathSum(root.right, remaining)


if __name__ == "__main__":
    sol = Solution()

    root1 = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])
    print("Test 1:", sol.hasPathSum(root1, 22))  # True

    root2 = build_tree([1, 2, 3])
    print("Test 2:", sol.hasPathSum(root2, 5))  # False

    root3 = build_tree([])
    print("Test 3:", sol.hasPathSum(root3, 0))  # False