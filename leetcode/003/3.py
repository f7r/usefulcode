# =============================================================================
# Author: falseuser
# Created Time: 2019-06-20 14:55:27
# Last modified: 2019-06-21 10:55:46
# Description: 3.py
# =============================================================================


class Solution:
    def lengthOfLongestSubstring1(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        d = {}
        for i in range(len(s)):
            if s[i] not in s[l:r]:
                r += 1
            else:
                l = d[s[i]] + 1
                r += 1
            d[s[i]] = i
            # print(s[l:r])
            if r - l > max_len:
                max_len = r - l
        return max_len

    def lengthOfLongestSubstring2(self, s: str) -> int:
        left = 0
        lookup = set()
        max_len = 0
        cur_len = 0
        for i in range(len(s)):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring1("abcxcasdasdqwrwxaabcbb"))
    print(s.lengthOfLongestSubstring2("abcxcasdasdqwrwxaabcbb"))
