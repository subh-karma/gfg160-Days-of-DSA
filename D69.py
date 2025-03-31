class Solution:
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        
    def addTwoLists(self, num1, num2):
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        dummy = Node(0)
        tail = dummy
        carry = 0
        
        while num1 or num2 or carry:
            summ = carry
            if num1:
                summ += num1.data
                num1 = num1.next
            if num2:
                summ += num2.data
                num2 = num2.next
            carry = summ // 10
            tail.next = Node(summ % 10)
            tail = tail.next
        res = self.reverse(dummy.next)
        while res and res.data == 0 and res.next:
            res = res.next
        return res
        
