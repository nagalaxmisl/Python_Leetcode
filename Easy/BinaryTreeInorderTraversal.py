class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            result.append(node.val)
            dfs(node.right)

        dfs(root)

        return result

    def main(self):
        # Tree: [1, null, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        print(self.inorderTraversal(root))

        root2 = TreeNode(1)
        print(self.inorderTraversal(root2))

        print(self.inorderTraversal(None))

if __name__ == "__main__":
    sol = Solution()
    sol.main()