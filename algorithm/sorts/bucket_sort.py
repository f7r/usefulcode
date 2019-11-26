# =============================================================================
# Author: falseuser
# Created Time: 2019-10-31 14:34:47
# Last modified: 2019-10-31 15:04:48
# Description: 桶排序
# =============================================================================


def sort(collection):
    if len(collection) <= 1:
        return collection

    min_value, max_value = min(collection), max(collection)
    buckets = [0 for i in range(min_value, max_value+1)]  # 减少buckets长度
    for i in collection:
        buckets[i-min_value] = buckets[i-min_value] + 1
    k = 0
    for j in range(len(buckets)):
        current = min_value + j
        while buckets[j] > 0:
            collection[k] = current
            buckets[j] = buckets[j] - 1
            k = k + 1
    return collection


if __name__ == "__main__":
    collection = [2, 5, 2, 7, 9, 6, 1]
    print(sort(collection))
