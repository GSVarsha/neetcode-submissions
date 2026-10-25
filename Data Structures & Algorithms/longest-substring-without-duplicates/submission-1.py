class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        l = 0
        best = 0
        for r in range(len(s)):
            ch = s[r]
            if ch in map:
                l = max(l, map[ch] + 1)
            best = max(best, r - l + 1)
            map[ch] = r
        return best 