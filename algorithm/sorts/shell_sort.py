# =============================================================================
# Author: falseuser
# Created Time: 2019-10-31 18:20:11
# Last modified: 2019-10-31 18:28:20
# Description: 希尔排序
# =============================================================================


def sort(collection):
    # 初始步长
    gap = len(collection) // 2
    while gap > 0:
        for i in range(gap, len(collection)):
            value = collection[i]
            j = i
            # 前gap项做比较
            while j >= gap and collection[j-gap] > value:
                collection[j] = collection[j-gap]
                j = j - gap
            collection[j] = value
        gap = gap // 2
    return collection


if __name__ == "__main__":
    collection = [1, 8, 4, 7, 8, 10, 23, 6]
    print(sort(collection))
