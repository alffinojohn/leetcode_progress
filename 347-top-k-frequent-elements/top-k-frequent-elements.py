class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        newCount = defaultdict(list)

        for num, freq in counter.items():
            newCount[freq].append(num)
        
        res = []

        for i in range(len(nums), -1, -1):
            if i in newCount:
                for val in newCount[i]:
                    res.append(val)
                    k -= 1
                    if k == 0:
                        return res





        