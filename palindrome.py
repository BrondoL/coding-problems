# def isPalindrome(s):
#     rev_s = ""
#     for x in range(len(s)-1, -1, -1):
#         rev_s += s[x]
#     return rev_s == s

# def isPalindrome(s):
#     for x in range(len(s)-1, len(s)//2-1, -1):
#         if s[len(s)-1-x] != s[x]:
#             return False
#     return True

def isPalindrome(s, i):
    if i >= len(s) // 2:
        return True
    else:
        if s[i] != s[len(s)-1-i]:
            return False
        else:
            return isPalindrome(s, i+1)


# s = "amanaplanacanalpanama"
# print(isPalindrome(s, 0))
# s = "raceacar"
# print(isPalindrome(s, 0))

import unittest

class PalindromeTest(unittest.TestCase):
    def testPalindrome(self):
        self.assertTrue(isPalindrome("amanaplanacanalpanama",0))

    def testNotPalindrome(self):
        self.assertFalse(isPalindrome("raceacar", 0))

unittest.main()