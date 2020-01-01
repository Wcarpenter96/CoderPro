# Definition for a singly-linked list
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self):
        result = str(self.val)
        if self.next:
            result += str(self.next)
        return result

class Solution:
    # ex. head = 1,2,3,4
    def reverseList(self, head):
        # CALL STACK 1 reverseList(1)
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        # p = reverseList(2)
        head.next.next = head
        # head.next.next = 1
        head.next = None
        # head.next = None
        return p 
        # CALL STACK 2 reverseList(2)

node = ListNode(1)
node.next = ListNode(2)
node.next.next = ListNode(3)
node.next.next.next = ListNode(4)

print(Solution().reverseList(node))
# 4321