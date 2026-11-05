# Last updated: 11/5/2026, 9:25:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = l1
        current2 = l2
        list1 = []
        list2 = []
        while current1 or current2:
            try:
               
                list1.append(current1.val)
                current1 = current1.next
              
                
            except:
                print("out")
            try:
                list2.append(current2.val)
                current2 = current2.next
            except:
                print("out2")

        print(list1, list2)

        list1.reverse()
        list2.reverse()
        
        add1 = ""
        add2 = ""
        for addend in list1:
            add1 += (str(addend))
        for addend in list2:
            add2 += (str(addend))
        sums = int(add1) + int(add2)
        print(sums)

        final_list = []
        for char in str(sums):
            final_list.insert(0, int(char))
        print(final_list)

        final_link = ListNode(0)
        current = final_link

        for item in final_list:
            current.next = ListNode(item)
            current = current.next
        return final_link.next
