package main

//Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	result := head
	for nil != head {
		if head.Next != nil && head.Next.Val == head.Val {
			head.Next = head.Next.Next
		} else {
			head = head.Next
		}
	}
	return result
}
