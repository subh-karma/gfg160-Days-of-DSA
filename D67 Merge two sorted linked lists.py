class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        if head1 is None:
            return head2
        if head2 is None:
            return head1
        
        ptr1 = head1
        ptr2 = head2
        new_head = None
        prev = None
        while ptr1 and ptr2:
            if ptr1.data < ptr2.data:
                if new_head is None:
                    new_head = ptr1
                else:
                    prev.next = ptr1
                prev = ptr1
                ptr1 = ptr1.next
            else:
                if new_head is None:
                    new_head = ptr2
                else:
                    prev.next = ptr2
                prev = ptr2
                ptr2 = ptr2.next
        while ptr1:
            prev.next = ptr1
            prev = ptr1
            ptr1 = ptr1.next
        while ptr2:
            prev.next = ptr2
            prev = ptr2
            ptr2 = ptr2.next
        return new_head
