def removeDuplicates(self, head):
    # Write your code here
    if not head:
        return None
    curr = head
    while curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
