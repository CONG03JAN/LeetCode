class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_1:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        cur = ListNode(0)
        result = cur
        delta = 0
        while l1 or l2:

            x1 = 0
            x2 = 0

            if l1:
                x1 = l1.val
                l1 = l1.next
            if l2:
                x2 = l2.val
                l2 = l2.next
                
            tmp = x1 + x2 + delta 

            cur.next = ListNode(tmp % 10)
            delta = tmp // 10

            cur = cur.next

        if delta:
            cur.next = ListNode(delta)

        return result.next
       

# 改善之后
class Solution_2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        curNode = ListNode(0)
        result = curNode
        delta = 0

        while l1 and l2:
            add = l1.val + l2.val + delta
            delta = add // 10
            tmp = ListNode(add % 10)
            curNode.next = tmp
            curNode = tmp
            l1, l2 = l1.next, l2.next
        
        l = l1 if l1 else l2
        while l:
            add = l.val + delta
            delta = add // 10
            tmp = ListNode(add % 10)
            curNode.next = tmp
            curNode = tmp
            l = l.next

        if delta:
            curNode.next = ListNode(delta)
        
        return result.next

        


 