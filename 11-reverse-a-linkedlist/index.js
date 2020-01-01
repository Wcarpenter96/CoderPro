function ListNode(val) {
   this.val = val;
   this.next = null;
}

var reverseList = function(head) {
    if (head == null || head.next == null)
        return head
    p = reverseList(head.next)
    head.next.next = head;
    head.next = null
    return p 
};

let node = new ListNode(1)
node.next = new ListNode(2)
node.next.next = new ListNode(3)
node.next.next.next = new ListNode(4)
console.log(node)
console.log(reverseList(node))