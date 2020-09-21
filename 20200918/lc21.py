# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = ListNode()
        pre = tmp
        while l1 and l2:
            if l1.val > l2.val:
                tmp.next = l2
                l2 = l2.next
            else:
                tmp.next = l1
                l1 = l1.next
            tmp = tmp.next
        if not l1:
            tmp.next = l2
        elif not l2:
            tmp.next = l1
        return pre.next


if __name__ == '__main__':
    ll3 = ListNode(4, None)
    ll2 = ListNode(2, ll3)
    ll1: ListNode = ListNode(1, ll2)

    ll6 = ListNode(4, None)
    ll5 = ListNode(3, ll6)
    ll4 = ListNode(1, ll5)

    s = Solution()
    result = s.mergeTwoLists(ll1, ll4)
    while not result:
        print(result.val)
