# Last updated: 11/5/2026, 9:25:02 PM
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        words = s.split(" ")
        return len(words[-1])
        