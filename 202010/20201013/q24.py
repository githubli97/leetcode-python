# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        headNode = ListNode()
        headNode.next = head

        pre = head
        next = head.next
        result = next
        while pre and next:
            headNode.next = next
            pre.next, next.next, headNode = next.next, pre, next

            headNode = pre
            pre = pre.next
            if pre:
                next = pre.next
            else:
                break
        return result
if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)

    l1.next = l2
    l2.next = l3
    l3.next = l4

    Solution().swapPairs(l1)