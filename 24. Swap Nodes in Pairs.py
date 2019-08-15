# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        if head == None:
            return None

        head.next, head.next.next = head.next.next, head

        head.next.next = self.swapPairs(head.next.next)

        return head
