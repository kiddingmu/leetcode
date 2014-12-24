# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        fast = slow = ListNode(0)
        fast.next = head
        slow.next = head
        count = 0 
        while fast.next:
            if count < n:
                print count
                fast = fast.next
                count += 1
                continue
            slow = slow.next
            fast = fast.next
        if slow.next == head:
            head = slow.next.next
        elif slow.next:
            slow.next = slow.next.next
        return head

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    #d = ListNode(4)
    #e = ListNode(5)
    a.next = b
    b.next = c
    #c.next = d
    #d.next = e
    solution = Solution()
    n = 1
    head_removed = solution.removeNthFromEnd(a, n)
    print "*****"*10, head_removed
    while head_removed:
        print head_removed.val
        head_removed = head_removed.next
