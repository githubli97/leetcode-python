// Definition for singly-linked list.
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}
class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode slow = head;
        ListNode quick = head;
        do {
            if (quick == null ||quick.next == null) {
                return null;
            }
            quick = quick.next.next;
            slow = slow.next;
        } while (slow != quick);

        quick = head;
        while (slow != quick) {
            quick = quick.next;
            slow = slow.next;
        }
        return quick;
    }
}