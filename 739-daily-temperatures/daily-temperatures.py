class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures), 1):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                num = stack.pop()
                res[num] = i - num

            stack.append(i)

        return res






