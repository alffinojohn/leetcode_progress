class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
            sorted_nums = sorted(intervals, key= lambda x : x[0])

            res = []
            res.append(sorted_nums[0])


            for i in range(1, len(sorted_nums)):
                interval = sorted_nums[i]

                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(interval[1], res[-1][1])
                else:
                    res.append(interval)

            return res

            

        

        


