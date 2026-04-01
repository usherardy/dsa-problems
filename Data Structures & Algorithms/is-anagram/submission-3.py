class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        #quick solution, we sort and see if the strings are euqal => Anagram. 
        #Time: O(n log n)
        #Space: O(n)


            
        
            

        
        