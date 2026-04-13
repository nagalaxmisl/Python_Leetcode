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
    def isBalanced(self, root):
        def height(node):
            if not node:
                return 0

            left = height(node.left)
            if left == -1:
                return -1

            right = height(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return height(root) != -1


if __name__ == "__main__":
    sol = Solution()

    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1:", sol.isBalanced(root1))  # True

    root2 = build_tree([1, 2, 2, 3, 3, None, None, 4, 4])
    print("Test 2:", sol.isBalanced(root2))  # False

    root3 = build_tree([])
    print("Test 3:", sol.isBalanced(root3))  # True