class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
            
        nodeMap = {}
        curr = head
        
        while curr:
            nodeMap[curr] = Node(curr.data)
            curr = curr.next
        curr = head
        
        while curr:
            nodeMap[curr].next = nodeMap.get(curr.next)
            nodeMap[curr].random = nodeMap.get(curr.random)
            curr = curr.next
            
        return nodeMap[head]
