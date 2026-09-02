# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        nodes = []
        current = head

        while current is not None:
            nodes.append(current)
            current = current.next

        if len(nodes) == 1:
            head = None
        elif n == len(nodes):
            return head.next
        elif n == 1:
            nodes[-2].next = None
        else:
            nodes[-(n+1)].next = nodes[-(n-1)]

        return head
        