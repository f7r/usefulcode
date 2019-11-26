# =============================================================================
# Author: falseuser
# Created Time: 2019-10-30 14:41:25
# Last modified: 2019-10-30 15:08:48
# Description: 归并排序
# 通过递归把序列分割成多个已排序的子序列，子序列最小长度为0，然后将子序列归并
# =============================================================================


def sort(collection):

    def merge(left, right):
        merged = []
        while left and right:
            if left[0] < right[0]:
                merged.append(left.pop(0))
            else:
                merged.append(right.pop(0))

        # 如果有一边的全部项都已插入merged，另一边剩下的项直接插入
        if left:
            merged.extend(left)
        if right:
            merged.extend(right)
        return merged

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2

    # 递归处理左右子序列
    return merge(sort(collection[:mid]), sort(collection[mid:]))


if __name__ == "__main__":
    collection = [4, 2, 1, 3, 8, 7, 5, 3]
    print(sort(collection))
