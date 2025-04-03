class Solution:
    def findFirstNode(self, head):
        #code here
        slow,fast=head,head
        while fast and fast.next:
            slow,fast=slow.next,fast.next.next
            if slow==fast:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            slow,fast=slow.next,fast.next
        return slow
