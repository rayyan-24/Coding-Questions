# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        arr=[]
        while True:
            if temp is None:
                break
            arr.append(temp.val)
            temp=temp.next
        arr.sort()
        temp=head
        for i in arr:
            temp.val=i
            temp=temp.next
        return head