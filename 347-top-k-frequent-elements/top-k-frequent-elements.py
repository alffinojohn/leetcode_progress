class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        f = defaultdict(list)

        for num, freq in count.items():
            f[freq].append(num)

        res = []

        for i in range(len(nums), -1, -1):
            if i in f:
                for val in f[i]:
                    res.append(val)
                    k -= 1
                    if k == 0:
                        return res

        