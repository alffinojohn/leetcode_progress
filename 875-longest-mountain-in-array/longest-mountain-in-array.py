class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        length = 0
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                l = i - 1
                r = i + 1
                while l > 0 and arr[l] > arr[l-1]:
                    l -= 1

                while r < len(arr)-1 and arr[r] > arr[r+1]:
                    r += 1

                newLen = r - l+1
                length = max(length, newLen)

        return length





        