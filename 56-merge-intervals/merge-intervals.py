class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new_intervals = sorted(intervals, key = lambda x: x[0])
        res = [new_intervals[0]]

        for i in range( 1, len(new_intervals)):
            interval = new_intervals[i]

            if interval[0] <= res[-1][1]:
                res[-1][1] = max(interval[1], res[-1][1])
            else:
                res.append(interval)


        return res

            




            

        

        


