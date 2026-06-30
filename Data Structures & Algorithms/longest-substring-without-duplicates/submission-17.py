class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            newSet = set()
            for j in range(i,len(s)):
                if s[j] in newSet:
                    break
                newSet.add(s[j])
            res = max(len(newSet),res)
        return res