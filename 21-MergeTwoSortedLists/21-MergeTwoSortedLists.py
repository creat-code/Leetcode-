# Last updated: 11/5/2026, 9:25:17 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        addlist = []
        currentNode = list1
        currentNode2 = list2
        

        while currentNode or currentNode2:
            try:
                print(currentNode.val)
                addlist.append(currentNode.val)
                currentNode = currentNode.next

            except:
                print("out of bounds")
            try:
                print(currentNode2.val)
                addlist.append(currentNode2.val)
                currentNode2 = currentNode2.next
    
            except:
                print("out of bounds")


        
            
        addlist.sort() 
        mylist = ListNode()
        current = mylist
        print(current)
        
    
        # loop through list to create nodes and link them together
        for item in addlist:
            current.next = ListNode(item)
            current = current.next
        return mylist.next
            
            
        
   
        
        
    
        