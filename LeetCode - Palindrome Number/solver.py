class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        return z == z[::-1]
