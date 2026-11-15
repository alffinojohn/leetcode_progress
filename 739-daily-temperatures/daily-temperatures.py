class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        wait = [0] * len(temperatures)
        leftover = []

        for i in range(len(temperatures)):
            while leftover and temperatures[leftover[-1]] < temperatures[i]:
                wait[leftover[-1]] = i - leftover[-1]
                leftover.pop()

            leftover.append(i)

        return wait

            

            


