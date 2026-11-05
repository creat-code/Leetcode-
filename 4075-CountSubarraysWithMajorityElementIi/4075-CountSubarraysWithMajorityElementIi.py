# Last updated: 11/5/2026, 9:23:23 PM
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pref = n

        freq = [0] * (2 * n + 1)
        freq[n] = 1

        less = 0
        ans = 0

        for num in nums:
            if num == target:
                less += freq[pref]
                pref += 1
            else:
                pref -= 1
                less -= freq[pref]

            freq[pref] += 1
            ans += less

        return ans