# =============================================================================
# Author: falseuser
# Created Time: 2019-10-29 17:31:50
# Last modified: 2019-10-29 17:47:24
# Description: 选择排序
# 从前往后扫描，找到未排序序列中的最小值，然后放到已排序序列的末尾
# =============================================================================


def sort(collection):
    for i in range(len(collection)-1):
        min_ = i
        # 找到最小值的索引
        for j in range(i+1, len(collection)):
            if collection[j] < collection[min_]:
                min_ = j
        if min_ != i:
            collection[min_], collection[i] = collection[i], collection[min_]
    return collection


if __name__ == "__main__":
    collection = [3, 2, 1, 4, 7, 9, 2]
    print(sort(collection))
