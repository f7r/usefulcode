# =============================================================================
# Author: falseuser
# Created Time: 2019-11-01 15:52:48
# Last modified: 2019-11-01 16:38:55
# Description: 堆排序
# 不断构造规模逐次减小的最大堆，并将每次堆的最大值与最后一项进行交换
# =============================================================================


def sort(collection):

    def max_heapify(heap, index, size):
        max_index = index
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < size and heap[left_index] > heap[max_index]:
            max_index = left_index

        if right_index < size and heap[right_index] > heap[max_index]:
            max_index = right_index

        if max_index != index:
            heap[max_index], heap[index] = heap[index], heap[max_index]
            max_heapify(heap, max_index, size)

    n = len(collection)
    for i in range(n//2-1, -1, -1):  # 从最后一个非叶子结点开始
        max_heapify(collection, i, n)

    for i in range(n-1, 0, -1):
        collection[i], collection[0] = collection[0], collection[i]
        # 交换后，collection[0]是较小项，需要尽快地将其下放
        max_heapify(collection, 0, i)

    return collection


if __name__ == "__main__":
    collection = [1, 3, 5, 3, 6, 2, 5, 7]
    print(sort(collection))
