def getHeight(self, root):
    # Write your code here
    def helper(root):
        if not root:
            return 0

        return 1 + max(helper(root.left), helper(root.right))

    return helper(root) - 1
