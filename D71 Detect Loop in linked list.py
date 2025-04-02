class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        a=head
        if(head.next!=None):
            b=head.next.next
        else:
            return False
        while(b!=None and b.next!=None):
            if(b==a):
                return True
            a=a.next
            b=b.next.next
        return False  
