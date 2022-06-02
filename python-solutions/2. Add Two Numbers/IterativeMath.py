# Time Complexity: O(max(M,N)) where M and N are the lengths of the two linked lists
# Space Complexity: O(1) constant space solution
# iterate through both lists while updating returned linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prehead = ListNode(0)
        head = prehead
        carry = 0
        while l1 or l2 or carry:
            # get value at l1 if l1 exists
            # get next if l1.next exists
            num1 = l1.val if l1 else 0
            l1 = l1.next if l1 else None
            
            # repeat with l2
            num2 = l2.val if l2 else 0
            l2 = l2.next if l2 else None
            
            # division and modulus to extract digits
            carry, num = divmod(num1+num2+carry, 10)
            
            # update return linked list
            head.next = ListNode(num)
            head = head.next
            
        return prehead.next
