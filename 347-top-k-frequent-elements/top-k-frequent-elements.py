class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums) # 1: 3, 2: 2, 3: 1
        freq = [[] for _ in range(len(nums)+1)]

        for num, f in counts.items():
            freq[f].append(num)

        res = []

        for i in range(len(nums), -1,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res




        