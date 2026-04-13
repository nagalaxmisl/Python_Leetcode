from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build tree from list
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
    def maxDepth(self, root):
        if not root:
            return 0

        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return 1 + max(left_depth, right_depth)

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    root1 = build_tree([3, 9, 20, None, None, 15, 7])
    print("Test 1:", sol.maxDepth(root1))  # Expected: 3

    # Test Case 2
    root2 = build_tree([1, None, 2])
    print("Test 2:", sol.maxDepth(root2))  # Expected: 2