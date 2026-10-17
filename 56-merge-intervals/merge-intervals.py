class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])
        res = [intervals[0]]

        for interval in intervals:
            if interval[0] <= res[-1][1]:
                old = res.pop()
                merged = [old[0], max(old[1], interval[1])]
                res.append(merged)
            else:
                res.append(interval)

        return res

        

        


