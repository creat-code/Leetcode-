# Last updated: 11/5/2026, 9:24:48 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = "".join(filter(str.isalnum, s)).lower()
        if new == new[::-1]:
            return True
        return False
            