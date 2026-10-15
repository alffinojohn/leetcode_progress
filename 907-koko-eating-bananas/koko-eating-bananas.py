class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def findHrs(k):
            hrs = 0
            for num in piles:
                val = num // k
                if num % k != 0:
                    val += 1

                hrs += val
            return hrs

        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            if findHrs(mid) > h:
                l = mid + 1
            else: 
                r = mid

        return l
