class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        n = self
        answer = ''
        while n:
            answer += str(n.val)
            n = n.next
        return answer


def remove_n_from_linked_list(head, val):

    while(head and head.val == val):
        head = head.next
            
    prev = head
    curr = head 
        
    while curr:
        if curr.val == val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next 
        
    return head



head = Node(6, Node(6, Node(6, Node(4, Node(5, None)))))
print head

remove_n_from_linked_list(head, 6)
print head
