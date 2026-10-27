class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        rev = 0
        while x > rev:
            last = x % 10
            rev = (rev * 10) + last
            x = x // 10
        
        return rev == x or x == rev // 10