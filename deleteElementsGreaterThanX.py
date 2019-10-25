def removeElements(self, head: ListNode, val: int) -> ListNode:
    curr = head
    prev = head
    while (curr):
        if (curr.val == val):
            if (curr == head):
                head = head.next
            else:
                prev.next = curr.next

            curr = curr.next

        else:
            prev = curr
            curr = curr.next

    return head