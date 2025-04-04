'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''

class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        mp={}
        cur=head
        prev=None
        while cur:
            if cur in mp:
                prev.next=None
                break
            mp[cur]=True
            prev,cur=cur,cur.next
        
