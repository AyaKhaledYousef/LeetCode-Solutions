# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    
        number1 = ""
        while l1 is not None:
            number1 += str(l1.val)
            l1 = l1.next
        
        number2 = ""
        while l2 is not None:
            number2 += str(l2.val)
            l2 = l2.next
            
        number1 = number1[::-1]
        number2 = number2[::-1]
        number3 = str(int(number1) + int(number2))[::-1]
    
        l3 = ListNode(number3[0])
        result = l3
        
        for i in range(1,len(number3)):
            l3.next = ListNode(number3[i])
            l3 = l3.next
        return result
    
if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print ("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))