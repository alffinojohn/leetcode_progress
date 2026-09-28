class Solution:
    def longestMountain(self, arr: list[int]) -> int:
        length = 0
        i = 0

        while i < len(arr) -1:
            if arr[i] < arr[i+1]:
                start = i
                while i < len(arr) -1 and arr[i] < arr[i+1]:
                    i +=1

                if i < len(arr) - 1 and arr[i] > arr[i+1]:
                    while i < len(arr)-1 and arr[i] > arr[i+1]:
                        i += 1

                    length = max(length, i-start+1)

            else:
                i += 1

        return length

            
        