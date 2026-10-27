class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        rev = 0
        while num > 0:
            last = num % 10
            rev = (rev * 10) + last
            num = num // 10
        
        return rev == x