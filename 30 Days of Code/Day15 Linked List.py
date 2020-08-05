# https://www.hackerrank.com/challenges/30-linked-list/problem

    def insert(self,head,data):
        new_node = Node(data)
        if not head:
            return new_node

        curr = head

        while curr.next:
            curr = curr.next
        curr.next = new_node

        return head

# github.com/ArutselvanManivannan
