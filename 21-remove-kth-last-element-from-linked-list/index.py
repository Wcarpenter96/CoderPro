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


def remove_kth_from_linked_list(node, k):

    slow, fast = node, node

    for i in range(k):
        print(fast.val)
        fast = fast.next
    if not fast:
        return node.next

    prev = None
    while fast:
        prev = slow
        fast = fast.next
        slow = slow.next
        print(node.val, node.next.val, node.next.next.val,
              node.next.next.next.val, node.next.next.next.next.val)
    prev.next = slow.next
    print(node.val,node.next.val,node.next.next.val,node.next.next.next.val)
    return node


head = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print head

remove_kth_from_linked_list(head, 1)
print head
