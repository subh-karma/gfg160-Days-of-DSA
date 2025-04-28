import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

    # To make Node comparable in heapq
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        # Create a priority queue (min-heap)
        min_heap = []
        
        # Insert the head of each list into the heap
        for head in arr:
            if head:
                heapq.heappush(min_heap, head)
        
        # Create a dummy node to help with the merging
        dummy = Node(0)
        current = dummy
        
        # Extract nodes from the heap and build the merged list
        while min_heap:
            # Pop the smallest node from the heap
            node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            
            # If the popped node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, node.next)
        
        # Return the next of the dummy node, which is the head of the merged list
        return dummy.next
