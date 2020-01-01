# use heaps

import heapq

class Solution:
    def findKthLargest1(self, nums, k):
        return heapq.nlargest(k, nums)[-1]

    def findKthLargest2(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for x in range(k):
            heapq.heappop(heap)
        print(heap)
        

print(Solution().findKthLargest1([3,5,2,4,6,8], 3))