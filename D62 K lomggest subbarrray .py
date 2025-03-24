class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_length = 0
        hash_map = {}  # To store the first occurrence of each prefix_sum

        for i in range(len(arr)):
            prefix_sum += arr[i]

            # Check if the whole array till this point has the required sum
            if prefix_sum == k:
                max_length = i + 1

            # Check if prefix_sum - k exists in the hash_map
            if (prefix_sum - k) in hash_map:
                max_length = max(max_length, i - hash_map[prefix_sum - k])

            # Store the first occurrence of each prefix_sum
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = i

        return max_length
    
