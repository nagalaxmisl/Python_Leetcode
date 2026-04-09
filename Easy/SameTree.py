class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

class Solution(object):
    def isSameTree(self, p, q):
        # Case 1: both are None
        if not p and not q:
            return True

        # Case 2: one is None
        if not p or not q:
            return False

        # Case 3: values are different
        if p.val != q.val:
            return False

        # Case 4: check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    p1 = build_tree([1, 2, 3])
    q1 = build_tree([1, 2, 3])
    print("Test 1:", sol.isSameTree(p1, q1))  # True

    # Test Case 2
    p2 = build_tree([1, 2])
    q2 = build_tree([1, None, 2])
    print("Test 2:", sol.isSameTree(p2, q2))  # False

    # Test Case 3
    p3 = build_tree([1, 2, 1])
    q3 = build_tree([1, 1, 2])
    print("Test 3:", sol.isSameTree(p3, q3))  # False
