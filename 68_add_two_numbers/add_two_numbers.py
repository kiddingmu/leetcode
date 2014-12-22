class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        head1 = l1
        head2 = l2
        carry = 0
        while head1 and head2:
            head1.val = head1.val + head2.val + carry
            if head1.val >= 10:
                head1.val = head1.val % 10
                carry = 1
            else:
                carry = 0
            if not head1.next or not head2.next:
                break
            head1 = head1.next
            head2 = head2.next
        if head2.next:
            head1.next = head2.next 
        if carry == 1:
            while head1.next:
                head1.next.val += carry
                if head1.next.val >= 10:
                    head1.next.val = head1.next.val % 10
                    carry = 1
                else:
                    carry = 0
                head1 = head1.next
            if carry == 1:
                head1.next = ListNode(1)
        return l1

if __name__ == "__main__":
    a1 = ListNode(9)
    b1 = ListNode(9)
    c1 = ListNode(3)
    d1 = ListNode(9)
    a1.next = b1
    #b1.next = c1
    #c1.next = d1
    a2 = ListNode(1)
    b2 = ListNode(6)
    c2 = ListNode(4)
    d2 = ListNode(9)
    #a2.next = b2
    #b2.next = c2
    #c2.next = d2
    solution = Solution()
    node = solution.addTwoNumbers(a1, a2)
    #print node
    while node:
        print node.val
        node = node.next

