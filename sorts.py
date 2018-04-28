from random import randint


def qsort(arr, first, last):
    if last > first:
        mid = partition(arr, first, last)
        qsort(arr, first, mid - 1)
        qsort(arr, mid + 1, last)


def partition(arr, first, last):
    mid = arr[first]
    r = last
    l = first + 1
    is_fin = True

    while is_fin:
        while l <= r and arr[l] <= mid:
            l += 1
        while l <= r and arr[r] >= mid:
            r -= 1
        if r < l:
            is_fin = False
        else:
            arr[r], arr[l] = arr[l], arr[r]
    arr[r], arr[0] = arr[0], arr[r]
    return r


def merge_sort(arr):
    if len(arr) < 5:
        return sorted(arr)
    size = len(arr)
    mid = int(size / 2)
    arr_1 = merge_sort(arr[0:mid])
    arr_2 = merge_sort(arr[mid:size])
    return merge(arr_1, arr_2)


def merge(arr_1, arr_2):
    res = []
    index_1 = index_2 = 0
    while len(arr_1) != index_1 and len(arr_2) != index_2:
        if arr_1[index_1] > arr_2[index_2]:
            res.append(arr_2[index_2])
            index_2 += 1
        else:
            res.append(arr_1[index_1])
            index_1 += 1
    if len(arr_1) == index_1:
        res.extend(arr_2[index_2:])
    else:
        res.extend(arr_1[index_1:])
    return res


arr = [randint(0, 50) for _ in range(100)]
print(arr)

qsort(arr, 0, len(arr) - 1)
print(arr)
