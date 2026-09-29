class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        ord_a = ord("a")

        for i in range(len(s)):
            count[ord(s[i]) - ord_a] += 1
            count[ord(t[i]) - ord_a] -= 1
        
        return not any(count)
