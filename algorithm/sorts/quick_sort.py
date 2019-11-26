# =============================================================================
# Author: falseuser
# Created Time: 2019-10-30 17:00:46
# Last modified: 2019-10-30 17:51:02
# Description: 快速排序
# 使用原地排序方式，减小空间复杂度
# =============================================================================


def sort(collection):
    if len(collection) <= 1:
        return collection

    def move(sub, first, last):
        if first >= last:  # 临界条件，无法继续拆分子序列
            return
        pivot = sub[first]
        low = first
        high = last
        while low < high:
            while low < high and sub[high] >= pivot:
                high = high - 1
            sub[low] = sub[high]
            while low < high and sub[low] < pivot:
                low = low + 1
            sub[high] = sub[low]
        sub[low] = pivot
        move(sub, first, low-1)
        move(sub, low+1, last)

    move(collection, 0, len(collection)-1)
    return collection


if __name__ == "__main__":
    collection = [2, 3, 5, 1, 4, 8, 6]
    print(sort(collection))
