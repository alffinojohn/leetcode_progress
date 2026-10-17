class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)


        for word in strs:
            count = [0] * 26

            for ch in word:
                count[ord(ch)-ord("a")] += 1

            output[tuple(count)].append(word)

        return list(output.values())


        

        
            
        