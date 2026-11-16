import heapq
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        elements = []

        for num in nums:
            heapq.heappush(elements, num)
            if len(elements) > k:
                heapq.heappop(elements)


        return elements[0]
        