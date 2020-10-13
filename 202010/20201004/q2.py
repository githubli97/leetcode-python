# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result, remainder = ListNode(), 0
        pre = result
        while l1 or l2:
            if l1:
                remainder += l1.val
                l1 = l1.next
            if l2:
                remainder += l2.val
                l2 = l2.next
            tmp = ListNode()
            tmp.val = remainder % 10
            remainder //= 10
            pre.next = tmp
            pre = pre.next
        if remainder != 0:
            tmp = ListNode()
            tmp.val = remainder % 10
            remainder //= 10
            pre.next = tmp
        return result.next

if __name__ == '__main__':
    l3 = ListNode(3)
    l4 = ListNode(4, l3)
    l2 = ListNode(2, l4)

    l1 = ListNode(1)
    l6 = ListNode(6, l1)
    l5 = ListNode(5, l6)

    print(Solution().addTwoNumbers(l2, l5))