class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def hrs(k):
            total = 0
            for pile in piles:
                total += pile // k
                if pile % k != 0:
                    total += 1

            return total

        l = 1
        r = max(piles)

        while l <= r:
            mid = (l+r) // 2
            if hrs(mid) > h:
                l = mid + 1
            else:
                r = mid - 1

        return l

        