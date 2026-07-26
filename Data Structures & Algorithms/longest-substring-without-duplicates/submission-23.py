class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        left = 0
        charSet = set()
        for i in range(len(s)):  
            while s[i] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[i])
            result = max(result, i - left+1 )
        return result
        