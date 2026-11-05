# Last updated: 11/5/2026, 9:25:25 PM
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        reversed = str(x)[::-1]
        if str(x) == reversed:
            return True