import bisect
from typing import List


def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    median = lambda a: (a[(len(a) - 1) // 2] + a[len(a) // 2]) / 2
    a = sorted(nums[:k])
    res = [median(a)]
    for i, j in zip(nums[:-k], nums[k:]):
        a.pop(bisect.bisect_left(a, i))
        a.insert(bisect.bisect_left(a, j), j)
        res.append(median(a))
    return res


def main():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(medianSlidingWindow(nums, k))


if __name__ == '__main__':
    main()