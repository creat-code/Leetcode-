# Last updated: 11/5/2026, 9:24:28 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        current = head
        nums = []
        decimal = 0
        while current != None:
            nums.append(current.val)
            current = current.next
        power = (len(nums)-1)
        for num in nums:
            decimal += num * (2** power)
            power = power - 1
        return decimal

        