class Solution:
    def reverseList(self, head):
        temp = head
        tail = None
        
        while temp != None:
            nextNode = temp.next
            temp.next = tail
            tail = temp
            temp = nextNode
        
        return tail    
