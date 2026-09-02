# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first, second = 0, 0

        mult = 1
        current = l1
        while current is not None:
            first += current.val * mult
            current = current.next
            mult *= 10

        mult = 1
        current = l2
        while current is not None:
            second += current.val * mult
            current = current.next
            mult *= 10

        mult = first + second
        head = ListNode((mult % 10))
        mult = mult // 10
        current = head
        while mult != 0:
            newnode = ListNode((mult % 10))
            current.next = newnode
            current = newnode
            mult = mult // 10

        return head

        