from util.linkedlist import ListNode, linkerize


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode()
    pre = head
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        carry, val = divmod(carry, 10)
        pre.next = ListNode(val)
        pre = pre.next
    return head.next


l1 = linkerize([0, 1, 2, 3])
l2 = linkerize([5, 9, 7, 3, 4])
print(addTwoNumbers(l1, l2))

l1 = linkerize([2, 4, 3])
l2 = linkerize([5, 6, 4])
print(addTwoNumbers(l1, l2))
