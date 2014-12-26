# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        cur_node = ListNode(-1)
        small_node = ListNode(-1)
        cur_node.next = head
        small_node.next = head
        while small_node.next:
            while cur_node.next and cur_node.next.val < x:
                cur_node = cur_node.next
            if small_node.next == head:
                small_node = cur_node
            while small_node.next and small_node.next.val >= x:
                small_node = small_node.next
            if small_node.next:
                temp = small_node.next.next
                small_node.next.next = cur_node.next
                if cur_node.next == head:
                    head = small_node.next
                cur_node.next = small_node.next
                small_node.next = temp
            cur_node = cur_node.next
        return head


if __name__ == "__main__":
    head = ListNode(2)
    A = ListNode(1)
    B = ListNode(10)
    C = ListNode(9)
    D = ListNode(8)
    E = ListNode(7)
    head.next = A
    #A.next = B
    #B.next = C
    #C.next = D
    #D.next = E
    solution = Solution()
    x = 2
    result = solution.partition(head, x)
    while result:
        print result.val
        result = result.next
