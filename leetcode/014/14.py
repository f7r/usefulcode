# =============================================================================
# Author: falseuser
# Created Time: 2019-06-27 13:49:32
# Last modified: 2019-06-27 13:58:48
# Description: 14.py
# =============================================================================


class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        start = ""
        if strs:
            for b in strs[0]:
                start = start + b
                for s in strs:
                    if not s.startswith(start):
                        start = start[:-1]
                        break
        return start


if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
