# =============================================================================
# Author: falseuser
# Created Time: 2019-06-21 16:22:56
# Last modified: 2019-06-24 11:55:12
# Description: 5.py
# =============================================================================


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        size = len(s)
        for i in range(size):
            left = i
            right = i
            while left > 0 and right < size:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if len(longest) < right - left - 1:
                longest = s[left+1:right]
            left = i
            right = i + 1
            while left > 0 and right < size:
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            if len(longest) < right - left - 1:
                longest = s[left+1:right]
        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babbadad"))
