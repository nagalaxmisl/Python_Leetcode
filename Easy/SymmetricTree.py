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
    def isSymmetric(self, root):
        def isMirror(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val != right.val:
                return False

            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

        return isMirror(root.left, root.right)


if __name__ == "__main__":
    sol = Solution()

    # Test 1
    root1 = build_tree([1, 2, 2, 3, 4, 4, 3])
    print("Test 1:", sol.isSymmetric(root1))  # True

    # Test 2
    root2 = build_tree([1, 2, 2, None, 3, None, 3])
    print("Test 2:", sol.isSymmetric(root2))  # False