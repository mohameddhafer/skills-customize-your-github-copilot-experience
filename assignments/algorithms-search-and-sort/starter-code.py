import random
import time
from typing import List, Optional


def linear_search(arr: List[int], target: int) -> Optional[int]:
    for i, v in enumerate(arr):
        if v == target:
            return i
    return None


def binary_search(arr: List[int], target: int) -> Optional[int]:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def insertion_sort(arr: List[int]) -> List[int]:
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    res = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res.extend(left[i:])
    res.extend(right[j:])
    return res


def quick_sort(arr: List[int]) -> List[int]:
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def time_fn(fn, *args, repeat=3):
    times = []
    for _ in range(repeat):
        t0 = time.perf_counter()
        fn(*args)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return min(times)


def demo():
    sizes = [100, 1000, 5000]
    for n in sizes:
        arr = [random.randint(0, n) for _ in range(n)]
        sorted_arr = sorted(arr)
        print(f"n={n}")
        print("  insertion_sort:", time_fn(insertion_sort, arr))
        print("  merge_sort:", time_fn(merge_sort, arr))
        print("  quick_sort:", time_fn(quick_sort, arr))
        print("  linear_search (target not present):", time_fn(linear_search, arr, -1))
        print("  binary_search (sorted, target not present):", time_fn(binary_search, sorted_arr, -1))


if __name__ == "__main__":
    demo()
