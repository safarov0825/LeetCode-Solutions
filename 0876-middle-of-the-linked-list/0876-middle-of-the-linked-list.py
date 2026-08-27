# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        nodes = []

        count = 0
        current = head
        while current is not None:
            count += 1
            nodes.append(current)
            current = current.next

        return nodes[count // 2]
        