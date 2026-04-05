class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for s in strs:
            count = [0] * 26 # creating frequenct array

            for char in s:
                count[ord(char) - ord('a')] +=1 #counting
            
            key = tuple(count) #hashable key

            anagram_map[key].append(s) #grouping

        return list(anagram_map.values())

         
#Using sorting
#Time: O(n * k) 
#Space: O(n * k)
