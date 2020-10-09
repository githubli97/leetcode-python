# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow and fast:
            if slow == fast:
                return True
            if fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return False
        return False

if __name__ == '__main__':
    # l3 = ListNode(3)
    # l2 = ListNode(2)
    # l0 = ListNode(0)
    # l4 = ListNode(4)
    #
    # l3.next = l2
    # l2.next = l0
    # l0.next = l4
    # l4.next = l0
    l3 = ListNode(3)

    print(Solution().hasCycle(None))
