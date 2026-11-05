# Last updated: 11/5/2026, 9:25:27 PM
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]: 
            return s
        pal = ""
        for x in range(len(s)):
            for i in range(1,len(s)+1):
                check = s[x:i]
                rev = check[::-1]
                if check == rev  and len(check) > len(pal):
                    pal = check

        return pal

            
      



        