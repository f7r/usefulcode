# =============================================================================
# Author: falseuser
# Created Time: 2019-06-24 15:49:57
# Last modified: 2019-06-24 17:49:08
# Description: 6.py
# =============================================================================


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size = len(s)
        form = []
        c = 0
        for i in range(numRows):
            form.append([])
        for i in range(size):
            if numRows == 1:
                return s
            j = i % (numRows + numRows - 2)
            if j == 0:
                c += 1  # 周期
            if j >= 0 and j < numRows:
                form[j].insert(c*(numRows-1), s[i])
            elif j >= numRows and j < (numRows + numRows - 2):
                form[2*numRows-2-j].insert(c*(numRows-1)+(j-(numRows-1)), s[i])
        for row in form:
            print(row)
        Str = ""
        for row in form:
            for b in row:
                Str = Str + b
        return Str.replace(" ", "")


if __name__ == "__main__":
    s = Solution()
    print(s.convert("LEETCODEISHIRING", 2))
