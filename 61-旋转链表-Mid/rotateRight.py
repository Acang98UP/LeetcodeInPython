class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        # 链表整体右移k个单位
        length = 0
        point = head
        # 首先获取长度
        while point:
            length += 1
            point = point.next
        k %= length
        if k == 0:
            return head
        # 分为快慢指针
        fast, slow = head, head
        while k:
            fast = fast.next
            k -= 1
        # 直接让fast指向最后一位，在收尾的时候就可以直接把头指针放进去就行
        while fast.next:
            fast = fast.next
            slow = slow.next
        newHead = slow.next
        slow.next = None
        fast.next = head
        return newHead

