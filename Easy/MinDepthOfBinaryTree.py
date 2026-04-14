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
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left:
            return 1 + self.minDepth(root.right)

        if not root.right:
            return 1 + self.minDepth(root.left)

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


if __name__ == "__main__":
    sol = Solution()

    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1:", sol.minDepth(root1))  # 2

    root2 = build_tree([2, None, 3, None, 4, None, 5, None, 6])
    print("Test 2:", sol.minDepth(root2))  # 5