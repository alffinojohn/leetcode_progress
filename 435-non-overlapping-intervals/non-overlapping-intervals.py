class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        remove = 0

        intervals.sort()
        res = [intervals[0]]

        for i in range(1, len(intervals), 1):
            if res[-1][1] > intervals[i][0]:
                remove += 1

                if intervals[i][1] < res[-1][1]:
                    res[-1] = intervals[i]

            else:
                res.append(intervals[i])

        return remove

            


            



        


        