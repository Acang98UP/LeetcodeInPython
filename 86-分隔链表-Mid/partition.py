class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def partition(head: ListNode, x: int) -> ListNode:
    dummy1 = ListNode(-1)
    dummy2 = ListNode(-1)
    p1 = dummy1
    p2 = dummy2
    while head:
        if head.val < x:
            p1.next = head
            p1 = p1.next
        else:
            p2.next = head
            p2 = p2.next
        head = head.next
    p1.next = dummy2.next
    p2.next = None
    return dummy1.next


def main():
    head = [1, 4, 3, 2, 5, 2]
    x = 3
    print(partition(head, x))


if __name__ == '__main__':
    main()