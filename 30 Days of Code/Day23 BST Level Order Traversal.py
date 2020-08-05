def levelOrder(self, root):
    from collections import deque
    # Write your code here
    if not root:
        return root
    queue = deque([root])

    while queue:
        temp = queue.popleft()
        print(temp.data, end=' ')

        if temp.left:
            queue.append(temp.left)

        if temp.right:
            queue.append(temp.right)
