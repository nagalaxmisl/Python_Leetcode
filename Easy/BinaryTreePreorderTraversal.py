class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []

        def dfs(node):
            if not node:
                return

            result.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return result

    def main(self):
        # Tree: [1, null, 2, 3]
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.left = TreeNode(3)

        print(self.preorderTraversal(root))

        root2 = TreeNode(1)
        print(self.preorderTraversal(root2))

        print(self.preorderTraversal(None))

if __name__ == "__main__":
    sol = Solution()
    sol.main()