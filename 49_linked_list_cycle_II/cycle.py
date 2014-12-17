# Given a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        node_set = set()
        while head:
            if head in node_set:
                return head
            else:
                node_set.add(head)
            head = head.next
        else:
            return None

if __name__ == "__main__":
    A = ListNode(1)
    B = ListNode(2)
    C = ListNode(3)
    solution = Solution()
    A.next = B
    B.next = C
    C.next = B
    print solution.detectCycle(A).val
    print A.val
