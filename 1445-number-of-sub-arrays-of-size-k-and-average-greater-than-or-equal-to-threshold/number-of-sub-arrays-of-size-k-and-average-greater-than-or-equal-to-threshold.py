class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        subs = 0
        total = 0

        for i in range(k):
            total += arr[i]
        avg = total/k
        if avg >= threshold:
            subs += 1

        
        for i in range(k, len(arr)):
            total -= arr[i-k]
            total += arr[i]
            avg = total /k
            if avg >= threshold:
                subs += 1

        return subs
        