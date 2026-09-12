class Node:
    def __init__(self, val):
        self.val = val
        self.next= None
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(8)

def merge(head1,head2):
    dummy = Node(0)
    tail = dummy
    while head1 and head2:
        if head1.val < head2.val:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next
    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return dummy.next
print(merge(head1,head2))