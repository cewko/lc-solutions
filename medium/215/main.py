import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i, n in enumerate(nums):
            nums[i] = -n

        heapq.heapify(nums)

        for _ in range(k - 1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)