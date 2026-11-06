class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        output = [0] * len(temperatures)
        
        for i in range(len(temperatures)):

            while stk and temperatures[i] > temperatures[stk[-1]]:
                index = stk.pop()
                output[index] = i - index
                
            stk.append(i)

        return output












