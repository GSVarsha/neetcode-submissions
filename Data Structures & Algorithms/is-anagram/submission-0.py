class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = [0] * 26
        ord_a = ord("a")
        for c in s:
            ind = ord(c) - ord_a
            res[ind] += 1

        for c in t:
            ind = ord(c) - ord_a
            res[ind] -= 1
            if res[ind] < 0:
                return False
        
        return not any(res) > 0
