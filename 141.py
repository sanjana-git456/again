class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(-4)
a.next = b
b.next = c
c.next = d
d.next = b

def cycle(head):
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
print(cycle(a))